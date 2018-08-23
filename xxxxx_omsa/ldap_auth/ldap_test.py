#!/usr/bin/env python
# -*- coding:utf8 -*-
# @Time    : 2018/2/13 12:13
# @Author  : Mat
# @Email   : v_ygshi@wesure.cn
# @File    : ldap_test.py
# @Software: PyCharm

'''
实现LDAP用户登录验证，首先获取用户的dn，然后再验证用户名和密码
'''

import os
import sys,json
import ldap


def login_ldap(username, password):
    try:
        # Server = "ldap://wesure.cn:389"
        # baseDN = "cn=omsa_ldap,ou=Service_Account,dc=wesure,dc=cn"
        # # baseDN = "dc=wesure,dc=cn"
        searchScope = ldap.SCOPE_SUBTREE
        # # 设置过滤属性，这里只显示cn=test的信息
        searchFilter = "sAMAccountName=" + username
        # # 为用户名加上域名
        # username = 'domainname\\' + username
        #
        # # None表示搜索所有属性，['cn']表示只搜索cn属性
        retrieveAttributes = None
        #
        # conn = ldap.initialize(Server)
        # # 非常重要
        # conn.protocol_version = ldap.VERSION3
        # conn.set_option(ldap.OPT_REFERRALS, 0)
        # # 这里用户名是域账号的全名例如domain/name
        # print conn.simple_bind_s(username, password)
        # # print 'ldap connect successfully'
        Server = "10.95.10.122"
        baseDN = "dc=wesure,dc=cn"
        # baseDN = "ou=运营平台组,OU=技术部,OU=微民保险,dc=wesure,dc=cn"
        conn = ldap.open(Server)
        # you should  set this to ldap.VERSION2 if you're using a v2 directory
        conn.protocol_version = ldap.VERSION3
        # Pass in a valid username and password to get
        # privileged directory access.
        # If you leave them as empty strings or pass an invalid value
        # you will still bind to the server but with limited privileges.
        # Any errors will throw an ldap.LDAPError exception
        # or related exception so you can ignore the result
        conn.simple_bind_s(username, password)
        # 调用search方法返回结果id
        ldap_result_id = conn.search(baseDN, searchScope, searchFilter, retrieveAttributes)
        result_set = []
        # print ldap_result_id
        result_type, result_data = conn.result(ldap_result_id, 0)
        result_set = result_data
        print result_data
        sys.exit(1)
        if result_type == ldap.RES_SEARCH_ENTRY:
            for r_key,r_value in result_data[0][1].items():
                print r_key," : ",r_value[0]
        # print result_data[0][1]['objectGUID']
        Name, Attrs = result_set[0]
        if hasattr(Attrs, 'has_key') and Attrs.has_key('name'):
            distinguishedName = Attrs['name'][0]
            # distinguishedName = Attrs['displayName'][0]
            # distinguishedName = Attrs['sAMAccountName'][0]
            # distinguishedName = Attrs['distinguishedName'][0]

            print "Login Info for user : %s" % distinguishedName
            return distinguishedName
        else:
            print("in error")
            return None
    except ldap.LDAPError, e:
        print("out error")
        print e
        return None


if __name__ == "__main__":
    login_ldap(username, password)