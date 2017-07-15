from django.shortcuts import render,redirect

class UrlMiddleware():

    def process_request(self,request):

        if request.path not in ['/user/user_info/','/user/user_order/','/user/user_site/','/user/login/','/user/login01/','/user/loginout/','/user/register/','/user/register01/']:

            request.session['Path'] = request.path



