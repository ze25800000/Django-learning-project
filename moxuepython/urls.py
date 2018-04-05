from django.conf.urls import url, include
from django.views.generic import TemplateView
from users.views import LoginView, RegisterView, ActiveUserView, ForgetPwdView, ResetView, ModifyPwdView
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$', LoginView.as_view(), name="login"),
    url(r'^register/$', RegisterView.as_view(), name="register"),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^active/(?P<active_code>.*)/$', ActiveUserView.as_view(), name="user_active"),
    url(r'^forget/$', ForgetPwdView.as_view(), name='forget_pwd'),
    url(r'^reset/(?P<active_code>.*)/$', ResetView.as_view(), name='resetpwd'),
    url(r'^ModifyPwdView/$', ModifyPwdView.as_view(), name='modify_pwd')
]
