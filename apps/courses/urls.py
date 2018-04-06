# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/7  5:26'

from django.conf.urls import url
from .views import CourseListView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    # url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
]
