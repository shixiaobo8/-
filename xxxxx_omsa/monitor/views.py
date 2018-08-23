#! /usr/bin/env python
# -*- coding:utf8 -*-
"""
    监控+报警
"""
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest
from monitor.woyunalarm import woyunPhoneAlarm
from monitor.sendmail import sendMail
from index.views import getCurrentTime
import json
import logging


# 电话报警封装
@csrf_exempt
@require_http_methods(['POST'])
def LandingCalls(request):
    phoneNumbers = []
    bodyJson = eval(request.body)
    status = bodyJson['status']
    params = request.META['QUERY_STRING'].split('&')
    mediaTxt = "服务器ip" + bodyJson['commonAnnotations']['description'].replace("has been down for more than 30 seconds","已经宕机30秒了").replace(':',"端口号")
    for k in params:
        print k
        if 'phoneNumber' in k:
            phoneNumbers.append(k.split('=')[-1])
    print phoneNumbers,mediaTxt
    res = dict()
    if not mediaTxt:
        res['code'] = 202
        res['error'] = '请求参数中缺少文本信息参数mediaTxt'
    elif not phoneNumbers:
        res['code'] = 202
        res['error'] = '请求参数中缺少号码参数phoneNumber'
    elif mediaTxt and phoneNumbers:
        wal = woyunPhoneAlarm()
        res['data'] = []
        res['info'] = []
        res['code'] = []
    	if status == 'firing':
            for phoneNumber in phoneNumbers:
                ph_res = wal.startAction(mediaTxt,phoneNumber)
           	if eval(ph_res['response'])['statusCode'] == "000000":
       	            res['code'].append(200)
                    res['data'].append(ph_res['response'])
               	    res['info'].append('电话成功拨号通知给'+phoneNumber)
            else:
                res['code'].append(200)
                res['data'].append(ph_res['response'])
                res['info'].append(eval(ph_res['response'])['statusMsg'])
    else:
        res['code'] = 204
        res['error'] = '缺少mediaTxt参数和phoneNumber参数'
        res['info'] = '服务器错误'
    logger = logging.getLogger("monitor")  # 为loggers中定义的名称
    logger.info("time:%s 正在调用电话告警   告警信息为: '%s'  告警电话为:%s  告警结果为: %s" % (getCurrentTime(), mediaTxt, phoneNumbers,json.dumps(res)))
    logger.info("请求json body post信息体为:%s"%bodyJson)
    return  HttpResponse(json.dumps(res))


# 邮件报警封装
@csrf_exempt
@require_http_methods(['GET','POST'])
def sendMailMonitor(request):
    res = dict()
    text_content = request.GET.get('text_content',None)
    toEmails = request.GET.get('toEmails',None)
    if not text_content:
        res['code'] = 203
        res['info'] = '缺少text_content参数'
    elif not toEmails:
        res['code'] = 203
        res['info'] = '缺少toEmails参数'
    elif toEmails and text_content:
        res = sendMail(text_content,[toEmails])
        print res
    else:
        res['code'] = 203
        res['info'] = '缺少text_content(告警内容)参数和toEmails(告警人)参数'
    print res
    if res['code'] != '200':
        sendMail("有告警邮件发送失败了",['v_ygshi@wesure.cn'])
    logger = logging.getLogger("monitor")  # 为loggers中定义的名称
    logger.info("time:%s 正在调用邮件告警   告警信息为: '%s'  告警邮箱为为:%s  告警结果为: %s" % (
    getCurrentTime(),text_content,toEmails, json.dumps(res)))
    return HttpResponse(json.dumps(res))
