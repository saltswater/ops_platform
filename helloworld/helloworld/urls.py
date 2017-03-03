"""helloworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from learn import views as learn_views
from zabbix import views as zabbix_views
from day_check import views as day_check_views
from upgrade import views as upgrade_views
from elk import views as elk_views

urlpatterns = [
    url(r'^$', learn_views.index, name='index'),
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^admin/', admin.site.urls),
    url(r'^zabbix/', include('zabbix.urls')),
    # url(r'^day_check/',day_check_views.day_check,name='day_check'),
    url(r'^upgrade/',upgrade_views.upgrade,name='upgrade'),
    # url(r'^elk/',elk_views.elk,name='elk'),
    
]
