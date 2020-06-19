"""
# @Time    : 2020/6/16 17:37
# @Author  : zhoubin
# @Site    : 
# @File    : custom_site.py
# @Software: PyCharm
"""
from django.contrib.admin import AdminSite


class CustomSite(AdminSite):
    site_header = 'Typeidea'
    site_title = 'Typeidea管理后台'
    index_title = '首页'


custom_site = CustomSite(name='cus_admin')
