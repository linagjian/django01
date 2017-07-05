from django.conf.urls import url
from . import views

urlpatterns =[
    url(r'^cart/$',views.cart),
    url(r'^user_center_info/$',views.user_center_info),
    url(r'^user_info/$',views.user_info),
    url(r'^user_site/$',views.user_site),
    url(r'^user_order/$', views.user_order),
    url(r'^login/$', views.login),
    url(r'^register/$', views.register),
]