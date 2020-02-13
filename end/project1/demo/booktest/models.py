from django.db import models

# Create your models here.
# 有模型类之后，模型类与数据库交互步骤：
# 1.注册模型 在setting.py 中的INSTALLED_APPS 添加应用名
# 2. 生成迁移文件 用于与数据库交互  python manage.py makemigrations
# 3. 执行迁移，会在对应的数据库中生成对应的表 python manage.py migrate
# 只要模型类发生更改，执行2,3步

# 模型类的设置
class Book(models.Model):
    title=models.CharField(max_length=20)
    price=models.FloatField(default=8)
    pub_date=models.DateField(default="1998-11-11")
    def __str__(self):
        return self.title
class Hero(models.Model):
    name=models.CharField(max_length=20)
    gender=models.CharField(max_length=6,choices=(('male','男'),('femle','女')),default='male')
    content=models.CharField(max_length=100)
    # book 指一对多的外键 on_delete代表删除主表数据时如何做
    book=models.ForeignKey(Book,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

# django orm 关联查询
# 多方Hero    一方Book
# 1. 多找一    多方对象.关系字段   exp：h1.book

# 2. 一找多    一方对象.小写多方类名_set.all()  exp：b1.hero_set.all()