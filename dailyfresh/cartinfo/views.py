#coding=utf-8
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from user_info.zhuangshi import *
from django.db.models import Sum
from models import *
from user_info.models import UserSite
# Create your views here.

def add(request):
    try:
        gid = int(request.GET.get('gid'))
        uid = request.session.get('uid')
        count = int(request.GET.get('count','1'))
        print '%d,%d,%d'%(gid,uid,count)
        print count
        carts = CartInfo.objects.filter(user_id=uid,goods_id=gid)
        print carts
        if len(carts)==1:
            cart=carts[0]
            cart.count+=count
            cart.save()
            print '111111111111'
        else:
            cart = CartInfo()
            cart.user_id=uid
            cart.goods_id=gid
            cart.count=count
            cart.save()
            print '222222222222'
        return JsonResponse({'add':1})
    except:
        print '333333cart333333'
        return JsonResponse({'add':0})

def count(request):
    cart_count = CartInfo.objects.filter(user_id = request.session.get('uid')).aggregate(Sum('count')).get('count__sum')
    return JsonResponse({'cart_count':cart_count})

@zhuangshi
def index(request):
    uid = request.session.get('uid')
    cart = CartInfo.objects.filter(user_id = uid)
    content={'title':'我的购物车','cart':cart}
    return render(request,'cartinfo/cart.html',content)

def delete(request):
    id = request.GET.get('id')
    cart = CartInfo.objects.get(pk=id)
    cart.delete()
    return JsonResponse({'ok':1})

def change(request):
    id = request.GET.get('id')
    count = request.GET.get('count')
    cart = CartInfo.objects.get(pk=id)
    cart.count=count
    cart.save()
    return JsonResponse({'ok':1})

def place_order(request):
    dict = request.POST
    id_list = dict.getlist('cart_id')
    c_list = ','.join(id_list)
    clist = CartInfo.objects.filter(id__in=id_list)
    uid = request.session.get('uid')
    address = UserSite.objects.filter(suser_id=uid)
    content = {'title': '提交订单','left':'0','clist':clist,'address':address[0],'c_list':c_list}
    return render(request, 'cartinfo/place_order.html',content)

