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
        verbose_name_plural='ubox-银行卡'
    def __str__(self):
        return self.bank_name
class CardInfo(models.Model):
    '''卡信息'''
    card_id=models.CharField(max_length=30,verbose_name="卡号")
    card_name=models.CharField(max_length=10,verbose_name="卡名")
    info=models.ForeignKey(Bank,on_delete=models.CASCADE,verbose_name="选择银行")
    class Meta:
        verbose_name_plural='ubox-卡号信息'
    def __str__(self):
        return self.card_id

#一对一设计表
# class Card(models.Model):
#     '''银行卡 基本信息'''
#     card_id=models.CharField(max_length=30,verbose_name="卡号",default='')
#     card_user=models.CharField(max_length=10,verbose_name='姓名',default='')
#     add_time=models.DateField(auto_now=True,verbose_name='添加时间')
#     class Meta:
#         verbose_name_plural="银行卡账户"
#         verbose_name="银行卡账户_基本信息"
#     def __str__(self):
#         return self.card_id
# class CarDetail(models.Model):
#     '''银行卡详情信息'''
#     card =  models.OneToOneField(Card,on_delete=models.CASCADE,verbose_name='卡号')
#     tel =  models.CharField(max_length=30,verbose_name="电话",default='')
#     mail = models.CharField(max_length=30,verbose_name='邮箱',default='')
#     city = models.CharField(max_length=10,verbose_name='城市',default='')
#     address = models.CharField(max_length=30,verbose_name='详细地址',default='')
#     class Meta:
#         verbose_name_plural = '个人资料'
#         verbose_name = '账户_个人资料'
#     def __str__(self):
#         return self.card


#创建一个作者表
class Auther(models.Model):
    name=models.CharField(max_length=10,verbose_name="作者")
    mail=models.CharField(max_length=30,verbose_name="邮箱")
    city=models.CharField(max_length=30,verbose_name="城市")
    class Meta:
        verbose_name_plural='ubox--作者'
    def __str__(self):
        return self.name
#创建一个书名表
class Book(models.Model):
    book_name=models.CharField(max_length=30,verbose_name="书名")
    auther=models.ManyToManyField(Auther,verbose_name="作者")
    class Meta:
        verbose_name_plural='ubox--书籍详情'
    def __str__(self):
        return self.book_name