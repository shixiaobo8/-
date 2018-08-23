#!/usr/bin/env python
# -*- coding:utf8 -*-
# Create your views here.
from __future__ import division
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.shortcuts import render
from django.http import HttpResponse,HttpRequest,JsonResponse
from django.http.response import StreamingHttpResponse
import os,shutil
import string
import time
from django.conf import settings
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .forms import TestUEditorForm as editForm
import sys,re
from django.utils.html import mark_safe
from index.views import get_nav
import json
from index.models import Nav
import jenkins
import xlrd,xlwt
from .models import WoVersionCheckHistory
from Server.views import pagn

reload(sys)
sys.setdefaultencoding("utf-8")


# 获取文件的绝对路径
def getfilePath(up_dir,file):
    abpath = ''
    for f in os.listdir(up_dir + os.sep + file):
        new_path = up_dir+ os.sep + file + os.sep + f
        if os.path.isfile(new_path):
            abpath = new_path
        elif os.path.isdir(f):
            dir = new_path
            f = getfilePath(dir,f)
    return abpath


# 格式化时间
def formatTime(time_str):
    return time.strftime('%Y-%m-%d %H:%S:%M',time.localtime(time_str))


# 获取文件大小
def getSizeStr(filesize):
    s = ''
    if filesize/1024/1024/1024 > 1:
        s = str(filesize/1024/1024/1024) + 'G'
    elif filesize/1024/1024 > 1:
        s = str(filesize/1024/1024) + 'M'
    elif filesize/1024 > 1:
        s = str(round(filesize/1024,3)) + 'k'
    else:
        s = str(filesize) + 'b'
    return s


# 获取文件内容返回字符串
def getfileContent(file):
    content = ''
    if istextfile(file):
        with open(file,'rb') as f:
            content = f.read()
    return content


#检查一个字符串是文本还是二进制
def istextfile(filename, blocksize = 512):
    content = open(filename,'rb').read(blocksize)
    if contain_zh(content):
        return True
    else:
       return istext(content)


# 检查文件是文本文件还是二进制文件
def istext(s,text =''.join(map(chr,range(32,127))) + '\r\n\t\b',threshold = 0.30):
    _null_trans = string.maketrans('','')
    if '\0' in s:
        return False
    if not s:
        return True
    t = s.translate(_null_trans,text) #s中删除text中的字符
    return len(t)/(len(s) * 1.0) <= threshold
    # if "" in s:
    #     return False
    # if not s:  # Empty files are considered text
    #     return True
    # # Get the non-text characters (maps a character to itself then
    # # use the 'remove' option to get rid of the text characters.)
    # t = s.translate(_null_trans, text_characters)
    # # If more than 30% non-text characters, then
    # # this is considered a binary file
    # if len(t)/len(s) > 0.30:
    #     return False
    # return True

# 获取jenknins 服务
def getjkServer():
    try:
        jk_url = ''
        RUNUING_ENV = settings.RUNUING_ENV
        if RUNUING_ENV == 'default':
            jk_url = settings.DEFAULTS_JENKINS_SERVER_URL
        if RUNUING_ENV == 'dev':
            jk_url = settings.DEV_JENKINS_SERVER_URL
        if RUNUING_ENV == 'production':
            jk_url = settings.PRODUCTION_JENKINS_SERVER_URL
        jk_username = settings.JK_USERNAME
        jk_password = settings.JK_PASSWORD
        server = jenkins.Jenkins(jk_url,username=jk_username,password=jk_password)
        return server
    except Exception,e:
        print e

# 检查字符串中是否包含中文
def contain_zh(word):
    '''
    判断传入字符串是否包含中文
    :param word: 待判断字符串
    :return: True:包含中文  False:不包含中文
    '''
    # zh_pattern = re.compile(u'[\u4e00-\u9fa5]+')
    # try:
    #     word = word.decode()
    #     match = zh_pattern.search(word)
    #     return match
    # except Exception,e:
    #     return False
    try:
        for ch in word.decode('utf-8'):
            if u'\u4e00' <= ch <= u'\u9fff':
                return True
        return False
    except Exception,e:
        print e
        return False

# def check_contain_chinese(check_str):
#      for ch in check_str.decode('utf-8'):
#          if u'\u4e00' <= ch <= u'\u9fff':
#              return True
#      return False

# 获取文件详细信息
def getfileInfo(root_dir,file):
    filename = file.replace(root_dir,'')[1:].replace('\\','/').replace('_zhonggang_','-')
    file_sub = "".join(filename.split('.')[:-1])
    if contain_zh(file_sub):
        filename = filename.decode("utf-8")
    return {'content': mark_safe(getfileContent(file)), 'fid':file.replace(root_dir,'')[1:].replace('\\','/').replace('/','_slash_').replace('.','_sep_').replace('-','_zhonggang_'),'is_text':istextfile(file),'filename':filename,'filesize':getSizeStr(os.path.getsize(file)),'mtime':formatTime(os.path.getmtime(file)),'ctime':formatTime(os.path.getctime(file))}


