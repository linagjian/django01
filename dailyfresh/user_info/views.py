#coding=utf-8
from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from . models import *
from goods_info.models import *
from hashlib import sha1
import datetime
from zhuangshi import *
from order_info.models import OrderMain,OrderDetail
from django.core.paginator import Paginator
# Create your views here.
def register(request):#呈现注册页面
    content={'top':'0'}
    return render(request,'user_info/register.html',content)
def register01(request):#用户注册
    dict = request.POST
    u = UserInfo()
    uname = dict.get('user_name')
    upwd = dict.get('user_pwd')
    uemail = dict.get('user_email')
    s1 = sha1()
    s1.update(upwd)
    upwd_sha1=s1.hexdigest()
    u = UserInfo()
    u.uname = uname
    u.upwd = upwd_sha1
    u.uemail = uemail
    u.save()
    return redirect('/user/login/')
def register_name(request):#判断用户注册的用户名是否是已经存在
    uname = request.GET.get('uname')
    result = UserInfo.objects.filter(uname=uname).count()
    print result
    return JsonResponse({'result':result})

def login(request):#呈现登陆页面
    uname = request.COOKIES.get('uname','')
    content = {'uname':uname,'top':'0'}
    return render(request,'user_info/login.html',content)

def login01(request):#用户登录验证
    dict = request.POST
    uname = dict.get('username')
    jz = dict.get('jz','0')
    list = UserInfo.objects.filter(uname=uname)
    if len(list)==0:
        #用户名错误
        content={'name_error':'1','top':'0'}
        return render(request, 'user_info/login.html',content)
    else:
        s1 = sha1()
        s1.update(dict.get('pwd'))
        upwd_sha1 = s1.hexdigest()
        if list[0].upwd == upwd_sha1:#用户已经通过验证。
            request.session['uid'] = list[0].id#记录用户的id
            request.session['uname'] = list[0].uname
            print request.session.get('Path')
            zhuanxiang = request.session.get('Path')
            if zhuanxiang == None:
                response = redirect('/goods/')
            else:
                response = redirect(request.session.get('Path'))
            if jz == '1':#如果用户点击记住用户名，则建立cookie
                response.set_cookie('uname',uname,expires=datetime.datetime.now() + datetime.timedelta(days = 7))
            else:#如果不点击记住用户名那就将cookie删除
                response.set_cookie('uname','',max_age=-1)
            return response
        else:#密码错误无法登陆
            content = {'pwd_error': '1'}
            return render(request, 'user_info/login.html',content)
def loginout(request):
    request.session.flush()
    return redirect('/user/login/')
def islogin(request):
    result = 0
    if request.session.get('uid'):
        result = 1
        print result
    return JsonResponse({'isadd':result})


@zhuangshi
def user_site(request):#用户收货地址界面
    uname = request.COOKIES['uname']
    pid = UserInfo.objects.filter(uname=uname)
    suser = pid[0].id
    s = UserSite.objects.filter(suser = suser)
    sname = s[0].sname
    ssite = s[0].ssite
    scode = s[0].scode
    stel = s[0].stel
    content = {'title': '收货信息','sname': sname, 'ssite': ssite, 'scode': scode, 'stel': stel,'left':'1'}

    return render(request, 'user_info/user_site.html', content)
def user_site01(request):#用户重新建立收货地址功能
    uname = request.COOKIES['uname']
    pid = request.session.get('uid')
    suser = pid
    dict = request.POST
    sname = dict.get('sname')
    ssite = dict.get('ssite')
    scode = dict.get('scode')
    stel = dict.get('stel')
    s = UserSite()
    s.sname = sname
    s.ssite = ssite
    s.scode = scode
    s.stel = stel
    s.suser_id = suser
    s.save()
    content={'sname':sname,'ssite':ssite,'scode':scode,'stel':stel,'left':'1'}

    return render(request, 'user_info/user_site.html',content)
@zhuangshi
def user_info(request):#用户中心界面
    uname = request.COOKIES['uname']
    suser = request.session.get('uid')
    s = UserSite.objects.filter(suser=suser)
    stel=s[0].stel
    ssite=s[0].ssite
    # user = UserInfo.objects.get(pk=request.session['uid'])
    # # 查询最近浏览60,30,29,
    # gids = request.COOKIES.get('goods_ids', '').split(',')
    # #gids.pop()
    # print gids
    # glist = []
    # for gid in gids:
    #     glist.append(GoodsInfo.objects.get(id=gid))
    Str = request.COOKIES.get('goods_ids','')
    print Str
    list =[]
    if Str == '':
        list.append('1')
        print list
    else:
        Str1 = Str.split(',')
        for item in Str1:
            good = GoodsInfo.objects.get(id = int(item))
            list.append(good)


    content = {'title': '个人中心','uname':uname,'stel':stel,'ssite':ssite,'left':'1','list':list}
    return render(request,'user_info/user_info.html',content)
@zhuangshi
def user_order(request):
    pindex = int(request.GET.get('pindex','1'))
    uid = request.session.get('uid')
    order_list = OrderMain.objects.filter(user_id=uid)
    print order_list
    print pindex
    paginator=Paginator(order_list,1)
    order_page = paginator.page(pindex)
    page_list=[]
    if paginator.num_pages<5:
        page_list=paginator.page_range
    elif pindex<=2:
        page_list = range(1,6)
    elif pindex>=paginator.num_pages-1:
        page_list=range(paginator.num_pages-4,paginator.num_pages+1)
    else:
        page_list=range(pindex-2,pindex+3)
    content = {'title': '全部订单','left':'1','order_page':order_page,'page_list':page_list}
    return render(request,'user_info/user_order.html',content)



