# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 13:06'
import xadmin
from .models import Course, Lesson, Video, CourseResource, BannerCourse
from organization.models import CourseOrg


class LessonInline(object):
    model = Lesson
    extra = 0


class CourseResourceInline(object):
    model = CourseResource
    extra = 0


class CourseAdmin(object):
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time', 'get_zj_nums']  # 模型中的方法也可以用于列表展示
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']  # 只能看不能改的内容
    list_editable = ['degree', 'desc']  # 在列表可以编辑的内容
    exclude = ['fav_nums']  # 禁止显示的内容
    inlines = [LessonInline, CourseResourceInline]  # 页面中嵌套外键关联的表
    refresh_times = [3, 5]  # 自动刷新

    # 将一张表分成两部分的方法
    def queryset(self):
        qs = super(CourseAdmin, self).queryset()
        qs = qs.filter(is_banner=False)
        return qs


class BannerCourseAdmin(object):
    search_fields = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums']
    list_display = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                    'add_time']
    list_filter = ['name', 'desc', 'detail', 'degree', 'learn_times', 'students', 'fav_nums', 'image', 'click_nums',
                   'add_time']
    ordering = ['-click_nums']
    readonly_fields = ['click_nums']
    exclude = ['fav_nums']
    inlines = [LessonInline, CourseResourceInline]

    # 将一张表分成两部分的方法
    def queryset(self):
        qs = super(BannerCourseAdmin, self).queryset()
        qs = qs.filter(is_banner=True)
        return qs

    def save_models(self):
        # 在保存课程的时候统计课程机构的课程数
        obj = self.new_obj
        obj.save()
        if obj.course_org is not None:
            course_org = obj.course_org
            course_org.course_nums = Course.objects.filter(course_org=course_org).count()
            course_org.save()


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
xadmin.site.register(BannerCourse, BannerCourseAdmin)
xadmin.site.register(Lesson, LessonAdmin)
xadmin.site.register(Video, VideoAdmin)
xadmin.site.register(CourseResource, CourseResourceAdmin)
