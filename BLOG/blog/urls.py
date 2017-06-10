# -*- coding: utf-8 -*-
from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^$', views.index),  # 主页地址（http://127.0.0.1:8000/blog/）
    # 文章页地址（http://127.0.0.1:8000/blog/article/ID）
    url(r'^article/(?P<article_id>[0-9]+)/$', views.article_page, name='article_page'),
    # 编辑文章页地址（http://127.0.0.1:8000/blog/edit/ID）
    url(r'^edit/(?P<article_id>[0-9]+)/$', views.edit_page, name='edit_page'),
    # 跳转至编辑文章页地址，没有这个url，新建文章和修改文章的url打不开
    url(r'^edit/action$', views.edit_action, name='edit_action'),
]
