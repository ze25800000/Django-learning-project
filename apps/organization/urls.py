# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/6 0006 13:03'
from django.conf.urls import url
from .views import OrgListView, AddUserAskView, OrgHomeView, OrgCourseView, OrgDescView, OrgTeacherView, AddFavView, \
    TeacherListView, TeacherDetailView

urlpatterns = [
    url(r'^list/$', OrgListView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name='add_ask'),
    url(r'^home/(?P<org_id>\d+)/$', OrgHomeView.as_view(), name='org_home'),
    url(r'^course/(?P<org_id>\d+)/$', OrgCourseView.as_view(), name='org_course'),
    url(r'^desc/(?P<org_id>\d+)/$', OrgDescView.as_view(), name='org_desc'),
    url(r'^org_teacher/(?P<org_id>\d+)/$', OrgTeacherView.as_view(), name='org_teacher'),

    # 讲师列表页面
    url(r'^teacher/list/$', TeacherListView.as_view(), name='teacher_list'),
    # 讲师列表页面
    url(r'^teacher/detail/(?P<teacher_id>\d+)/$', TeacherDetailView.as_view(), name='teacher_detail'),
    # 机构收藏
    url(r'^add_fav/$', AddFavView.as_view(), name='add_fav'),
]