@csrf_exempt
# 文件列表
def index(request):
    # @get_nav()
    # def getNav(navs):
    #     print navs
    #     return navs
    editform = editForm()
    if request.method == 'GET':
        up_dir = settings.UPLOADS_DIR
        files = []
        # navs = getNav()
        navs = list(Nav.objects.all())
        for file in os.listdir(up_dir):
            if os.path.isfile(up_dir + os.sep + file):
                files.append(getfileInfo(up_dir,up_dir + os.sep + file))
            elif os.path.isdir(up_dir + os.sep + file):
                files.append(getfileInfo(up_dir,getfilePath(up_dir,file)))
        # return HttpResponse(1112)
        return render(request,'uploads/index.html',{'files':files,"editform": editform,'navs':navs})


# 文件上传
@csrf_exempt
@require_http_methods(["POST"])
def uploadFiles(request):
    data = ''
    up_dir = settings.UPLOADS_DIR
    os.chdir(up_dir)
    if not os.path.exists(up_dir):
        os.makedirs(up_dir)
    if request.method == 'POST':
        files = request.FILES.get("newfile", None)  # 获取上传的文件,如果没有文件,则默认为None
        if not files:
            return HttpResponse(json.dumps({'data': "没有上传数据"}))
        save_destination = open(os.path.join(up_dir, files.name), 'wb+')  # 打开特定的文件进行二进制写操作
        for chunk in files.chunks():
            save_destination.write(chunk)
        save_destination.close()
        return HttpResponse(json.dumps({'error': data}))


# 文件上传
@csrf_exempt
@require_http_methods(["POST"])
def uploadExcel(request):
    data = ''
    up_dir = settings.UPLOADS_DIR
    os.chdir(up_dir)
    if not os.path.exists(up_dir):
        os.makedirs(up_dir)
    if request.method == 'POST':
        files = request.FILES.get("excel", None)  # 获取上传的文件,如果没有文件,则默认为None
        if not files:
            return HttpResponse(json.dumps({'status':'205','data':"没有上传数据"}))
        save_destination = open(os.path.join(up_dir, files.name), 'wb+')  # 打开特定的文件进行二进制写操作
        for chunk in files.chunks():
            save_destination.write(chunk)
        save_destination.close()
        # 读取excel数据
        excelDatas = getExcelData(files.name)
        # 检查文件字段列
        if excelDatas[0] != [u'\u670d\u52a1\u540d', u'Tag\u53f7']:
            return HttpResponse(json.dumps({'status': 205, 'data': 'excel格式不正确,请重新上传!'}))
        return HttpResponse(json.dumps({'status':'200','data': "文件上传成功!"}))


def getExcelData(filename):
    res = []
    up_dir = settings.UPLOADS_DIR
    os.chdir(up_dir)
    file = filename.encode('gbk')
    if not os.path.exists(file):
        return [{'error':'文件不存在'}]
    data = xlrd.open_workbook(filename)
    table = data.sheets()[0]
    # 列总数
    ncols = table.ncols
    # 行总数
    nrows = table.nrows
    for i in range(0,nrows):
        row_data = table.row_values(i)
        if data:
            res.append(row_data)
            continue
    return res


# 获取excel表格数据接口
@require_http_methods(['POST'])
@csrf_exempt
def getExcelTableJson(request):
    res = dict()
    # 获取文件名称
    filename = request.POST.get('filename', None)
    limit = request.POST.get('limit', None)
    offset = request.POST.get('offset', '0')
    page = request.POST.get('page', '1')
    sort = request.POST.get('sortOrder', 'asc')
    order_by = request.POST.get("sort", 'id')
    res['rows'] = []
    # 读取excel数据
    excelDatas = getExcelData(filename)
    # 检查文件字段列
    if excelDatas[0] != [u'\u670d\u52a1\u540d', u'Tag\u53f7']:
        return HttpResponse(json.dumps({'status':205,'data':'数据列表错误!'}))
    for i in range(0, len(excelDatas)):
        excelDatas[i].append(i)
    res['total'] = len(excelDatas) - 1
    # if limit:
    #     page = (int(offset) + 10) / int(limit)
    #     excelDatas = pagn(excelDatas, limit, page)
    # if not limit:
    #     excelDatas = pagn(excelDatas, 10, page)
    if page and not limit:
        excelDatas = pagn(excelDatas, 10, page)
    elif limit and page:
        excelDatas = pagn(excelDatas, limit, page)
    try:
        for i in range(0,len(excelDatas)):
            if page == '1' and i == 0:
                continue
            t_d = dict()
            t_d['id'] = excelDatas[i][2]
            t_d['service_name'] = excelDatas[i][0]
            t_d['tag'] = excelDatas[i][1]
            res['rows'].append(t_d)
    except Exception,e:
        print e
    res['count'] = res['total']
    res['status'] = 200
    res['msg'] = ''
    return HttpResponse(json.dumps(res))


