#coding=utf-8
from django.db import models

# Create your models here.

class UserInfo(models.Model):
    uname = models.CharField(max_length=20)
    upwd = models.CharField(max_length=40)
    uemail = models.CharField(max_length=20)


class UserSite(models.Model):
    sname = models.CharField(max_length=20)
    ssite = models.CharField(max_length=200)
    stel = models.CharField(max_length=20)
    scode=models.CharField(max_length=20)
    suser = models.ForeignKey('UserInfo')
