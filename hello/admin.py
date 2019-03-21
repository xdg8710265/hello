from django.contrib import admin
from hello import models

# Register your models here.
# class TestAdmin(admin.ModelAdmin):
#     list_display = ("name")

# class UserAdmin(admin.ModelAdmin):
#     list_display = ("username","headImg")


# 把数据库加到后台
# admin.site.register(Test,TestAdmin)
# admin.site.register(User,UserAdmin)


#将数据库字段全部展示出来
class ControCus(admin.ModelAdmin):
    #显示字段属性
    list_display=('user','psw','mail')
    #添加搜索
    search_fields = ("user",)
#博客表展示在后台
class ControArticle(admin.ModelAdmin):
    #自定义列表栏目
    list_display=('title','body','auth','create_time','up_time')
    #增加搜索框按钮
    search_fields = ("title",'body',)
    #按字段降序排列
    ordering = ('create_time',)
    #显示每页条数10条
    list_per_page = 10
    #设置可编辑字段
    list_editable = ('auth',)#title是默认的link链接字段，不能添加到list_editable 否则会报错
    #设置可以点击链接字段
    list_display_links = ('title','body',)
    #设置过滤器
    list_filter = ('auth','title',)
    #按时间分层
    date_hierarchy = 'create_time'

class ControBank(admin.ModelAdmin):
    list_display = ('bank_name','city',"point")


class ControCardInfo(admin.ModelAdmin):
    list_display=("card_id",'card_name','info')

    
#将数据库加载到后台
admin.site.register(models.Bank,ControBank)
admin.site.register(models.CardInfo,ControCardInfo)
admin.site.register(models.cus,ControCus)
admin.site.register(models.List)
admin.site.register(models.Article,ControArticle)