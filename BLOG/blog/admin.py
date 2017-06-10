# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from models import Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'pub_time')  # 设置后台管理系统显示文章标题/字段和发布日期
    list_filter = ('pub_time',)  # 设置日期过滤器


admin.site.register(Article, ArticleAdmin)
