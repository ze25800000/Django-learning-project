import json
from django.shortcuts import render
from django.contrib.auth import authenticate, login
from django.contrib.auth.backends import ModelBackend
from django.db.models import Q  # 并集查询
from django.views.generic.base import View
from django.contrib.auth.hashers import make_password
from django.contrib.auth import logout
from django.http import HttpResponse, HttpResponseRedirect
from pure_pagination import Paginator, PageNotAnInteger

from .models import UserProfile, EmailVerifyRecord, Banner
from .forms import LoginForm, RegisterForm, ForgetForm, ModifyPwdForm
from utils.email_send import send_register_email
from utils.mixin_urls import LoginRequiredMixin
from .forms import UploadImageForm, UserInfoForm
from operation.models import UserCourse, UserFavorite, UserMessage
from organization.models import CourseOrg, Teacher
from courses.models import Course


class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username=username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None


class ActiveUserView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                user = UserProfile.objects.get(email=email)
                user.is_active = True
                user.save()
                return render(request, 'login.html')
        else:
            return render(request, 'active_fail.html')


class RegisterView(View):
    def get(self, request):
        register_form = RegisterForm()
        return render(request, "register.html", {'register_form': register_form})

    def post(self, request):
        register_form = RegisterForm(request.POST)
        if register_form.is_valid():
            user_name = request.POST.get('email', '')
            if UserProfile.objects.filter(email=user_name):
                return render(request, 'login.html', {"msg": '用户名已经注册', 'register_form': register_form})
            else:
                pass_word = request.POST.get('password', '')
                user_profile = UserProfile()
                user_profile.username = user_name
                user_profile.email = user_name
                user_profile.password = make_password(pass_word)
                user_profile.is_active = False
                user_profile.save()

                # 写入用户注册成功的消息
                user_message = UserMessage()
                user_message.user = user_profile.id
                user_message.message = '欢迎注册暮雪网在线网'
                user_message.save()

                send_register_email(user_name, "register")
                return render(request, 'login.html')
        else:
            return render(request, 'register.html')


class LoginView(View):
    def get(self, request):
        return render(request, "login.html", {})

    def post(self, request):
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user_name = request.POST.get('username', '')
            pass_word = request.POST.get('password', '')
            user = authenticate(username=user_name, password=pass_word)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    from django.core.urlresolvers import reverse
                    return HttpResponseRedirect(reverse('index'))
                else:
                    return render(request, 'login.html', {"msg": '用户未激活'})
            else:
                return render(request, 'login.html', {"msg": '用户名或密码错误'})
        else:
            return render(request, 'login.html', {'login_form': login_form})


class LogoutView(View):
    def get(self, request):
        logout(request)
        from django.core.urlresolvers import reverse
        return HttpResponseRedirect(reverse('index'))


class ForgetPwdView(View):
    def get(self, request):
        forget_form = ForgetForm()
        return render(request, 'forgetpwd.html', {'forget_form': forget_form})

    def post(self, request):
        forget_form = ForgetForm(request.POST)
        if forget_form.is_valid():
            email = request.POST.get('email', '')
            send_register_email(email, "forget")
            return render(request, 'send_success.html')
        else:
            return render(request, 'forgetpwd.html', {'forget_form': forget_form})


class ResetView(View):
    def get(self, request, active_code):
        all_records = EmailVerifyRecord.objects.filter(code=active_code)
        if all_records:
            for record in all_records:
                email = record.email
                return render(request, 'password_reset.html', {'email': email})
        else:
            return render(request, 'forgetpwd.html')
        return render(request, 'login.html')


class ModifyPwdView(View):
    """修改用户密码"""

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            email = request.POST.get('email', '')
            if pwd1 != pwd2:
                return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致'})
            user = UserProfile.objects.get(email=email)
            user.password = make_password(pwd1)
            user.save()
            return render(request, 'login.html')
        else:
            email = request.POST.get('email', '')
            return render(request, 'password_reset.html', {'email': email, 'msg': '密码不一致'})


class UserInfoView(LoginRequiredMixin, View):
    def get(self, request):
        return render(request, 'usercenter-info.html', {})

    def post(self, request):
        user_info_form = UserInfoForm(request.POST, instance=request.user)  # 如果不加instance，将怎讲数据，而不是修改
        if user_info_form.is_valid():
            user_info_form.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse(json.dumps(user_info_form.errors), content_type='application/json')


class ImageUploadView(LoginRequiredMixin, View):
    """用户修改头像"""

    # def post(self, request):
    #     image_form = UploadImageForm(request.POST, request.FILES)
    #     if image_form.is_valid():
    #         image = image_form.cleaned_data['image']
    #         request.user.image = image
    #         request.user.save()
    def post(self, request):
        # 既有model又有form的功能
        image_form = UploadImageForm(request.POST, request.FILES, instance=request.user)
        if image_form.is_valid():
            image_form.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse("{'status':'fail'}", content_type='application/json')


