#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.forms import forms
from  DjangoUeditor.forms import UEditorField

class TestUEditorForm(forms.Form):
    Description=UEditorField("描述",initial="abc",width=600,height=800)