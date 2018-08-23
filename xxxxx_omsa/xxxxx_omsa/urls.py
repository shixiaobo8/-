#!/usr/bin/env python
# -*- coding:utf8 -*-
"""wesure_omsa URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Import the include() function: from django.conf.urls import url, include
    3. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import url,include
from django.conf import settings
from django.contrib import admin
from uploads import views as uploads_view
from index import views as index_view
from Server import views as server_view
from django import VERSION
from monitor import views as monitor_view
if VERSION[0:2]>(1,3):
    from django.conf.urls import patterns, url
    from DjangoUeditor import views as ue_view
else:
    from DjangoUeditor import views as ue_view
    from django.conf.urls.defaults import patterns, url
    from ue_view import get_ueditor_controller

urlpatterns = [
    # url(r'^ueditor/',include('DjangoUeditor.urls' )),
    url(r'^ueditor/controller$',ue_view.get_ueditor_controller),
    url(r'^admin/', admin.site.urls),
    url(r'^file/upload$', uploads_view.index, name='fileList'),
    url(r'^file/upload/n_saveFiles$', uploads_view.uploadFiles, name='uploadFiles'),
    url(r'^file/upload/n_saveExcel$', uploads_view.uploadExcel, name='uploadExcel'),
    url(r'^file/upload/editsave$', uploads_view.editsave, name='editsave'),
    url(r'^file/edit$', uploads_view.aceFileEdit, name='ace_edit'),
    url(r'^server/status/list$', server_view.serverStatusList, name='server_list'),
    url(r'^server/getJkListJson$', server_view.JenkinslistJson, name='jk_list_json'),
    url(r'^server/getJkListbJson$', server_view.JenkinslistbJson, name='jk_list_bjson'),
    url(r'^server/getJkListbsJson$', server_view.JenkinslistbsJson, name='jk_list_bsjson'),
    url(r'^server/jenkins/checkSupervisorGroupName$', server_view.checkSupervisorGroupName, name='checkSupervisorGroupName'),
    url(r'^server/jenkins/prolist$', server_view.Jenkinslist, name='jk_list'),
    url(r'^server/jenkins/supGroupList$', server_view.supGroupList, name='supGroupList'),
    url(r'^server/jenkins/selectFiledValue$', server_view.selectFiledValue, name='selectFiledValue'),
    url(r'^server/versionCheckHis/selectFiledValue$', uploads_view.selectVHFiledValue, name='selectVersionHisFiledValue'),
    url(r'^server/jenkins/save$', server_view.JenkinslistSave, name='jk_list_save'),
    url(r'^server/jenkins/add$', server_view.JenkinslistAdd, name='jk_list_add'),
    url(r'^jenkins/sup_group/add$', server_view.JenkinsSupGroupAdd, name='jk_sup_groupAdd'),
    url(r'^jenkins/sup_group_add$', server_view.JenkinsSupGroup_Add, name='jk_sup_groupAdd'),
    url(r'^server/jenkinsList/del$', server_view.JkListDelById, name='JkListDelById'),
    url(r'^server/jenkins/list_form$', server_view.jenkinsEditForm, name='jenkinsEditForm'),
    url(r'^server/jenkins/detail_form$', server_view.jenkinsDetailForm, name='jenkinsDetailForm'),
    url(r'^server/jenkins/add_form.html$', server_view.jenkinsAddForm, name='jenkinsAddForm'),
    url(r'^server/status/list_json$', server_view.serverStatusListJson, name='server_list_json'),
    url(r'^server/jenkins/query$', server_view.jk_query, name='jk_query'),
    url(r'^server/status/list_sub$', server_view.serverStatusListSubJson, name='server_list_subjson'),
    url(r'^file/chfilename$', uploads_view.chfilename, name='chfilename'),
    url(r'^file/dl$', uploads_view.f_download, name='f_download'),
    url(r'^upload/DelteFile$', uploads_view.delteFile, name='delteFile'),
    url(r'reg$', index_view.register, name='register'),
    url(r'^$', index_view.index, name='index'),
    url(r'index/login$', index_view.login, name='login'),
    url(r'index/userinfo$', index_view.userinfo, name='userinfo'),
    url(r'monitor/LandingCalls$', monitor_view.LandingCalls, name='api_monitor_phone'),
    url(r'monitor/sendMail$', monitor_view.sendMailMonitor, name='api_monitor_mail'),
    url(r'index/user/changePwd.html$', index_view.changePwd, name='changePwd'),
    url(r'file/stepTest$', uploads_view.step_test, name='stepTest'),
    url(r'prd/version/check$', uploads_view.versionFileCheck, name='versionFileCheck'),
    url(r'server/getexcelTableJson$', uploads_view.getExcelTableJson, name='getExcelTableJson'),
    url(r'server/getVerCheckHisJson$', uploads_view.getVerCheckHisJson, name='getVerCheckHisJson'),
    url(r'server/getVersionHisListJson$', uploads_view.getVersionHisListJson, name='getVersionHisListJson'),
    url(r'^prd/version/dldemo$', uploads_view.dlExceldemo, name='dlExceldemo'),
]
handler404 = index_view.page_not_found
handler500 = index_view.page_error

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
