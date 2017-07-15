from django.db import models
from goods_info.models import GoodsInfo
from user_info.models import UserInfo
# Create your models here.
# Create your models here.
class OrderMain(models.Model):
    order_id=models.CharField(max_length=20,primary_key=True)#20170713000000uid
    user=models.ForeignKey(UserInfo)
    order_date=models.DateTimeField(auto_now_add=True)
    total=models.DecimalField(max_digits=8,decimal_places=2,default=0)
    state=models.IntegerField(default=0)

class OrderDetail(models.Model):
    order=models.ForeignKey(OrderMain)
    goods=models.ForeignKey(GoodsInfo)
    count=models.IntegerField()
    price=models.DecimalField(max_digits=5,decimal_places=2)
