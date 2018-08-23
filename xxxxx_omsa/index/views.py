#!/usr/bin/env python
# -*- coding:utf8 -*-
# Create your views here.
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from django.views.decorators.http import require_http_methods
from django.shortcuts import render_to_response
from functools import wraps
from django.utils.decorators import available_attrs
from .models import Nav
from django.contrib.auth import authenticate,login as auth_login,logout as auth_logout
from django.contrib.auth.models import User
# from ldap_auth.ldap_test import login_ldap
# from ldap_auth.l_test import LDAPLogin
import json
import logging
import time
import requests


def get_nav():
    def func_wrapper(func):
        @wraps(func)
        def return_wrapper(*args, **wkargs):
            # 函数通过装饰起参数给装饰器传送参数
            # print 'before task',taskname
            # 装饰器传变量给函数
            # 获取navs
            navs = list(Nav.objects.all())
            summer, funcres = func(navs, *args, **wkargs)
            # print 'after task', taskid, summer
            return funcres
        return return_wrapper
    return func_wrapper


def database_error_decorator(func):
    def decorator(view_func):
        @wraps(view_func, assigned=available_attrs(view_func))
        def _wrapped_view(request, *args, **kwargs):
            try:
                return view_func(request, *args, **kwargs)
            except Exception as e:
                return database_error(request, message=e.message)

        return _wrapped_view
    return decorator(func)


@csrf_exempt
@database_error_decorator
def page_not_found(request):
    return render_to_response('common/404.html')

@database_error_decorator
@csrf_exempt
def page_error(request):
    return render_to_response('common/500.html')


@database_error_decorator
def register(request):
    if request.method == 'GET':
        return render(request,'index/register.html')


@require_http_methods(['GET','POST'])
@database_error_decorator
def index(request):
    navs = list(Nav.objects.all())
    login_datas = request.META
    print login_datas
    print request.body
    session = request.session
    username = login_datas['HTTP_X_WESURE_ENAME']
    user_chinesename = login_datas['HTTP_X_WESURE_NAME']
    request.user.username = username
    logger = logging.getLogger("login")  # 为loggers中定义的名称
    logger.info("time:%s name=%s    正在登陆" % (getCurrentTime(), username))
    return render(request, 'base/frame_boot_base.html', {"navs": navs})


# @database_error_decorator
@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    navs = list(Nav.objects.all())
    errors_list = []
    if request.method == 'POST':
        print request.body
        print request.META
        print 'pp: ', request.POST.get('username'), request.POST.get('password')
        username = request.POST.get('username')
        password = request.POST.get('password')
        request.user.username = username
        logger = logging.getLogger("login")  # 为loggers中定义的名称
        logger.info("time:%s name=%s  password:%s  正在登陆" % (getCurrentTime(),username,password))
        if ldap_username is not None:
        # if user is not None:
        #     auth_login(request,user)
            request.user.username = ldap_username
            logger.error("time:%s name=%s  password:%s  登陆成功" % (getCurrentTime(), username, password))
            return render(request,'base/frame_boot_base.html',{"navs":navs})
    logger.error("time:%s name=%s  password:%s  登陆失败" % (getCurrentTime(), username,password))
    return render(request,"index/login.html",{"error":"域用户名或域密码错误"})


@database_error_decorator
@csrf_exempt
@require_http_methods(["POST","GET"])
def changePwd(request):
    return render(request,'index/user/changePwd.html')


@database_error_decorator
@csrf_exempt
@require_http_methods(["POST","GET"])
def userinfo(request):
    navs = Nav.objects.all()
    return render(request,'index/user/userinfo.html',{"navs":navs})


def database_error(request, message):
    if message == "" or message is None:
        message = "Error detail is not given."
    context = {
        "database_error": message,
    }
    return render(request, "common/exception.html", context)


def getCurrentTime():
    return time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))

@require_http_methods(["POST","GET"])
def lay_test(request):
    res = {"code":0,"msg":"","count":1000,"data":[{"id":10000,"username":"user-0","sex":"女","city":"城市-0","sign":"签名-0","experience":255,"logins":24,"wealth":82830700,"classify":"作家","score":57},{"id":10001,"username":"user-1","sex":"男","city":"城市-1","sign":"签名-1","experience":884,"logins":58,"wealth":64928690,"classify":"词人","score":27},{"id":10002,"username":"user-2","sex":"女","city":"城市-2","sign":"签名-2","experience":650,"logins":77,"wealth":6298078,"classify":"酱油","score":31},{"id":10003,"username":"user-3","sex":"女","city":"城市-3","sign":"签名-3","experience":362,"logins":157,"wealth":37117017,"classify":"诗人","score":68},{"id":10004,"username":"user-4","sex":"男","city":"城市-4","sign":"签名-4","experience":807,"logins":51,"wealth":76263262,"classify":"作家","score":6},{"id":10005,"username":"user-5","sex":"女","city":"城市-5","sign":"签名-5","experience":173,"logins":68,"wealth":60344147,"classify":"作家","score":87},{"id":10006,"username":"user-6","sex":"女","city":"城市-6","sign":"签名-6","experience":982,"logins":37,"wealth":57768166,"classify":"作家","score":34},{"id":10007,"username":"user-7","sex":"男","city":"城市-7","sign":"签名-7","experience":727,"logins":150,"wealth":82030578,"classify":"作家","score":28},{"id":10008,"username":"user-8","sex":"男","city":"城市-8","sign":"签名-8","experience":951,"logins":133,"wealth":16503371,"classify":"词人","score":14},{"id":10009,"username":"user-9","sex":"女","city":"城市-9","sign":"签名-9","experience":484,"logins":25,"wealth":86801934,"classify":"词人","score":75}]}
    return HttpResponse(json.dumps(res))
