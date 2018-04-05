# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 0005 17:47'
from django import forms
from captcha.fields import CaptchaField


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, min_length=6)


class RegisterForm(forms.Form):
    email = forms.EmailField(required=True)
    password = forms.CharField(required=True, min_length=6)
    captcha = CaptchaField()


class ForgetForm(forms.Form):
    email = forms.EmailField(required=True)
    captcha = CaptchaField()


class ModifyPwdForm(forms.Form):
    password1 = forms.CharField(required=True, min_length=6)
    password2 = forms.CharField(required=True, min_length=6)
