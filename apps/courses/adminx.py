# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 13:06'
import xadmin
from .models import Course, Lesson, Video, CourseResource


class CourseAdmin(object):
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']


class LessonAdmin(object):
    search_fields = ['course', 'name']
    list_display = ['course', 'name', 'add_time']
    list_filter = ['course__name', 'name', 'add_time']


class VideoAdmin(object):
    search_fields = ['lesson', 'name', 'url']
    list_display = ['lesson', 'name', 'url', 'add_time']
    list_filter = ['lesson__name', 'name', 'url', 'add_time']


class CourseResourceAdmin(object):
    search_fields = ['course', 'download', 'name']
    list_display = ['course', 'download', 'name', 'add_time']
    list_filter = ['course__name', 'download', 'name', 'add_time']


xadmin.site.register(Course, CourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
