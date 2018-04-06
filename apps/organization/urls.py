# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/6 0006 13:03'
from django.conf.urls import url
from .views import OrgListView, AddUserAskView

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask')
]
