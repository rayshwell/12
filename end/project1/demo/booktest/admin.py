from django.contrib import admin
from django.contrib.admin import ModelAdmin

# Register your models here.
# 后台管理操作
# 注册自己需要管理的模型 Book Hero

from .models import Book,Hero,User
class HeroInline(admin.StackedInline):
    # book关联hero
    model = Hero
    extra = 1
class BookAdmin(ModelAdmin):
        # 定义模型管理类
        # 通过该类修改后台页面
        # 更改后端显示列
        list_display = ('title','price','pub_date')
        # 符页显示2个
        list_per_page = 2
        # 过滤字段
        list_filter = ('title','price')
        # 定义后端搜索字段
        search_fields = ('title',)
        inlines = [HeroInline]

class HeroAdmin(ModelAdmin):

    list_display = ('name','gender','content','book')


admin.site.register(Book,BookAdmin)
admin.site.register(Hero,HeroAdmin )
admin.site.register(User )