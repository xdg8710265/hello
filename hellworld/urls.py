"""hellworld URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
# from django.urls import path
#
# urlpatterns = [
#     path('admin/', admin.site.urls),
# ]

from django.conf.urls import url
from hello import views
from django.urls import re_path,path

urlpatterns = [

    url(r'^$', views.index),
    url(r'^index$',views.index),
    url(r'^tomxu', views.tomxu),
    url(r'^demo$',views.demo,name='demo_page'),
    url(r'^demo/page=\d+$',views.demo),
    path("home", views.home,name='home_page'),
    url(r'^date/(?P<year>[0-9]{4})/(?P<month>[0-9]{1,2}).html$',views.home1),
    url(r'^test$',views.test),
    url(r'^ubox$',views.ubox,name='ubox_page'),
    url(r'^base$',views.base),
    url(r'page1/$',views.page1),
    url(r'mpage',views.mpage),

]