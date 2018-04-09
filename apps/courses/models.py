from django.db import models
from datetime import datetime
from organization.models import CourseOrg, Teacher


# Create your models here.
class Course(models.Model):
    course_org = models.ForeignKey(CourseOrg, verbose_name='所属机构', null=True, blank=True)
    name = models.CharField(max_length=50, verbose_name=u"课程名")
    desc = models.CharField(max_length=300, verbose_name=u"课程描述")
    teacher = models.ForeignKey(Teacher, verbose_name='讲师', null=True, blank=True)
    detail = models.TextField(verbose_name=u"课程详细")
    degree = models.CharField(choices=(("cj", "初级"), ("zj", "中级"), ("gj", "高级")), max_length=2, verbose_name=u"难度")
    learn_times = models.IntegerField(default=0, verbose_name=u"学习次数")
    students = models.IntegerField(default=0, verbose_name=u"学习人数")
    fav_nums = models.IntegerField(default=0, verbose_name=u"收藏人数")
    is_banner = models.BooleanField(default=False, verbose_name='是否轮播')
    category = models.CharField(default='后端开发', max_length=20, verbose_name=u"课程类别")
    image = models.ImageField(upload_to="course/%Y/%m", verbose_name=u"封面")
    click_nums = models.IntegerField(default=0, verbose_name=u"点击数")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")
    tag = models.CharField(max_length=10, verbose_name='课程标签', default='')
    you_need_know = models.CharField(max_length=300, verbose_name='课程须知', default='')
    teacher_tell = models.CharField(max_length=300, verbose_name='老师告诉你', default='')

    class Meta:
        verbose_name = u"课程"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_zj_nums(self):
        return self.lesson_set.all().count()

    def get_learn_users(self):
        return self.usercourse_set.all()[:5]

    def get_course_lesson(self):
        # 获取课程章节
        return self.lesson_set.all()

    def get_course_resource(self):
        # 获取课程章节
        return self.courseresource_set.all()


class Lesson(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    name = models.CharField(max_length=100, verbose_name=u"章节名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"章节信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name

    def get_lession_viedo(self):
        return self.video_set.all()


class Video(models.Model):
    lesson = models.ForeignKey(Lesson, verbose_name=u'章节')
    name = models.CharField(max_length=100, verbose_name=u"视频名称")
    url = models.CharField(max_length=200, verbose_name='视频地址', default='')
    learn_times = models.IntegerField(default=0, verbose_name=u"学习时长", )
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"视频信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class CourseResource(models.Model):
    course = models.ForeignKey(Course, verbose_name=u"课程")
    download = models.FileField(upload_to="course/resource/%Y/%m", verbose_name=u"资源文件", max_length=100)
    name = models.CharField(max_length=100, verbose_name=u"名称")
    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"课程资源"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
