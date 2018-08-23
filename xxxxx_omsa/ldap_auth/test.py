#!/usr/bin/env python
# -*- coding:utf8 -*-
# @Time    : 2018/2/13 16:52
# @Author  : Mat
# @Email   : v_ygshi@wesure.cn
# @File    : test.py
# @Software: PyCharm
import ldap
try:
    Server = "wesure.cn"
    baseDN = "dc=wesure,dc=cn"
    l = ldap.open(Server)
    # you should  set this to ldap.VERSION2 if you're using a v2 directory
    l.protocol_version = ldap.VERSION3
    # Pass in a valid username and password to get
    # privileged directory access.
    # If you leave them as empty strings or pass an invalid value
    # you will still bind to the server but with limited privileges.
    username = "omsa_sldaps"
    password = "8*dfH@2A!s"
    # Any errors will throw an ldap.LDAPError exception
    # or related exception so you can ignore the result
    l.simple_bind(username, password)
except ldap.LDAPError, e:
    print e
# handle error however you like