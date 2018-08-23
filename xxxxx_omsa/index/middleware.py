#!/usr/bin/env python
# -*- coding:utf8 -*-
# @Time    : 2018/3/14 14:38
# @Author  : Mat
# @Email   : v_ygshi@wesure.cn
# @File    : middleware.py
# @Software: PyCharm
import requests
from django.http import HttpResponseRedirect
from django.conf import settings

class WesureGwAuthMiddleware(object):
    def process_request(self, request):
        login_datas = request.META
        print login_datas
        print request.body
        session = request.session
        username = login_datas.get('HTTP_X_WESURE_ENAME')
        gw_url = ''
        RUNUING_ENV = settings.RUNUING_ENV
        if RUNUING_ENV == 'default':
            gw_url = settings.DEFAULTS_DEPLOY_DOMAIN
        if RUNUING_ENV == 'dev':
            gw_url = settings.DEV_DEPLOY_DOMAIN
        if RUNUING_ENV == 'production':
            gw_url = settings.PRODUCTION_DEPLOY_DOMAIN
        c_userInfo = requests.get(gw_url + '/SolomonService/GetCurrentUserInfo',verify=False)
        print c_userInfo.text
        url = request.get_full_path()
        print url
        print login_datas
        if not username and 'monitor' not in url:
            return HttpResponseRedirect('/')
        if username:
            user_chinesename = login_datas['HTTP_X_WESURE_NAME']
            request.user.username = username
