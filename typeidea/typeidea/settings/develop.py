"""
# @Time    : 2020/6/12 10:26
# @Author  : zhoubin
# @Site    :
# @File    : develop.py
# @Software: PyCharm
"""

from typeidea.settings.base import * # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'typeidea',
        'HOST': '192.168.13.1',
        'USER': 'root',
        'PASSWORD': 'zhoubin123',
        'TEST': {
            'NAME': 'mytestdatabase'
        }
    }
}