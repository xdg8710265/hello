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
from django.contrib.auth.hashers import make_password,check_password

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
#网站首页
def index(request):
    return render(request,'hello/index.html')
#注册页面显示
def register(request):
    res=""
    if request.method =="POST":
        user=request.POST.get("username")
        passwd=request.POST.get('pass')
        mail=request.POST.get("mail")
        user_list=models.cus.objects.filter(user=user)
        if user_list:
            res="用户已被注册"
            return render(request,'hello/register.html',{"res":res})
        else:
            res="%s用户名可以使用"%user_list
            cus=models.cus()
            cus.user=user
            #对密码进行加密存储
            cus.psw=passwd
            cus.mail=mail
            cus.save()
            return render(request,'hello/login.html',{"res":res})

    return render(request, 'hello/register.html')

#登录功能
def  login(request):
    res=''
    if request.method=='POST':
        user=request.POST.get("username")
        passwd=request.POST.get('pass')

        ret=models.cus.objects.filter(user=user,psw=passwd).first()
        #对密码进行解密处理
        #is_pass_wd=check_password(passwd,ret.psw)

        if ret:
            return HttpResponse("登录成功")
        else:
            return HttpResponse("用户名或密码错误")

    if request.method=="GET":
        return render(request,'hello/login.html')


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

#测试账户提交功能
def test_user(request):
    #请求页面
    return render(request,'hello/get_demo.html')

def result_user(request):
    #返回结果
    if request.method == 'GET':
        #获取提取数据
        r = request.GET.get('user',None) #当key_value不存在时不会报错
        res = ''
        try:
            if int(r) %2==0:
                res = "大吉大利！"
            else:
                res = "恭喜发财！"
        except:
            res = "请输入正确的账户"
        return HttpResponse("测试结果显示:%s"%res)
    else:
        render(request,'hell/get_demo.html')

#提交方式和数据库关联，操作数据库

def name(request):
    res = ''
    if request.method == 'GET':
        n = request.GET.get('user',None)
        res =  models.cus.objects.filter(user='%s' %n)
        try:
            res = res[0].mail
        except:
            res = '未查询到数据'
        return render(request,'hello/name.html',{'mail':res})
    else:
        return render(request,'hello/name.html',{'mail':res})






