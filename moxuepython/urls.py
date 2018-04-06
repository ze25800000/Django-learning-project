from django.conf.urls import url, include
from django.views.generic import TemplateView
from django.views.static import serve
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
from organization.views import OrgListView
from moxuepython.settings import MEDIA_ROOT
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    # 配置上传文件的访问处理
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),

    url(r'^login/$', LoginView.as_view(), name="login"),
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

    url(r'^org_list/$', OrgListView.as_view(), name='org_list')
]
