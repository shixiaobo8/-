#!/usr/bin/env python
# -*- coding:utf8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class WoVersionCheckHistory(models.Model):
    ctime = models.DateTimeField(blank=True, null=True)
    excel_name = models.CharField(max_length=255, blank=True, null=True)
    mtime = models.DateTimeField(blank=True, null=True)
    check_count = models.IntegerField(blank=True, null=True)
    file_exists_status = models.IntegerField(blank=True, null=True)
    tar_status = models.IntegerField(blank=True, null=True)
    excel_datas = models.TextField(blank=True, null=True)
    is_del = models.IntegerField(blank=True, null=True)
    creator = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'wo_version_check_history'

