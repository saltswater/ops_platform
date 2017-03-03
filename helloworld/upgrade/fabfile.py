# -*- coding: utf-8 -*-
# 文件名要保存为 fabfile.py
#模块导入
from __future__ import unicode_literals
from fabric.api import *
import os,sys
import time
 
# 登录用户和主机名：
#env.user = 'root'
# 如果没有设置，在需要登录的时候，fabric 会提示输入
#env.password = 'hyxxZyw@200.com'
# 如果有多个主机，fabric会自动依次部署
#env.hosts = ['root@172.16.1.201','root@172.16.1.202','root@172.16.1.203']
env.hosts = ['root@172.16.12.201']
#env.hosts = ['root@172.16.12.249']
#env.password = '6789@jkl'
env.password = '123'
##========================================================================
#创建各个功能函数
#=========================================================================
#创建备份函数
def copy_file():
    with cd('/tas/tas/webapps'):
        run('cp -rf thims.war /backup/thims.`date +%Y%m%d`.war')
    if os.path.exists('/backup/thims.`date +%Y%m%d`war'):
        message = "ok"
    else :
        message =  "sorry"
    return  message
#创建缓存删除函数
def rm_file():
    try:
        with cd('/tas/tas/work/'):
            run('rm -rf jetty-0.0.0.0-80-thims.war-_thims-any-')
        with cd('/tas/tas/webapps/'):
            run('rm -rf thims.war')
    except :
        print ('The file isnot exist!')
#创建进程停止函数
def kill_pid():
    run('/tas/tas/bin/StopTAS.sh')
    time.sleep(30)
    try:
        run('ps -ef|egrep /tas/|grep -v  grep')
    except:
        print('The process has already stoped!')
    else:
        print('The process is running,please wait a moment or retry to stop it!')
#创建发布包上传函数
def upload_file():
    try:
        put('E:/upload/thims.war','/tas/tas/webapps')
    except:
        print('The remote server is unreachable!')
    if os.path.exists('/tas/tas/webapps/thims.war'):
        print "The file upload successfully!"
#创建服务启动函数
def startup_serv():
    run(' /tas/tas/bin/StartTAS.sh')
#    run('/tmp/starup.sh')
   # time.sleep(10)
    # try:
        # run('ps -ef|egrep /tas/|grep -v grep')
        
    # except:
        # print('The service  isnot running!')
    # else:
        # print "Service has already started!"