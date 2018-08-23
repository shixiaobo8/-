#!/usr/bin/env python
# -*- coding:utf8 -*-
# @Time    : 2018/3/8 11:26
# @Author  : Mat
# @Email   : v_ygshi@wesure.cn
# @File    : sendmail.py
# @Software: PyCharm
from django.core.mail import EmailMultiAlternatives
from django.conf import settings
import time
import json
# 发送邮件(含任务失败和成功邮件)

def sendMail(text_content,toEmails):
    # 给app部门组发送邮件
    try:
        service_name = 'test_service'
        now = time.strftime('%Y年%m月%d日 %H:%M:%S',time.localtime(time.time()))
        subject = now + ":weusure告警提醒"
        html_content = '<h3>'+subject+'</h3><p><h2>'+text_content+'</h2></p><p>注:</p><ul><li><a href="http://101.201.31.40:88/video/mp4AferCut?id=22">1.点击这里可以查看告警详情并修改告警状态以便记录告警</a></li><li>2.处理完告警请在企业微信群中告知</li></ul>'
        msg = EmailMultiAlternatives(subject, text_content, settings.EMAIL_FROM, toEmails)
        msg.attach_alternative(html_content, "text/html")
        res = msg.send()
        return {"server_time": now, "code": '200', 'mess': "给" + "".join(toEmails) + "发送邮件成功",'info':json.dumps(res)}
    except Exception,e:
        print e
        return {"server_time": now, "code": '205', 'mess': "给" + "".join(toEmails) + "发送邮件失败",'error':str(e)}