# 文件编辑保存
@csrf_exempt
@require_http_methods(["POST"])
def editsave(request):
    res = commom_res()
    contents = request.POST.get('content',None)
    filename = request.POST.get('fid',None)
    filename = filename.replace('_sep_','.').replace('_slash_','/').replace('_zhonggang_','-')
    up_dir = settings.UPLOADS_DIR
    filename = up_dir + '/' + filename
    save_destination = open(filename, 'wb+')  # 打开特定的文件进行二进制写操作
    save_destination.write(contents)
    save_destination.close()
    res['data'] = "保存成功!"
    return HttpResponse(json.dumps(res))


# 基础公共返回信息
def commom_res():
    res = {}
    res['data'] = ''
    res['code'] = '200'
    return res


# 文件重命名
@csrf_exempt
@require_http_methods(["POST"])
def chfilename(request):
    res = commom_res()
    oldfilename = request.POST.get('old_filename',None)
    newfilename = request.POST.get('new_filename',None)
    if oldfilename and newfilename:
        oldfilename = oldfilename.replace('_slash_','/').replace('_sep_','.').replace('_zhonggang_','-')
        up_dir = settings.UPLOADS_DIR
        try:
            os.rename(up_dir+'/'+oldfilename,up_dir+'/'+newfilename)
            res['data'] = '文件名修改成功!'
        except Exception,e:
            print e
            res['data'] = str(e)
            res['code'] = '500'
    else:
        res['data'] = '前端传参错误'
        res['code'] = '500'
    return HttpResponse(json.dumps(res))


# 文件删除
@csrf_exempt
@require_http_methods(["POST"])
def delteFile(request):
    res = commom_res()
    filename = request.POST.get("filename",None)
    filename1 = filename
    # 和前端约定好的fid 命名规范 _slash_ 表示目录路径分隔符  __sep 表示后缀名.
    server_filename = filename.replace('_slash_','/').replace('_sep_','.').replace('_zhonggang_','-')
    up_dir = settings.UPLOADS_DIR
    server_filename = up_dir + '/' + server_filename
    try:
        os.chdir(up_dir)
        if '_slash' in filename1:
            shutil.rmtree(os.path.dirname(server_filename))
        else:
            os.remove(server_filename)
        res['code'] = 200
        res['data'] = '删除成功!'
    except Exception,e:
        print e
        res['code'] = 500
        res['data'] = str(e)
    return HttpResponse(json.dumps(res))


# 文件下载
@csrf_exempt
@require_http_methods(["GET"])
@xframe_options_sameorigin
def f_download(request):
    res = commom_res()
    updir = settings.UPLOADS_DIR
    filename = request.GET.get('fid',None)
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    if filename:
        fid = filename
        f_name = filename.replace('_slash_','/').replace('_sep_','.').replace('_zhonggang_','-')
        filename = updir + '/' + f_name
        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format(f_name)
        res['data'] = {'filename':fid,'result':'下载成功','server_time':repr(time.time())}
        return response
    else:
        res['data'] = "文件不存在！"
        return JsonResponse(res)


# exceldemo文件下载
@csrf_exempt
@require_http_methods(["GET"])
@xframe_options_sameorigin
def dlExceldemo(request):
    res = commom_res()
    updir = settings.UPLOADS_DIR
    filename = updir.replace("\\",'/') + '/' + 'versionDemo.xlsx'
    def file_iterator(file_name, chunk_size=512):
        with open(file_name,'rb') as f:
            while True:
                c = f.read(chunk_size)
                if c:
                    yield c
                else:
                    break
    if os.path.exists(filename):
        response = StreamingHttpResponse(file_iterator(filename))
        response['Content-Type'] = 'application/octet-stream'
        response['Content-Disposition'] = 'attachment;filename="{0}"'.format("versionDemo.xlsx")
        res['data'] = {'filename':"versionDemo.xlsx",'result':'下载成功','server_time':repr(time.time())}
        return response
    else:
        res['data'] = "文件不存在！"
        return JsonResponse(res)


