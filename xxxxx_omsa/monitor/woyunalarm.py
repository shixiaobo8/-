#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
	电话语音接口外拨接口通知
"""
from django.conf import settings
import base64
import time
import urllib2,urllib
import hashlib
import json
import ssl
from requests import Request, Session

class woyunPhoneAlarm():
	"""
		电话告警类
	"""
	
	# 构造器
	def __init__(self):
		# 电话语音sig 账号
		self.account = settings.WOYUN_PHONE_ACCOUNT
		# 电话语音auth_token
		self.auth_token = settings.WOYUN_PHONE_AUTH_TOKEN
		# 电话语音请求地址
		self.callbaseUrl = settings.WOYUN_PHONE_URL
		# 电话语音appid
		self.appid = settings.WOYUN_PHONE_APPID
		# 电话语音显示号码
		self.displayNumber = settings.WOYUN_PHONE_DISPLAYNUM
		# 电话语音播放次数
		self.playTimes = settings.WOYUN_PHONE_PLAYTIMES

	# 获取系统当前时间
	def getCurrentTime(self):
		return time.strftime('%Y%m%d%H%M%S',time.localtime(time.time()))

	# md5 加密
	def Md5String(self,str):
		m = hashlib.md5()
		m.update(str)
		res = m.hexdigest()
		# print res
		# print res.upper()
		return res.upper()

	# 添加header头部信息
	def getHeaders(self):
		res = dict()
		authorization_str = self.account + ':' + self.getCurrentTime()
		authorization = base64.b64encode(authorization_str)
		res['Authorization'] = authorization
		res['Content-Type'] = 'application/json;charset=utf-8;'
		res['Accept'] = 'application/json;'
		# print res
		return res

	# post body 体数据
	def getBodyData(self,mediaTxt,phoneNumber):
		data = dict()
		data['appId'] = self.appid
		data['to'] = phoneNumber
		data['displayNum'] = self.displayNumber
		data['mediaTxt'] = mediaTxt
		data['playTimes'] = self.playTimes
		#data['mediaTxt'] = '服务器宕机了'
		# print data
		return json.dumps(data)

	# 获取最终的url
	def getCallUrl(self):
		sig_str = self.account + self.auth_token + self.getCurrentTime()
		# print sig_str
		sig = self.Md5String(sig_str)
		Url = self.callbaseUrl + sig
		# print "sig = %s"%sig
		# print "url = %s"%Url
		return Url

	# 发起api请求
	def startAction(self,mediaTxt,phoneNumber):
		res = dict()
		try:
			ab_url = self.getCallUrl()
			headers_data = self.getHeaders()
			body_data = self.getBodyData(mediaTxt,phoneNumber)
			# 忽略证书验证
			context = ssl._create_unverified_context()
			running_envs = settings.RUNUING_ENV
			http_proxy = dict()
			if running_envs == 'dev':
				http_proxy = settings.DEV_ENVS
			if running_envs == 'production':
				http_proxy = settings.PRODUCTION_ENVS
			s = Session()
			req = Request('POST', ab_url,
						  data=body_data,
						  headers=headers_data
						  )
			prepped = req.prepare()

			# do something with prepped.body
			# do something with prepped.headers

			resp = s.send(prepped,
						  verify=False,
						  proxies=http_proxy,
						  timeout=10
						  )
			res['response'] = resp.text
		except urllib2.URLError,e:
			print e
			res['response'] = str(e)
		return res
