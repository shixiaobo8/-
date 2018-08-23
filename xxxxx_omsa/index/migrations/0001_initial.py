# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-02-09 08:12
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Nav',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('firstNavName', models.CharField(blank=True, default='\u5de6\u4fa7\u5bfc\u822a\u680f\u540d\u79f0', max_length=40, null=True)),
                ('firstNavUrl', models.CharField(blank=True, default='#', max_length=40, null=True)),
                ('firstNavIconName', models.CharField(blank=True, default='#', max_length=40, null=True)),
                ('secondNavName', models.CharField(blank=True, default='\u5de6\u4fa7\u5bfc\u822a\u680f\u4e8c\u7ea7\u5206\u7c7b\u540d\u79f0', max_length=40, null=True)),
                ('secondNavUrl', models.CharField(blank=True, default='#', max_length=40, null=True)),
                ('thirdNavName', models.CharField(blank=True, default='\u5de6\u4fa7\u5bfc\u822a\u680f\u4e8c\u7ea7\u5206\u7c7b\u540d\u79f0', max_length=40, null=True)),
                ('thirdNavUrl', models.CharField(blank=True, default='#', max_length=40, null=True)),
            ],
        ),
    ]