# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-03-13 12:23
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('WX_FUNC', '0002_citylist'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('UserName', models.CharField(max_length=40)),
                ('UserStatus', models.CharField(default='00', max_length=3)),
            ],
        ),
    ]
