#coding=utf-8
from django.shortcuts import render,redirect
from django.db import transaction
from datetime import datetime
from models import OrderMain,OrderDetail
from cartinfo.models import CartInfo
# Create your views here.
@transaction.atomic
def order(request):
    print '12222222'
    isok = True
    #创建事物
    sid = transaction.savepoint()
    try:
        uid = request.session.get('uid')
        now_str = datetime.now().strftime('%Y%m%d%H%M%S')
        main = OrderMain()
        main.order_id = now_str
        main.user_id = uid
        main.save()
        #2接收所有的购物车请求
        clist = request.POST.get('c_list').split(',')
        cart_list = CartInfo.objects.filter(id__in=clist)
        total = 0
        for cart in cart_list:
            if cart.count<=cart.goods.gkucun:
                #2
                detail = OrderDetail()
                detail.order = main
                detail.goods = cart.goods
                detail.count = cart.count
                detail.price = cart.goods.gprice
                detail.save()
                #3
                cart.goods.gkucun-=cart.count
                cart.goods.save()
                #4
                total += cart.count*cart.goods.gprice
                main.total = total
                main.save()
                #5
                cart.delete()
            else:
                isok=False
                transaction.savepoint_rollback(sid)
                break
        if isok==True:
            transaction.savepoint_commit(sid)
    except:
        transaction.savepoint_rollback(sid)
        isok=False
    if isok==True:
        return redirect('/user/user_order/')
    else:
        return redirect('/cart/')


