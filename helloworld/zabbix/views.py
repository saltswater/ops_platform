from django.shortcuts import render
from zabbix.host_info import *
from zabbix.auth_session import *
from django.http import HttpResponse


def index(request):
    h_info = Hostinfo().get_info()
    return render(request, 'zabbix/index.html', {'h_info': h_info})



