#! /usr/bin/env python -i
# -*- coding: utf-8 -*-
#
#=========================================================
import os,sys
from fabric.api import *
import subprocess
import fabfile
import pdb
#=========================================================
class Upgrade():
    def upgrad(self):
        #打印提示语
        print "Now,the system upgrade has started......\nThe operation number are: 1-copy_file,2-rm_file,3-kill_pid,4-upload_file,5-startup_serv"
        #定义一个字典
        #num = {'1':'copy_file','2':'rm_file','3':'kill_pid','4':'upload_file','5':'startup_serv'}

        #创建循环，执行操作
        while True:
        #    pdb.set_trace()
        #    print args
        #用户选择性输入
            args = raw_input("1:copy_file,2:rm_file,3:kill_pid,4:upload_file,5:startup_serv\nPlease select a number:")
            if args == "1":
                p = subprocess.Popen("fab -f E:/fabfile.py copy_file")
                p.communicate()


            elif args == "2":
                p = subprocess.Popen("fab -f E:/fabfile.py rm_file")
                p.communicate()

            elif args == "3":
                p = subprocess.Popen("fab -f E:/fabfile.py kill_pid")
                p.communicate()

            elif args == "4":
                p = subprocess.Popen("fab -f E:/fabfile.py upload_file")
                p.communicate()

            elif args == "5":
                p = subprocess.Popen("fab -f E:/fabfile.py startup_serv")
                p.communicate()
                print "The system upgrade has already complete!"
                break
            else:
                print "Please input number from 1 to 4"
        

