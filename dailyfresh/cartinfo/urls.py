from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.index),
    url(r'^add/$',views.add),
    url(r'^count/$',views.count),
    url(r'^change/$',views.change),
    url(r'^del/$',views.delete),
    url(r'^place_order/$', views.place_order),

]