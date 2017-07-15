#coding=utf-8
from django.shortcuts import render
from models import TypeInfo,GoodsInfo
from django.core.paginator import Paginator
# Create your views here.
def index(request):
    tlist = TypeInfo.objects.filter()
    glist=[]
    for t in tlist:
        nlist = t.goodsinfo_set.order_by('-id')[0:4]
        clist = t.goodsinfo_set.order_by('-gclick')[0:4]
        glist.append({'t':t,'nlist':nlist,'clist':clist})
    content = {'title': '首页', 'left': '0','glist':glist}
    return render(request,'goods_info/index.html',content)

def list(request,id,t,pIndex):
    t1 = TypeInfo.objects.get(pk=id)
    new_list = t1.goodsinfo_set.order_by('-id')[0:2]
    glist = t1.goodsinfo_set.order_by(t)
    p = Paginator(glist,10)


    if pIndex == '':
        pIndex = (p.num_pages+1)//2
        print pIndex
    elif int(pIndex) < 1:
        pIndex = 1
        print pIndex
    elif 1<=int(pIndex)<= p.num_pages:
        pIndex = int(pIndex)
        print pIndex
    else:
        pIndex = p.num_pages
        print pIndex
    list = p.page(pIndex)
    if p.num_pages <= 5:
        plist = p.page_range
    else:
        if pIndex <= 3:
            plist = p.page_range[0:5]
            print plist
        elif 3 < pIndex < p.num_pages:
            plist = p.page_range[pIndex - 3:pIndex + 2]
            print plist
        else:
            print pIndex
            plist = p.page_range[p.num_pages - 5:]
            print plist
    content = {'title': '商品列表','t1':t1,'new':new_list,'list':list,'plist':plist,'t':t}
    return render(request,'goods_info/list.html',content)

def detail(request,pk):
    goods = GoodsInfo.objects.get(id = int(pk))
    type = goods.gtype
    new_list = goods.gtype.goodsinfo_set.order_by('-id')[0:2]
    goods.gclick += 1
    goods.save()
    content = {'title': '商品详情','goods':goods,'new':new_list}

    goods_ids = request.COOKIES.get('goods_ids', '')
    goods_id = '%d' % goods.id
    print '1111111111'
    print goods_ids
    if goods_ids != '':
        goods_ids1 = goods_ids.split(',')
        if goods_ids1.count(goods_id) >= 1:
            goods_ids1.remove(goods_id)
        goods_ids1.insert(0, goods_id)
        if len(goods_ids1) >= 6:
            del goods_ids1[5]
        goods_ids = ','.join(goods_ids1)
    else:
        goods_ids = goods_id
    response = render(request, 'goods_info/detail.html',content)
    response.set_cookie('goods_ids', goods_ids)
    print goods_ids
    return response



