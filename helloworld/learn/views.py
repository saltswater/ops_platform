#coding:utf-8

from django.shortcuts import render
from django.http import HttpResponse
# 引入我们创建的表单类
from .forms import AddForm
# Create your views here.
def index(request):
    return render(request, 'index.html')
def test(request):
    return render(request, 'test.html')


def cal(request):
    if request.method == 'POST':  # 当提交表单时

        form = AddForm(request.POST)  # form 包含提交的数据

        if form.is_valid():  # 如果提交的数据合法
            a = form.cleaned_data['a']
            b = form.cleaned_data['b']
            return HttpResponse(str(int(a) + int(b)))

    else:  # 当正常访问时
        form = AddForm()
    return render(request, 'cal.html', {'form': form})


