from django.contrib import admin
from learn.models import *
admin.site.register(Article, ArticleAdmin)
admin.site.register(Person)
