# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-16 16:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WX_FUNC', '0004_robotlog'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='robotlog',
            name='UserName',
        ),
        migrations.RemoveField(
            model_name='userlist',
            name='UserName',
        ),
        migrations.AddField(
            model_name='robotlog',
            name='FromUserName',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='robotlog',
            name='MsgId',
            field=models.CharField(default='', max_length=70),
        ),
        migrations.AddField(
            model_name='userlist',
            name='FromUserName',
            field=models.CharField(default='', max_length=100),
        ),
    ]
