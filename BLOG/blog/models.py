# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Article(models.Model):
    title = models.CharField(max_length=32, default='Title')  # 设置标题栏
    content = models.TextField(null=True)   # 设置文章内容编辑区
    pub_time = models.DateTimeField(auto_now=True)  # 设置文章发布日期

    def __unicode__(self):  # 设置字符串格式
        return self.title # 返回并显示出标题
