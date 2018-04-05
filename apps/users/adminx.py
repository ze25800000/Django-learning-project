# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 10:46'
import xadmin
from .models import EmailVerifyRecord
from .models import Banner
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GlobalSettings(object):
    site_title = "杨泽后台管理系统"  # 设置头部logo文字
    site_footer = "杨泽就是你们老大"  # 设置底部公司
    menu_style = "accordion"  # 设置菜单折叠


class EmailVerifyRecordAdmin(object):
    search_fields = ['code', 'email', 'send_type']
    list_display = ['code', 'email', 'send_type', 'send_time']
    list_filter = ['code', 'email', 'send_type', 'send_time']


class BannerAdmin(object):
    search_fields = ['title', 'image', 'url', 'index']
    list_display = ['title', 'image', 'url', 'index', 'add_time']
    list_filter = ['title', 'image', 'url', 'index', 'add_time']


xadmin.site.register(EmailVerifyRecord, EmailVerifyRecordAdmin)
xadmin.site.register(Banner, BannerAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
