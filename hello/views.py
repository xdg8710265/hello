from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse,Http404

def index(request):
    return HttpResponse("welcome to my world!!!")

def tomxu(request):
    return HttpResponse("tom xu is good!!!")

def demo(request):
    data={'name':"xudegui","list":['a','b','c']}

    return render(request,'demo.html',data)

def page(request,num):
    try:
        num = int(num)
        return render(request,'demo.html')
    except:
        raise Http404

def home(request):
    return render(request,'home.html')

def home1(request,year,month):
    return HttpResponse("Today is %s-%s "%(year,month))


def test(request):
    data={}
    data['name']="hello"
    data['test']='world'
    data['age']=18
    return render(request,"test.html",data)


def ubox(request):
    data={}
    data['name']="ubox"
    data['city']="shenzhen"
    data['age']=2018
    return render(request,'ubox.html',data)

def base(request):
    data={}
    data['time']=time.strftime("%Y-%M-%d %H:%M:%S")
    return render(request,'base.html',data)

def page1(request):

    data={"name":"xudegui","city":"shangrao","time":time.strftime("%Y-%M-%d %H:%M:%S")}
    return render(request,'page1.html',data)