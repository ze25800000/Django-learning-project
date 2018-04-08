# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/7  5:26'

from django.conf.urls import url
from .views import UserInfoView, ImageUploadView, UpdatePwdView, SendEmailCodeView, UpdateEmailView, UserCourseView, \
    MyFavOrgView, MyFavTeacherView, MyFavCourseView, UserMessageView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 我的课程
    url(r'^course/$', UserCourseView.as_view(), name='user_course'),
    # 我的消息
    url(r'^message/$', UserMessageView.as_view(), name='user_message'),
    # 我的收藏课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),
    # 我的收藏的授课教师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),
    # 我的收藏的公开课
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),
    # 修改密码
    url(r'^update/pwd/$', UpdatePwdView.as_view(), name='update_pwd'),
    # 用户头像修改
    url(r'^image/upload/$', ImageUploadView.as_view(), name='image_upload'),
    # 发送邮箱验证码
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),
    # 修改邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),
]
