#!/usr/bin/env python
# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.
class Nav(models.Model):
    # 主键id
    id = models.AutoField(primary_key=True)
    # 一级左侧导航栏名称
    firstNavName = models.CharField(max_length=40, default="左侧导航栏名称", blank=True, null=True)
    # 一级左侧导航栏url
    firstNavUrl = models.CharField(max_length=40, default="#", blank=True, null=True)
    # # 一级左侧导航栏名称(可以手动添加)
    firstNavIconName = models.CharField(max_length=40, default="#", blank=True, null=True)
    # 二级左侧导航栏名称
    secondNavName = models.CharField(max_length=40, default="左侧导航栏二级分类名称", blank=True, null=True)
    # 二级左侧导航栏url
    secondNavUrl = models.CharField(max_length=40, default="#", blank=True, null=True)
    # 二级左侧导航栏名称
    thirdNavName = models.CharField(max_length=40, default="左侧导航栏二级分类名称", blank=True, null=True)
    # 二级左侧导航栏名称
    thirdNavUrl = models.CharField(max_length=40, default="#", blank=True, null=True)

    def __unicode__(self):
        return self.firstNavName