# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/7  5:26'

from django.conf.urls import url
from .views import CourseListView, CourseDetailView, CourseVideoView, CourseCommentView, AddCommentView

urlpatterns = [
    url(r'^list/$', CourseListView.as_view(), name='course_list'),
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),
    url(r'^video/(?P<course_id>\d+)/$', CourseVideoView.as_view(), name='course_video'),
    url(r'^comment/(?P<course_id>\d+)/$', CourseCommentView.as_view(), name='course_comment'),
    # 添加课程评论
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),

]
