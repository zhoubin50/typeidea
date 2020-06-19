"""
# @Time    : 2020/6/16 17:04
# @Author  : zhoubin
# @Site    : 
# @File    : adminforms.py
# @Software: PyCharm
"""
from django import forms


class PostAdminForm(forms.ModelForm):
    desc = forms.CharField(widget=forms.Textarea, label='摘要', required=False)
