# _*_ coding:utf-8 _*_
__author__ = 'yangze'
__date__ = '2018/4/5 0005 22:17'

from random import Random


def generate_random_str():
    str = ''
    chars = 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasfdghjklzxcvbmn1234567890'
    length = len(chars) - 1
    random = Random()
    for i in range(4):
        str += chars[random.randint(0, length)]
    return str


print(generate_random_str())
