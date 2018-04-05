# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 0005 13:44'
import xadmin
from .models import UserAsk, CourseComments, UserFavorite, UserMessage, UserCourse


class UserAskAdmin(object):
    search_fields = ['name', 'mobile', 'course_name']
    list_display = ['name', 'mobile', 'course_name', 'add_time']
    list_filter = ['name', 'mobile', 'course_name', 'add_time']


class CourseCommentsAdmin(object):
    search_fields = ['user', 'course', 'comments']
    list_display = ['user', 'course', 'comments', 'add_time']
    list_filter = ['user', 'course', 'comments', 'add_time']


class UserFavoriteAdmin(object):
    search_fields = ['user', 'fav_id', 'fav_type']
    list_display = ['user', 'fav_id', 'fav_type', 'add_time']
    list_filter = ['user', 'fav_id', 'fav_type', 'add_time']


class UserMessageAdmin(object):
    search_fields = ['user', 'message', 'has_read']
    list_display = ['user', 'message', 'has_read', 'add_time']
    list_filter = ['user', 'message', 'has_read', 'add_time']


class UserCourseAdmin(object):
    search_fields = ['user', 'course']
    list_display = ['user', 'course', 'add_time']
    list_filter = ['user', 'course', 'add_time']


xadmin.site.register(UserAsk, UserAskAdmin)
xadmin.site.register(CourseComments, CourseCommentsAdmin)
xadmin.site.register(UserFavorite, UserFavoriteAdmin)
xadmin.site.register(UserMessage, UserMessageAdmin)
xadmin.site.register(UserCourse, UserCourseAdmin)
