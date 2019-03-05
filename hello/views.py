from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse,Http404
import json
from . import models
from django.forms import Form
from django.http import JsonResponse
from django.core import serializers
from django.forms.models import model_to_dict

#获取json 数据格式
def get_json(request):
    data={}#声明一个变量
    a=models.cus.objects.all()
    #实现序列化操作
    data['data']=json.loads(serializers.serialize('json',a))
    return JsonResponse(data)
#获取字典数据的格式
def get_dict(request):
    json_list=[]
    a=models.cus.objects.all()
    for i in a:
        ls=model_to_dict(i)
        json_list.append(ls)
    return JsonResponse(json_list,safe=False)

#返回的中文编码问题
def json_data(request):
    '''values()获取的可迭代dict对象转list'''
    data={}
    ret = models.cus.objects.all().values()
    data['data']=list(ret)
    return JsonResponse(data,safe=False,json_dumps_params={'ensure_ascii':False})


#将values转换为list
def get_data(request):
    data={}
    c=models.cus.objects.all().values()
    data['values']=list(c)
    return JsonResponse(data,safe=False)
def index(request):
    return HttpResponse("welcome to my world!!!")
#注册页面显示
def register(request):
    return render(request,'hello/register.html')

def top(request):
    data={"name":"xudegui","city":'shangrao'}
    return render(request,'hello/top.html',data)

def tomxu(request):
    return HttpResponse("ubox is good!!! 努力加油!!!")

def demo(request):
    alldb = models.Test.objects.all()
    data={'name':"xudegui","list":['a','b','c'],'time':time.strftime("%Y-%m-%d %H:%M:%S"),"a":alldb}

    return render(request,'hello/demo.html',data)


def page(request,num):
    try:
        num = int(num)
        return render(request,'hello/demo.html')
    except:
        raise Http404

def home(request):
    content={"list":['a','b','c']}
    return render(request,'hello/home.html',content)

def home1(request,year,month,day):
    return HttpResponse("Today is %s-%s-%s "%(year,month,day))


def test(request):
    data={}
    data['name']="hello"
    data['test']='world'
    data['age']=18
    return render(request,"hello/test.html",data)


def ubox(request):
    data={}
    data['name']="ubox"
    data['city']="shenzhen"
    data['age']=2018
    return render(request,'hello/ubox.html',data)

def base(request):
    data={}
    data['time']=time.strftime("%Y-%m-%d %H:%M:%S")
    return render(request,'hello/base.html',data)

def page1(request):
    data={"name":"xudegui","city":"shangrao","time":time.strftime("%Y-%m-%d %H:%M:%S")}
    return render(request,'hello/page1.html',data)

def testdb(request):
    test1=models.Test.objects.create(name="xudegui222")
    test1.save()
    return HttpResponse("数据库信息添加成功")

def listdb(request):
    #向数据库添加数据，能否正常显示
    list1=models.List.objects.create(list="ubox")
    list1.save()
    return HttpResponse("列表信息添加成功")
#修改数据表的信息
def update_listdb(request):
    # list2=models.List.objects.get(list='xdg111')
    # list2.list="xdg"
    # list2.save()
    li=models.List.objects.filter(id=2).update(list='ubox22')

    return HttpResponse("修改成功！！！%s"%li)
#删除数据库信息
def dele_listdb(request):
    #进行数据删除的操作
    # list3=models.List.objects.filter(id=3)
    # list3.delete()
    models.List.objects.all().delete()
    return HttpResponse("删除成功！！！")
#查询数据表信息
def select_listdb(request):
    #查询第一条数据
    #m=models.List.objects.get(id=1).list
    #n=models.List.objects.all()
    e=models.List.objects.filter(id=2)

    return HttpResponse("THIS IS %s"%e)

#新增数据显示
def cus_add(request):
    a=models.cus.objects.create(user='徐生',psw="密码",mail='邮箱')
    a.save()
    return HttpResponse("数据添加成功")

#查询数据并显示出来
def cus_select(request):
    a=''
    b=''
    c=''
    ret=models.cus.objects.all()
    for i in ret:
        a += '用户名： '+i.user+'\n'
        b += '密码： '+i.psw+'\n'
        c += '邮箱： '+i.mail+'\n'
    return HttpResponse('''<p>用户名为：%s</p><p>密码为：%s</p><P>邮箱为：%s</p>'''%(a,b,c))

#筛选需要的数据
def cus_fil(request):
    r=""
    a=models.cus.objects.filter(user="xu01",psw="123")
    try:
        r=a[0].mail
    except:
        r="null"
    data={"mail":r}
    #return HttpResponse("查询结果为:%s"%r)
    return render(request,'hello/cusdata.html',data)

#可迭代的的字典序列
def sele_values(request):
    '''可迭代的字典序列'''
    r=""
    ret=models.cus.objects.all().values("mail").distinct()#进行去重操作
    #获取数据的数量
    conut=models.cus.objects.all().count()
    #判断表中是否有数据并打印
    is_ex=models.cus.objects.all().exists()
    for i in ret:
        r += str(i)
    return HttpResponse("需要的结果显示：%s,显示的条数为：%d,返回的结果显示：%s"%(r,conut,is_ex))

#获取第一条记录和最后一条记录
def first_end(request):
    '''获取需要的数据'''
    ret=models.cus.objects.all().order_by("-mail").first()
    a=ret.mail
    return HttpResponse("返回的结果：%s"%a)

