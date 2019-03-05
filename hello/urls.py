#!/usr/bin/python
# -*- coding:utf-8 -*-
# name:徐德贵
# 2018/11/29
from django.conf.urls import url
from . import views

urlpatterns =[
   url(r'^$', views.index),
   url(r'^index',views.tomxu),
   url(r'demo',views.demo,name='demo_page'),
   url(r'^home/$',views.home,name='home_page'),
   url(r'^home/page=\d+$',views.home),
   url(r'ubox',views.ubox,name='ubox_page'),
   url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2})/(?P<day>[0-9]{1,2}).html$',views.home1),
   url(r'^register$',views.register),
   url(r'^top$',views.top),
   url(r'listdb',views.listdb),
   url(r'update',views.update_listdb),
   url(r'delete',views.dele_listdb),
   url(r'select',views.select_listdb),
   url(r'add_cus',views.cus_add),
   url(r'sel_cus',views.cus_select),
   url(r'fil_cus',views.cus_fil),
   url(r'sel_val',views.sele_values),
   url('fend',views.first_end),
   url("get_json",views.get_json),
   url("get_dict",views.get_dict),
   url('get_data',views.get_data),
   url(r'^json_data$',views.json_data),
]