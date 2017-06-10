# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect

from . import models


def index(request):  # 设置主页
    articles = models.Article.objects.all()  # 获取所有文章列表（可在django shell中查看 详见印象笔记）
    return render(request, 'blog/index.html', {'articles': articles})  # 渲染index.html


def article_page(request, article_id):  # 设置文章页面
    article = models.Article.objects.get(pk=article_id)  # 获取文章ID
    return render(request, 'blog/article_page.html', {'article': article})  # 渲染article_page.html


def edit_page(request, article_id):  # 设置编辑文章页面
    if str(article_id) == '0':  # 判断文章是新建文章还是修改文章（新建文章id为0）
        return render(request, 'blog/edit_page.html')  # 渲染edit_page.html
    article = models.Article.objects.get(pk=article_id)  # 不是新建文章而是修改文章就获取待修改文章ID
    return render(request, 'blog/edit_page.html', {'article': article}) # 渲染待修改文章的页面


def edit_action(request):  # 设置编辑区域
    title = request.POST.get('title', 'TITLE')  # 请求文章标题
    content = request.POST.get('content', 'CONTENT')  # 请求文章内容
    article_id = request.POST.get('article_id', '0')  # 用dict的get方法判断文章ID是否是0

    if article_id == '0':  # 如果文章ID是0
        models.Article.objects.create(title=title, content=content)  # 创建新文章，编辑区域为空
        return HttpResponseRedirect('/blog/')

    article = models.Article.objects.get(pk=article_id)  # 否则获取文章ID
    article.title = title  # 编辑区域标题为原文标题，可编辑
    article.content = content  # 编辑区域内容为原文内容，可编辑
    article.save()  # 保存
    return HttpResponseRedirect('/blog/')  # 重新定向跳转回首页
