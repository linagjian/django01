from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^user_site/$',views.user_site),
    url(r'^user_order/$', views.user_order),
    url(r'^login/$', views.login),
    url(r'^login01/$', views.login01),
    url(r'^loginout/$',views.loginout),
    url(r'^islogin/$',views.islogin),
    url(r'^register/$', views.register),
    url(r'^register01/$',views.register01),
    url(r'^register_name/$',views.register_name),
    url(r'^user_site01/$',views.user_site01),
    url(r'^user_info/$',views.user_info),

]