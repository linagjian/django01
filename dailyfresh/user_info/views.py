from django.shortcuts import render

# Create your views here.


def cart(request):
    return render(request,'user_info/cart.html')

def user_center_info(request):
    return render(request,'user_info/user_center_info.html')

def user_info(request):
    return render(request,'user_info/user_info.html')
def user_site(request):
    return render(request,'user_info/user_site.html')
def user_order(request):
    return render(request,'user_info/user_order.html')
def login(request):
    return render(request,'user_info/login.html')
def register(request):
    return render(request,'user_info/register.html')