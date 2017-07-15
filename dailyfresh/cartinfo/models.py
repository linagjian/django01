from django.db import models
from goods_info.models import GoodsInfo
from user_info.models import UserInfo
# Create your models here.

class CartInfo(models.Model):
    user = models.ForeignKey(UserInfo)
    goods = models.ForeignKey(GoodsInfo)
    count = models.IntegerField()
