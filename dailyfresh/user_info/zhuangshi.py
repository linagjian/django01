from django.shortcuts import render,redirect
def zhuangshi(func):
    def func1(request,*args,**kwargs):
        if request.session.has_key('uid'):
            return func(request,*args,**kwargs)
        else:
            return redirect('/user/login/')
    return func1