# ace fileedit
@require_http_methods(["GET"])
def aceFileEdit(request):
    fid = request.GET.get("fid",None)
    updir = settings.UPLOADS_DIR
    if fid:
        filename = updir + '/' + fid.replace('_slash_','/').replace('_sep_','.').replace('_zhonggang_','-')
        # return render(request,'uploads/ace_editor_demo.html',{"filename":filename,'content':mark_safe(getfileContent(filename)),"fid":fid})
        return render(request, 'uploads/ace_editor_demo.html',{"filename": filename, 'content': mark_safe(getfileContent(filename)), "fid": fid})
    else:
        return render(request, 'uploads/ace_editor_demo.html',
                      {"message":"没有找到合适的文件,请先去文件上传列表选择要编辑的文件"})


def step_test(request):
    job_params = getJobParams('OS_PROD_MTLFWIM_BUILD')
    print job_params
    navs = list(Nav.objects.all())
    return render(request,'uploads/step.html',{'navs':navs,'jps':job_params})


def getJobParams(job_name):
    res = []
    jk_server = getjkServer()
    jobs_configs = jk_server.get_job_info_regex(job_name)
    job_config = []
    # 获取单个job配置参数
    for jobs in jobs_configs:
        if jobs['name'] == job_name:
            job_config = jobs['property'][0]['parameterDefinitions']
    res = []
    for p in job_config:
        node = dict()
        node['description'] = p['description']
        node['name'] = p['name']
        if p['_class'] == 'hudson.model.TextParameterDefinition':
            p = p['defaultParameterValue']
            node['value'] = p['value']
            node['type'] = 'input'
            res.append(node)
        if p['_class'] == 'hudson.model.StringParameterValue':
            node['value'] = p['value']
            node['type'] = 'select'
            res.append(node)
        if p['_class'] == 'hudson.model.BooleanParameterValue':
            node['type'] = 'boolean'
            node['choices'] = p['choices']
            res.append(node)
        if p['_class'] == 'hudson.model.PasswordParameterDefinition':
            node['type'] = 'password'
            res.append(node)
        if p['_class'] == 'hudson.model.FileParameterDefinition':
            node['type'] = 'file'
            res.append(node)
    return res


# 版本发布文件包检查
def versionFileCheck(request):
    navs = list(Nav.objects.all())
    return render(request,'uploads/versionCheck.html',{'navs':navs})


# 获取his接口json
@csrf_exempt
@require_http_methods(['POST'])
def getVerCheckHisJson(request):
    res = dict()
    # 获取文件名称
    filename = request.POST.get('filename', None)
    limit = request.POST.get('limit', None)
    offset = request.POST.get('offset', '0')
    page = request.POST.get('page', '1')
    sort = request.POST.get('sortOrder', 'asc')
    order_by = request.POST.get("sort", 'id')
    res['rows'] = []
    # 获取历史操作数据
    wchDatas = WoVersionCheckHistory.objects.all().values()
    res['total'] = len(wchDatas)
    if page and not limit:
        wchDatas = pagn(wchDatas, 10, page)
    elif limit and page:
        wchDatas = pagn(wchDatas, limit, page)
    try:
        for wD in wchDatas:
            t_d = dict()
            t_d['id'] = wD['id']
            t_d['ctime'] = wD['ctime'].strftime("%Y-%m-%d %H:%M:%S")
            t_d['mtime'] = wD['mtime'].strftime("%Y-%m-%d %H:%M:%S")
            t_d['creator'] = wD['creator']
            t_d['excel_name'] = wD['excel_name']
            t_d['check_count'] = wD['check_count']
            t_d['file_exists_status'] = wD['file_exists_status']
            t_d['tar_status'] = wD['tar_status']
            res['rows'].append(t_d)
    except Exception, e:
        print e
    res['count'] = res['total']
    res['status'] = 200
    res['msg'] = ''
    return HttpResponse(json.dumps(res))


@csrf_exempt
@require_http_methods(['POST'])
# 获取选择字段值
def selectVHFiledValue(request):
    res = []
    selectField = request.POST.get("selectField", None)
    if selectField == 'is_ok':
        wvch = WoVersionCheckHistory.objects.values_list(selectField, flat=True)
    elif selectField == 'is_notok':
        wvch = WoVersionCheckHistory.objects.values_list(selectField, flat=True)
    elif selectField == 'is_del':
        wvch = WoVersionCheckHistory.objects.values_list(selectField, flat=True)
    else:
        return HttpResponse(json.dumps({"data":"参数传递错误!"}))
    # 去掉unicode
    for w in wvch:
        res.append(w)
    return HttpResponse(json.dumps(list(set(res))))


# 查询version check 历史接口
@csrf_exempt
@require_http_methods(['POST'])
def getVersionHisListJson(request):
    data = request.POST
    return HttpResponse(json.dumps(data))