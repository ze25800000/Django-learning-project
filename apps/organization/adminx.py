# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 13:30'
import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin(object):
    search_fields = ['name', 'desc']
    list_display = ['name', 'desc', 'add_time']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin(object):
    search_fields = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city']
    list_display = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city', 'add_time']
    list_filter = ['name', 'desc', 'click_nums', 'fav_nums', 'image', 'address', 'city__name', 'add_time']
    relfield_style = 'fk-ajax'


class TeacherAdmin(object):
    search_fields = ['org', 'name', 'work_years', 'work_company']
    list_display = ['org', 'name', 'work_years', 'work_company']
    list_filter = ['org__name', 'name', 'work_years', 'work_company']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
