from django.shortcuts import render
from django.http import HttpResponse
from upgrade import *
# Create your views here.
def upgrade(request):
    ugrade = Upgrade()
    ugrade = ugrade.upgrade()
    return render(request, 'upgrade/index.html', {'upgrade': ugrade})