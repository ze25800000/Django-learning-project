# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/7  5:26'

from django.conf.urls import url
from .views import UserInfoView,ImageUploadView

urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),
    # 用户头像修改
    url(r'^image/upload/$', ImageUploadView.as_view(), name='image_upload'),

]
