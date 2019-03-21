from django.db import models

# Create your models here.
class Test(models.Model):
    name=models.CharField(max_length=100)
    def __str__(self):
        return self.name


#创建一个用户表
class User(models.Model):
    username=models.CharField(max_length=30)
    headImg=models.FileField(upload_to="./upload/")
    def __str__(self):
        return self.username
#创建一个分类表
class List(models.Model):
    list=models.CharField(max_length=100)
    def __str__(self):
        return self.list

#创建一个person 表
class Person(models.Model):
    person=models.CharField(max_length=200)
    age=models.IntegerField()
    def __str__(self):
        return self.person
#创建一个用户表
class cus(models.Model):
    user=models.CharField(max_length=50,verbose_name='用户名')
    psw=models.CharField(max_length=255,verbose_name='密码')
    mail=models.CharField(max_length=50,verbose_name='邮箱')

    def __str__(self):
        return self.user

    class Meta:
        verbose_name_plural="访客用户"

class Article(models.Model):
    '''文章'''
    title = models.CharField(max_length=30,verbose_name="标题")  # 标题
    body = models.TextField(verbose_name='正文')  # 正文
    auth = models.CharField(max_length=10,verbose_name='作者')  # 作者
    create_time=models.DateTimeField(auto_now_add=True,verbose_name='创建时间')
    up_time=models.DateTimeField(auto_now=True,verbose_name='更新时间')
    def __str__(self):
        return self.title
    #将表名修改为自定义的表名
    class Meta:
        verbose_name_plural = '文章列表'

#创建一个银行卡的表
class Bank(models.Model):
    '''银行信息'''
    bank_name=models.CharField(max_length=50,verbose_name="银行名称")
    city=models.CharField(max_length=30,verbose_name="城市")
    point=models.CharField(max_length=60,verbose_name="网点")
    class Meta:
        verbose_name_plural='银行卡'
    def __str__(self):
        return self.bank_name
class CardInfo(models.Model):
    '''卡信息'''
    card_id=models.CharField(max_length=30,verbose_name="卡号")
    card_name=models.CharField(max_length=10,verbose_name="卡名")
    info=models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name="选择银行")
    class Meta:
        verbose_name_plural='卡号信息'
    def __str__(self):
        return self.card_id

class