class UpdatePwdView(View):
    """个人中心修改用户密码"""

    def post(self, request):
        modify_form = ModifyPwdForm(request.POST)
        if modify_form.is_valid():
            pwd1 = request.POST.get('password1', '')
            pwd2 = request.POST.get('password2', '')
            if pwd1 != pwd2:
                return HttpResponse("{'status':'fail','msg':'密码不一致'}", content_type='application/json')
            user = request.user
            user.password = make_password(pwd1)
            user.save()
            return HttpResponse("{'status':'success'}", content_type='application/json')
        else:
            return HttpResponse(json.dumps(modify_form.errors), content_type='application/json')


class SendEmailCodeView(LoginRequiredMixin, View):
    """发送邮箱验证码"""

    def get(self, request):
        email = request.GET.get('email', '')
        if UserProfile.objects.filter(email=email):
            return HttpResponse("{'email':'邮箱已经存在'}", content_type='application/json')
        send_register_email(email, 'update_email')
        return HttpResponse("{'status':'success'}", content_type='application/json')


class UpdateEmailView(LoginRequiredMixin, View):
    """修改个人邮箱"""

    def post(self, request):
        email = request.POST.get('email', '')
        code = request.POST.get('code', '')
        existed_records = EmailVerifyRecord.objects.filter(email=email, code=code, send_type='update_email')
        if existed_records:
            user = request.user
            user.email = email
            user.save()
        else:
            return HttpResponse("{'email':'验证码出错'}", content_type='application/json')


class UserCourseView(LoginRequiredMixin, View):
    def get(self, request):
        """我的课程"""
        user_courses = UserCourse.objects.filter(user=request.user)
        return render(request, 'usercenter-mycourse.html', {
            "user_courses": user_courses
        })


class MyFavOrgView(LoginRequiredMixin, View):
    """我收藏的课程机构"""

    def get(self, request):
        user_org_favs = UserFavorite.objects.filter(user=request.user, fav_type=2)
        org_ids = [user_org_fav.fav_id for user_org_fav in user_org_favs]
        user_orgs = CourseOrg.objects.filter(id__in=org_ids)
        return render(request, 'usercenter-fav-org.html', {
            'user_fav_orgs': user_orgs
        })


class MyFavTeacherView(LoginRequiredMixin, View):
    def get(self, request):
        """我收藏的授课教师"""
        user_teacher_favs = UserFavorite.objects.filter(user=request.user, fav_type=3)
        teacher_ids = [user_teacher_fav.fav_id for user_teacher_fav in user_teacher_favs]
        user_teachers = Teacher.objects.filter(id__in=teacher_ids)
        return render(request, 'usercenter-fav-teacher.html', {
            "user_teachers": user_teachers
        })


class MyFavCourseView(LoginRequiredMixin, View):
    def get(self, request):
        """我收藏的公开课"""
        user_course_favs = UserFavorite.objects.filter(user=request.user, fav_type=1)
        course_ids = [user_course_fav.fav_id for user_course_fav in user_course_favs]
        user_courses = Course.objects.filter(id__in=course_ids)
        return render(request, 'usercenter-fav-course.html', {
            'user_courses': user_courses
        })


class UserMessageView(LoginRequiredMixin, View):
    """我的信息"""

    def get(self, request):
        all_message = UserMessage.objects.filter(user=request.user.id)

        all_unread_messages = UserMessage.objects.filter(user=request.user.id, has_read=False)
        for unread_message in all_unread_messages:
            unread_message.has_read = True
            unread_message.save()

        message_num = all_message.count()

        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_message, 9, request=request)

        message = p.page(page)

        return render(request, 'usercenter-message.html', {
            "all_message": message,
            "message_num": message_num
        })


class IndexView(View):
    def get(self, request):
        all_banners = Banner.objects.all().order_by('index')
        courses = Course.objects.filter(is_banner=False)[:6]
        banner_courses = Course.objects.filter(is_banner=True)[:3]
        course_orgs = CourseOrg.objects.all()[:15]
        return render(request, 'index.html', {
            'all_banners': all_banners,
            'courses': courses,
            'banner_courses': banner_courses,
            'course_orgs': course_orgs
        })


def page_not_found(request):
    # 全局404处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('404.html', {})
    response.status_code = 404
    return response


def page_error(request):
    # 全局500处理函数
    from django.shortcuts import render_to_response
    response = render_to_response('500.html', {})
    response.status_code = 500
    return response
