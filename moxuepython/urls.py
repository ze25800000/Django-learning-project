from django.conf.urls import url, include
from django.views.static import serve
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView, LogoutView, \
    IndexView
from moxuepython.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', IndexView.as_view(), name="index"),
    # 配置上传文件的访问处理
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    # url(r'^static/(?P<path>.*)$', serve, {'document_root': STATIC_ROOT}),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^logout/$', LogoutView.as_view(), name="logout"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='resetpwd'),
    url(r'^ModifyPwdView/$', ModifyPwdView.as_view(), name='modify_pwd'),
    # 课程机构url配置
    url(r'^org/', include('organization.urls', namespace='org')),
    # 课程列表页
    url(r'^course/', include('courses.urls', namespace='course')),
    # 个人中心
    url(r'^users/', include('users.urls', namespace='users')),
]
# 全局404页面配置
handler404 = 'users.views.page_not_found'
# 全局500页面配置
handler500 = 'users.views.page_error'
