# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-06-10 15:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_article_pub_time'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='_time',
            field=models.DateTimeField(null=True),
        ),
    ]