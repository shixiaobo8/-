#!/usr/bin/env python
# -*- coding:utf8 -*-
"""
Django settings for xxxxx_omsa project.

Generated by 'django-admin startproject' using Django 1.9.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""

import os
from django.conf import settings as gSettings   #全局设置
import logging
import logging.config
import django.utils.log
import logging.handlers
import time
# import ldap
# from django_auth_ldap.config import LDAPSearch,LDAPSearchUnion, GroupOfNamesType #导入LDAP model

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.9/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'o06ict4yn*opp+)u$$v6+!5jbnk1_k=gffnhy8wxvelg^(3z07'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'DjangoUeditor',
    'index',
    'uploads',
    'Server',
    # 'ldap_auth',
    'logs',
]

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    # 'index.middleware.xxxxxGwAuthMiddleware',
# 调试工具
#    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'xxxxx_omsa.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'xxxxx_omsa.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases
# 数据库配置
DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': 'django_xxxxx_omsa',
	'USER': 'root',
	'PASSWORD':'123456',
	'HOST':'localhost',
	'PORT':'3306',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'zh-hans'

TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# 文件类型
FILE_CHARSET='utf-8'
DEFAULT_CHARSET='utf-8'


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

# 当运行 python manage.py collectstatic 的时候
# STATIC_ROOT 文件夹 是用来将所有STATICFILES_DIRS中所有文件夹中的文件，以及各app中static中的文件都复制过来
# 把这些文件放到一起是为了用apache等部署的时候更方便
STATIC_ROOT = os.path.join(BASE_DIR, 'collected_static')

# 其它 存放静态文件的文件夹，可以用来存放项目中公用的静态文件，里面不能包含 STATIC_ROOT
# 如果不想用 STATICFILES_DIRS 可以不用，都放在 app 里的 static 中也可以
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "common_static"),
    # '/path/to/others/static/',  # 用不到的时候可以不写这一行
)

# 这个是默认设置，Django 默认会在 STATICFILES_DIRS中的文件夹 和 各app下的static文件夹中找文件
# 注意有先后顺序，找到了就不再继续找了
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder"
)

# 上传的文件的保存位置
UPLOADS_DIR = os.path.join(BASE_DIR, "UP_FILES")
# upload folder
MEDIA_URL = UPLOADS_DIR + '/'
MEDIA_ROOT = UPLOADS_DIR + '/'

#工具栏样式，可以添加任意多的模式
TOOLBARS_SETTINGS={
    "besttome":[['source','undo', 'redo','bold', 'italic', 'underline','forecolor', 'backcolor','superscript','subscript',"justifyleft","justifycenter","justifyright","insertorderedlist","insertunorderedlist","blockquote",'formatmatch',"removeformat",'autotypeset','inserttable',"pasteplain","wordimage","searchreplace","map","preview","fullscreen"], ['insertcode','paragraph',"fontfamily","fontsize",'link', 'unlink','insertimage','insertvideo','attachment','emotion',"date","time"]],
    "mini":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','simpleupload','attachment']],
    "normal":[['source','|','undo', 'redo', '|','bold', 'italic', 'underline','removeformat', 'formatmatch','autotypeset', '|', 'forecolor', 'backcolor','|', 'link', 'unlink','|','simpleupload', 'emotion','attachment', '|','inserttable', 'deletetable', 'insertparagraphbeforetable', 'insertrow', 'deleterow', 'insertcol', 'deletecol', 'mergecells', 'mergeright', 'mergedown', 'splittocells', 'splittorows', 'splittocols']]
}

#默认的Ueditor设置，请参见ueditor.config.js
UEditorSettings={
    "toolbars":TOOLBARS_SETTINGS["normal"],
    "autoFloatEnabled":False,
    "defaultPathFormat":"%(basename)s_%(datetime)s_%(rnd)s.%(extname)s"   #默认保存上传文件的命名方式
}
#请参阅php文件夹里面的config.json进行配置
UEditorUploadSettings={
   #上传图片配置项
    "imageActionName": "uploadimage", #执行上传图片的action名称
    "imageMaxSize": 10485760, #上传大小限制，单位B,10M
    "imageFieldName": "upfile", #* 提交的图片表单名称 */
    "imageUrlPrefix":"",
    "imagePathFormat":"",
    "imageAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #上传图片格式显示

    #涂鸦图片上传配置项 */
    "scrawlActionName": "uploadscrawl", #执行上传涂鸦的action名称 */
    "scrawlFieldName": "upfile", #提交的图片表单名称 */
    "scrawlMaxSize": 10485760, #上传大小限制，单位B  10M
    "scrawlUrlPrefix":"",
    "scrawlPathFormat":"",

    #截图工具上传 */
    "snapscreenActionName": "uploadimage", #执行上传截图的action名称 */
    "snapscreenPathFormat":"",
    "snapscreenUrlPrefix":"",

    #抓取远程图片配置 */
    "catcherLocalDomain": ["127.0.0.1", "localhost", "img.baidu.com"],
    "catcherPathFormat":"",
    "catcherActionName": "catchimage", #执行抓取远程图片的action名称 */
    "catcherFieldName": "source", #提交的图片列表表单名称 */
    "catcherMaxSize": 10485760, #上传大小限制，单位B */
    "catcherAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #抓取图片格式显示 */
    "catcherUrlPrefix":"",
    #上传视频配置 */
    "videoActionName": "uploadvideo", #执行上传视频的action名称 */
    "videoPathFormat":"",
    "videoFieldName": "upfile", # 提交的视频表单名称 */
    "videoMaxSize": 102400000, #上传大小限制，单位B，默认100MB */
    "videoUrlPrefix":"",
    "videoAllowFiles": [
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid"], #上传视频格式显示 */

    #上传文件配置 */
    "fileActionName": "uploadfile", #controller里,执行上传视频的action名称 */
    "filePathFormat":os.path.join(BASE_DIR, "UP_FILES"),
    "fileFieldName": "upfile",#提交的文件表单名称 */
    "fileMaxSize": 204800000, #上传大小限制，单位B，200MB */
    "fileUrlPrefix": "",#文件访问路径前缀 */
    "fileAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml"
    ], #上传文件格式显示 */

    #列出指定目录下的图片 */
    "imageManagerActionName": "listimage", #执行图片管理的action名称 */
    "imageManagerListPath":"",
    "imageManagerListSize": 30, #每次列出文件数量 */
    "imageManagerAllowFiles": [".png", ".jpg", ".jpeg", ".gif", ".bmp"], #列出的文件类型 */
    "imageManagerUrlPrefix": "",#图片访问路径前缀 */

    #列出指定目录下的文件 */
    "fileManagerActionName": "listfile", #执行文件管理的action名称 */
    "fileManagerListPath":"",
    "fileManagerUrlPrefix": "",
    "fileManagerListSize": 30, #每次列出文件数量 */
    "fileManagerAllowFiles": [
        ".png", ".jpg", ".jpeg", ".gif", ".bmp",".tif",".psd"
        ".flv", ".swf", ".mkv", ".avi", ".rm", ".rmvb", ".mpeg", ".mpg",
        ".ogg", ".ogv", ".mov", ".wmv", ".mp4", ".webm", ".mp3", ".wav", ".mid",
        ".rar", ".zip", ".tar", ".gz", ".7z", ".bz2", ".cab", ".iso",
        ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".pdf", ".txt", ".md", ".xml",
        ".exe",".com",".dll",".msi"
    ] #列出的文件类型 */
}


#更新配置：从用户配置文件settings.py重新读入配置UEDITOR_SETTINGS,覆盖默认
def UpdateUserSettings():
    UserSettings=getattr(gSettings,"UEDITOR_SETTINGS",{}).copy()
    if UserSettings.has_key("config"):UEditorSettings.update(UserSettings["config"])
    if UserSettings.has_key("upload"):UEditorUploadSettings.update(UserSettings["upload"])

#读取用户Settings文件并覆盖默认配置
UpdateUserSettings()


#取得配置项参数
def GetUeditorSettings(key,default=None):
    if UEditorSettings.has_key(key):
        return UEditorSettings[key]
    else:
        return default

UEDITOR_SETTINGS={
"config":UEditorSettings,
"upload":UEditorUploadSettings
}

# ### log 配置部分BEGIN ### #
MONITOR_LOGS = os.path.join(BASE_DIR,'logs/monitor/'+ time.strftime('%Y_%m_%d_',time.localtime(time.time())) +'monitor.log')
DEFALUT_LOGS = os.path.join(BASE_DIR,'logs/' + time.strftime('%Y_%m_%d_',time.localtime(time.time())) + 'default.log')
LOGIN_LOGS = os.path.join(BASE_DIR, 'logs/login/'+ time.strftime('%Y_%m_%d_',time.localtime(time.time())) +'login.log')
DB_LOGS = os.path.join(BASE_DIR, 'logs/db/'+ time.strftime('%Y_%m_%d_',time.localtime(time.time())) +'dbsql.log')
stamdard_format = '[%(asctime)s][%(threadName)s:%(thread)d]' + \
                  '[task_id:%(name)s][%(filename)s:%(lineno)d] ' + \
                  '[%(levelname)s]- %(message)s'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {  # 详细
            'format': stamdard_format
        },
    },
    'handlers': {
        'default': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DEFALUT_LOGS,
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'db': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': DB_LOGS,
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'monitor': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': MONITOR_LOGS,
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'login': {
            'level': 'DEBUG',
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': LOGIN_LOGS,
            'maxBytes': 1024 * 1024 * 100,  # 5 MB
            'backupCount': 5,
            'formatter': 'standard',
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        }
    },
    'loggers': {
        'default': {  # default日志，存放于log中
            'handlers': ['default'],
            'level': 'DEBUG',
        },
        'monitor': {  # 监控告警日志，存放于log中
            'handlers': ['monitor'],
            'level': 'DEBUG',
        },
        'login': {  # 登陆日志，存放于log中
            'handlers': ['login'],
            'level': 'DEBUG',
        },
        'django.db.backends': {  # 数据库相关执行过程log打印到console
            'handlers': ['db'],
            'level': 'DEBUG',
        },
    }
}
# ### log 配置部分END ### #

######## 沃云电话告警参数配置start ########