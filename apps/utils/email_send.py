# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 0005 22:17'

from users.models import EmailVerifyRecord
from random import Random
from django.core.mail import send_mail
from moxuepython.settings import EMAIL_FROM


def send_register_email(email, send_type="register"):
    email_record = EmailVerifyRecord()
    if send_type == 'update_email':
        random_str = generate_random_str(4)
    else:
        random_str = generate_random_str(16)
    email_record.code = random_str
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ""
    email_body = ""
    if send_type == 'register':
        email_title = "注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "密码重置链接"
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "修改邮箱链接"
        email_body = "你的邮箱验证码为：{0}".format(random_str)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass


def generate_random_str(randomlength=8):
    str = ''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasfdghjklzxcvbmn1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str
