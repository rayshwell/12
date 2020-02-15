from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.

from .models import Article,Ticket

class TicketInline(admin.StackedInline):
    # book关联hero
    model = Ticket
    extra = 1
class ArticleAdmin(ModelAdmin):
        # 定义模型管理类
        # 通过该类修改后台页面
        # 更改后端显示列
        list_display = ('title',)
        # 符页显示2个
        list_per_page = 2
        # 过滤字段
        list_filter = ('title',)
        # 定义后端搜索字段
        search_fields = ('title',)
        inlines = [TicketInline]

class TicketAdmin(ModelAdmin):

    list_display = ('content','count','contact')


admin.site.register(Article,ArticleAdmin)
admin.site.register(Ticket,TicketAdmin )

