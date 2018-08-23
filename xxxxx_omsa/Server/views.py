#!/usr/bin/env python
# -*- coding:utf8 -*-
from __future__ import division
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from index.models import Nav
from django.http import HttpResponse
import json,time
import math
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.forms.models import model_to_dict
from .models import WoJenkinsServices,WoSupervisorGroup
from django.db import connection
from index.views import getCurrentTime
import types
# Create your views here.


def getServerStatusJson():
    running = "<img src='/static/img/running.png' />"
    stop = "<img src='/static/img/stop.png' />"
    prepare = "<img src='/static/img/huidu.png' />"
    service_data = [
        {"ip": "10.2.1.2", "service_name": "nginx", "status": running + " running", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.2", "service_name": "tomcat", "status": running + " running", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.3", "service_name": "nginx", "status": stop + " stop", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.5", "service_name": "tomcat", "status": stop + " stop", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.6", "service_name": "tomcat", "status": running + " prepare", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.2", "service_name": "nginx", "status": running + " running", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.2", "service_name": "tomcat", "status": running + " running", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.3", "service_name": "nginx", "status": stop + " stop", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.5", "service_name": "tomcat", "status": stop + " stop", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.6", "service_name": "tomcat", "status": running + " prepare", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.2", "service_name": "nginx", "status": running + " running", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.2", "service_name": "tomcat", "status": running + " running", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.3", "service_name": "nginx", "status": stop + " stop", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.5", "service_name": "tomcat", "status": stop + " stop", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.6", "service_name": "tomcat", "status": running + " prepare", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.1.5", "service_name": "tomcat", "status": stop + " stop", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
        {"ip": "10.2.2.2", "service_name": "nginx", "status": prepare + " prepare", "current_version": "1.10.2",
         "service_time": "19days", "last_version": "1.10.1"},
        {"ip": "10.2.1.6", "service_name": "tomcat", "status": running + " prepare", "current_version": "8.5.1",
         "service_time": "8days", "last_version": "8.5.2"},
    ]
    return service_data

# 服务器状态列表
@require_http_methods(["GET"])
def serverStatusList(request):
    navs = list(Nav.objects.all())
    return render(request,'server/server_status_list.html',{"navs":navs})


# 解析相应的匹配符号
def getF(key):
    res = ''
    FDATA = {
        "eq":"=",
        "neq":"!=",
        "lt":"<",
        "le":"<=",
        "gt":">",
        "ge":">=",
        "nu":"null",
        "nn":"is not null ",
        "in":"in ",
        "ni":"is not in "
    }
    res = FDATA[key]
    return "".join(res)


def getSearchData(source_data,field,op,s_data):
    res = []
    for data in source_data:
        for k,v in data.items():
            if k == field:
                if op == 'eq':
                    if v == s_data:
                        res.append(data)
                if op == 'ne':
                    if v != s_data:
                        res.append(data)
                if op == 'lt':
                    if v < s_data:
                        res.append(data)
                if op == 'le':
                    if v <= s_data:
                        res.append(data)
                if op == 'gt':
                    if v > s_data:
                        res.append(data)
                if op == 'ge':
                    if  v >= s_data:
                        res.append(data)
                if op == 'nu':
                    if not s_data:
                        res.append(data)
                if op == 'nn':
                    if s_data:
                        res.append(data)
                if op == 'in':
                    if s_data in v:
                        res.append(data)
                if op == 'ni':
                    if s_data not in v:
                        res.append(data)
    return res


# 返回服务状态json数据
@require_http_methods(["GET"])
def serverStatusListJson(request):
    # 客户端时间
    nd = request.GET.get('nd', None)
    if not nd:
        nd = time.time()
    # 每行显示的行数
    rows = int(request.GET.get('rows', None))
    if not rows:
        rows = 10
    # 分页
    page = int(request.GET.get('page', None))
    if not page:
        page = 1
    #
    sidx = request.GET.get('sidx', None)
    if not sidx:
        pass
    # 排序规则
    sord = request.GET.get('sord', None)
    if not sord:
        sord = "desc"
    # 过滤字段
    filters = request.GET.get('filters', '')
    # 搜索字段
    searchField = request.GET.get('searchField', '')
    # 搜索关键词
    searchString = request.GET.get('searchString', '')
    # 搜索操作
    searchOper = request.GET.get('searchOper', '')
    # 操作
    oper = request.GET.get('oper', None)
    if not oper:
        pass
    service_data = getServerStatusJson()
    total_rows = len(service_data)
    # 总页数向上取整
    total_page = total_rows/rows
    total_page = int(math.ceil(total_page))
    # 其实页码
    startrows = (page - 1) * rows
    # 终止页码
    lastrows = rows*page
    if lastrows > total_rows:
        lastrows = total_rows
    res = service_data[startrows:lastrows]
    # 是否搜索
    _search = request.GET.get('_search', None)
    if _search == 'true':
        filters = request.GET.get('filters',None)
        if filters:
            filters = json.loads(filters)
            rules = filters['rules']
            search_data = []
            for rule in rules:
                field = rules['field']
                op = rules['op']
                s_data = rules['data']
                search_data = getSearchData(service_data,field,op,s_data)
                search_data = [ data for data in search_data1 if data in search_data ]
            return HttpResponse(json.dumps(search_data))
    if page > total_page:
        return HttpResponse(json.dumps({'data':"亲,没有那么多数据!"}))
    else:
        return HttpResponse(json.dumps(res))


# 返回服务子栏目状态json数据
@require_http_methods(["GET"])
def serverStatusListSubJson(request):
    id = request.GET.get('id',None)
    service_data = getServerStatusJson()
    sub_data = service_data[int(id)]
    subService_data = [ sub_data for i in range(0,8)]
    return HttpResponse(json.dumps(subService_data))


# jenkins 服务管理页面
@require_http_methods(["GET"])
def Jenkinslist(request):
    navs = Nav.objects.all()
    return render(request,'server/jkList1.html',{"navs":navs})
    # return render(request,'server/lay.html',{"navs":navs})


# 是否有
def Has_value(value):
    res =['No','Yes']
    return res[value]


# 是否有
def get_Has_value(value):
    res ={'No':0,'Yes':1}
    return res[value]

# 获取分页数据
def pagn(data, limit, page):
    paginator = Paginator(data, limit)
    try:
        data = paginator.page(page)
    except PageNotAnInteger:
        data = paginator.page(1)
    except EmptyPage:
        data = paginator.page(paginator.num_pages)
    return data


# 获取数据
def getData(Obj,where,order_byField):
    res = []
    table_name = Obj._meta.db_table.encode()
    sql = "select * from `" + table_name + "` where "
    if where:
        where = eval(where)
        if where['selectpickerField'] == 'is_del' or where['selectpickerField'] == 'is_config' or where['selectpickerField'] == 'is_bin':
            where['selectpickerValue'] = get_Has_value(where['selectpickerValue'][0])
        if where['selectpickerField'] == 'is_del':
            sql += "`" + where['selectpickerField'] + "` in " + repr(tuple(str(where['selectpickerValue']))).replace(",)",")")
        if where['selectpickerField'] != 'is_del':
            sql += "`" + where['selectpickerField'] + "` in " + repr(tuple(where['selectpickerValue'])).replace(",)",")") + " and `is_del`=0 "
        if '-' in order_byField:
            sql += " order by `" + order_byField + "` desc;"
        else:
            sql += " order by `" + order_byField + "` asc;"
    else:
        sql = "select * from `" + table_name + "` where `is_del`=0;"
    try:
        print sql
        cursor = connection.cursor()
        cursor.execute(sql)
        res = cursor.fetchall()
    except Exception,e:
            print e
    return res



# jenkins json 列表 bootstrap-tables 格式
@require_http_methods(["GET"])
def JenkinslistbsJson(request):
    # 没页面显示行数
    rows = request.GET.get('rows',None)
    limit = request.GET.get('limit', None)
    offset = request.GET.get('offset','0')
    sort = request.GET.get('sortOrder','asc')
    order_by = request.GET.get("sort",'id')
    if sort == 'desc':
        order_by = '-' + order_by
    where = request.GET.get('where',None)
    res = dict()
    res['rows'] = []
    jk_datas = getData(WoJenkinsServices,where,order_by)
    res['total'] = len(jk_datas)
    if rows:
        jk_datas = pagn(jk_datas,rows,page)
    if limit:
        page = (int(offset) + 10)/int(limit)
        jk_datas = pagn(jk_datas, limit, page)
    if not rows and not limit:
        jk_datas = pagn(jk_datas, 10, page)
    for data in jk_datas:
        data1 = dict()
        data1['ctime'] = data[-3].strftime("%Y-%m-%d %H:%M:%S")
        data1['id'] = int(data[0])
        data1['service_name'] = data[1]
        data1['locate_service_name'] = data[2]
        data1['project_name'] = data[3]
        data1['service_app_name'] = data[4]
        data1['is_bin'] = Has_value(int(data[5]))
        data1['is_config'] = Has_value(int(data[6]))
        data1['sup_group'] = data[7]
        data1['suffix'] = data[8]
        data1['service_dir'] = data[9]
        data1['is_del'] = data[-1]
        data1['mtime'] = data[-2].strftime("%Y-%m-%d %H:%M:%S")
        res['rows'].append(data1)
    # bootstrap-table 返回格式
    res['count'] = res['total']
    res['status'] = 200
    res['msg'] = ''
    return HttpResponse(json.dumps(res))



# jenkins json 列表 dataTables 格式
@require_http_methods(["GET"])
def JenkinslistbJson(request):
    # 没页面显示行数
    rows = request.GET.get('rows',None)
    limit = request.GET.get('limit', None)
    page = request.GET.get('page',1)
    sort = request.GET.get('sortOrder','asc')
    order_by = request.GET.get("sort",'id')
    draw = request.GET.get("draw",None)
    if sort == 'desc':
        order_by = '-' + order_by
    where = request.GET.get('where',None)
    res = dict()
    res['data'] = []
    res['draw'] = draw
    res['recordsTotal'] = len(WoJenkinsServices.objects.all().values())
    jk_datas = getData(WoJenkinsServices,where,order_by)
    res['recordsFiltered'] = len(jk_datas)
    # 一次行放回所有数据,客户端分页
    for data in jk_datas:
        data1 = dict()
        data1['ctime'] = data[-3].strftime("%Y-%m-%d %H:%M:%S")
        data1['id'] = int(data[0])
        data1['service_name'] = data[1]
        data1['locate_service_name'] = data[2]
        data1['project_name'] = data[3]
        data1['service_app_name'] = data[4]
        data1['is_bin'] = Has_value(int(data[5]))
        data1['is_config'] = Has_value(int(data[6]))
        data1['sup_group'] = data[7]
        data1['suffix'] = data[8]
        data1['service_dir'] = data[9]
        data1['is_del'] = data[-1]
        data1['mtime'] = data[-2].strftime("%Y-%m-%d %H:%M:%S")
        res['data'].append(data1)
    # dataTable 返回格式
    res['error'] = ''
    return HttpResponse(json.dumps(res))



# jenkins json 列表 layui data 格式
@require_http_methods(["GET"])
def JenkinslistJson(request):
    # 没页面显示行数
    rows = request.GET.get('rows',None)
    limit = request.GET.get('limit', None)
    page = request.GET.get('page',1)
    sort = request.GET.get('sortOrder','asc')
    order_by = request.GET.get("sort",'id')
    if sort == 'desc':
        order_by = '-' + order_by
    where = request.GET.get('where',None)
    res = dict()
    res['rows'] = []
    jk_datas = getData(WoJenkinsServices,where,order_by)
    res['total'] = len(jk_datas)
    if rows:
        jk_datas = pagn(jk_datas,rows,page)
    if limit:
        jk_datas = pagn(jk_datas, limit, page)
    if not rows and not limit:
        jk_datas = pagn(jk_datas, 10, page)
    for data in jk_datas:
        data1 = dict()
        data1['ctime'] = data[-3].strftime("%Y-%m-%d %H:%M:%S")
        data1['id'] = int(data[0])
        data1['service_name'] = data[1]
        data1['locate_service_name'] = data[2]
        data1['project_name'] = data[3]
        data1['service_app_name'] = data[4]
        data1['is_bin'] = Has_value(int(data[5]))
        data1['is_config'] = Has_value(int(data[6]))
        data1['sup_group'] = data[7]
        data1['suffix'] = data[8]
        data1['service_dir'] = data[9]
        data1['is_del'] = data[-1]
        data1['mtime'] = data[-2].strftime("%Y-%m-%d %H:%M:%S")
        res['rows'].append(data1)
    # layui 返回格式
    res['count'] = res['total']
    res['status'] = 200
    res['msg'] = ''
    return HttpResponse(json.dumps(res))

# form 表单页面
@require_http_methods(["GET"])
def jenkinsAddForm(request):
    return render(request,'server/layer_add_form.html')


# form 表单详情页面
@require_http_methods(["GET"])
def jenkinsDetailForm(request):
    data = {}
    error = ''
    ID = request.GET.get('id',None)
    if id:
        jk_datas = WoJenkinsServices.objects.all().filter(id=ID).values()[0]
        w_data = jk_datas
        w_data['ctime'] = jk_datas['ctime'].strftime("%Y-%m-%d %H:%M:%S")
        w_data['id'] = int(jk_datas['id'])
        w_data['is_bin'] = Has_value(int(jk_datas['is_bin']))
        w_data['is_del'] = Has_value(int(jk_datas['is_del']))
        w_data['is_config'] = Has_value(int(jk_datas['is_config']))
        w_data['mtime'] = jk_datas['mtime'].strftime("%Y-%m-%d %H:%M:%S")

    else:
        error = '出错了!'
    return render(request,'server/layer_detail_form.html',{"error":error,'data':w_data,'o_data':json.dumps(w_data)})


# form 表单页面
@require_http_methods(["GET"])
def jenkinsEditForm(request):
    data = {}
    error = ''
    ID = request.GET.get('id',None)
    if id:
        jk_datas = WoJenkinsServices.objects.all().filter(id=ID).values()[0]
        w_data = jk_datas
        w_data['ctime'] = jk_datas['ctime'].strftime("%Y-%m-%d %H:%M:%S")
        w_data['id'] = int(jk_datas['id'])
        w_data['is_bin'] = Has_value(int(jk_datas['is_bin']))
        w_data['is_del'] = Has_value(int(jk_datas['is_del']))
        w_data['is_config'] = Has_value(int(jk_datas['is_config']))
        w_data['mtime'] = jk_datas['mtime'].strftime("%Y-%m-%d %H:%M:%S")
        del w_data['ctime']
        del w_data['mtime']
    else:
        error = '出错了!'
    return render(request,'server/layer_md_form.html',{"error":error,'data':w_data,'o_data':json.dumps(w_data)})


# 单个修改
@csrf_exempt
@require_http_methods(["POST"])
def JenkinslistSave(request):
    res = dict()
    f_data = request.POST.get('data',None)
    if f_data:
        f_data1 = json.dumps(f_data)
        f_data = json.loads(f_data)
        id = ''
        u_sql = 'update wo_jenkins_services set '
        for k,v in f_data.items():
            if k == 'id':
                id = str(v)
            elif k == 'is_del':
                pass
            elif k == 'is_bin':
                u_sql += k + "='" + str(get_Has_value(str(v))) + "',"
            elif k == 'is_config':
                u_sql += k + "='" + str(get_Has_value(str(v))) + "',"
            else:
                u_sql += k + "='" + str(v) + "',"
        u_sql += "mtime='" + getCurrentTime() + "',"
        u_sql = u_sql[:-1]
        u_sql += " where id='" + id + "';"
        try:
            cursor = connection.cursor()
            cursor.execute(u_sql)
            res['status'] = 200
            res['info'] = "修改成功!,即将跳转刷新到主页面"
        except Exception,e:
            print e
            res['status'] = 500
            res['info'] = str(e)
    else:
        res['status'] = 500
    return HttpResponse(json.dumps(res))


# 新增加
@csrf_exempt
@require_http_methods(["POST"])
def JenkinslistAdd(request):
    res = dict()
    f_data = request.POST.get('data',None)
    if f_data:
        f_data1 = json.dumps(f_data)
        f_data = json.loads(f_data)
        ctime = getCurrentTime()
        mtime = ctime
        i_sql = "insert into wo_jenkins_services(`service_name`,`service_app_name`,`service_dir`,`suffix`,`locate_service_name`,`project_name`,`is_bin`,`is_config`,`sup_group`,`ctime`,`mtime`) values ("
        i_sql += "'%s','%s','%s','%s','%s','%s','%s','%s','%s','%s','%s');"%(f_data['service_name'],f_data['service_app_name'],f_data['service_dir'],f_data['suffix'],f_data['locate_service_name'],f_data['project_name'],f_data['is_bin'],f_data['is_config'],f_data['sup_group'],ctime,mtime)
        try:
            cursor = connection.cursor()
            cursor.execute(i_sql)
            res['status'] = 200
            res['info'] = "修改成功!,即将跳转刷新到主页面"
        except Exception,e:
            print e
            res['status'] = 500
            res['info'] = str(e)
    else:
        res['status'] = 500
    return HttpResponse(json.dumps(res))


# 增加分组
@csrf_exempt
@require_http_methods(["GET"])
def JenkinsSupGroupAdd(request):
    return render(request,"server/jk_sup_group_add.html")


# 增加分组
@csrf_exempt
@require_http_methods(["POST"])
def JenkinsSupGroup_Add(request):
    res = dict()
    new_supervisor_group_name = request.POST.get("new_supervisor_group_name",None)
    if new_supervisor_group_name:
        try:
            rs = WoSupervisorGroup.objects.get_or_create(supervisor_group_name=new_supervisor_group_name)
            res['status'] = 200
            res['info'] = "添加新组成功"
        except Exception,e:
            res['status'] = 205
            res['info'] = str(e)
    else:
        res['status'] = 505
        res['info'] = "传参错误"
    return HttpResponse(json.dumps(res))


# checkSupervisorGroupName ajax 检查是否有存在的sup_group
@csrf_exempt
@require_http_methods(['GET'])
def checkSupervisorGroupName(request):
    res = dict()
    new_supervisor_group_name = request.GET.get('new_supervisor_group_name',None)
    if new_supervisor_group_name:
        wsn = WoSupervisorGroup.objects.filter(supervisor_group_name=new_supervisor_group_name).values()
        if len(wsn) == 0:
            res['code'] = 200
            res['data'] = "ok"
        else:
            res['code'] = 202
            res['data'] = "not ok!"
    else:
        res['code'] = 505
        res['data'] = "传参错误!"
    return HttpResponse(json.dumps(res))


@csrf_exempt
@require_http_methods(['GET','POST'])
def selectFiledValue(request):
    res = []
    selectField = request.POST.get("selectField",None)
    if selectField:
        wjs = WoJenkinsServices.objects.values_list(selectField,flat=True)
        # 去掉unicode
        for w in wjs:
            res.append(w)
    return HttpResponse(json.dumps(list(set(res))))


@csrf_exempt
@require_http_methods(['GET','POST'])
def supGroupList(request):
    res = []
    wsg = WoSupervisorGroup.objects.all().values()
    # 去掉unicode
    for w in wsg:
        nw = []
        for k,v in w.items():
            nw.append(v)
        res.append(nw)
    return HttpResponse(json.dumps(res))


@csrf_exempt
@require_http_methods(['POST'])
def JkListDelById(request):
    res = dict()
    ids = request.POST.get("data",None)
    if ids:
        sql = "update wo_jenkins_services set `is_del`='1' where id in ("
        for id in json.loads(ids):
            sql += str(id['id']) + ','
        sql = sql[:-1]
        sql += ");"
        try:
            cursor = connection.cursor()
            cursor.execute(sql)
            res['status'] = 200
            res['info'] = "删除成功!"
        except Exception,e:
            print e
            res['status'] = 500
            res['info'] = str(e)
    else:
        res['status'] = 500
    return HttpResponse(json.dumps(res))


@csrf_exempt
@require_http_methods(['POST'])
def jk_query(request):
    res = dict()
    return HttpResponse(res)