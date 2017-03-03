# coding:utf-8
from django.db import models
from django.contrib import admin
 
class Article(models.Model):
    title = models.CharField(u'标题', max_length=256)
    content = models.TextField(u'内容')
    pub_date = models.DateTimeField(u'发表时间', auto_now_add=True, editable = True)
    update_time = models.DateTimeField(u'更新时间',auto_now=True, null=True)

    def __unicode__(self):  # 在Python3中用 __str__ 代替 __unicode__
        return self.title
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title','pub_date','update_time',)
class Person(models.Model):
    name = models.CharField(max_length=30)
    age = models.IntegerField()
     
    def __unicode__(self):
    # 在Python3中使用 def __str__(self)
        return self.name