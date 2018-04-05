from django.conf.urls import url
from django.views.generic import TemplateView
from users.views import user_login
import xadmin

urlpatterns = [
    url(r'^xadmin/', xadmin.site.urls),
    url(r'^$', TemplateView.as_view(template_name="index.html"), name="index"),
    url(r'^login/$', user_login, name="login")
]
