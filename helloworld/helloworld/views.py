# coding=utf-8

'''
Created on 2017年2月6日
@author: Administrator
'''
from django.http import HttpResponse


def hello(request):
    return HttpResponse("hello world!")
