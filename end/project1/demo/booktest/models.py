from django.db import models

# Create your models here.
# 有模型类之后，模型类与数据库交互步骤：
# 1.注册模型 在setting.py 中的INSTALLED_APPS 添加应用名
# 2. 生成迁移文件 用于与数据库交互  python manage.py makemigrations
# 3. 执行迁移，会在对应的数据库中生成对应的表 python manage.py migrate
# 只要模型类发生更改，执行2,3步

# 模型类的设置
#  多找一，一找多
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
    # 如果在关系字段中使用 related_name="heros" 则一找多  一方对象.heros.all() == 一方对象.hero_set.all()
    book=models.ForeignKey(Book,on_delete=models.CASCADE,)
    def __str__(self):
        return self.name
#     自定义管理类模型
class UserManager(models.Manager):
    """
    自定义模型管理类  该模型不在具有objects对象
    """
    def deletePhone(self,tele):
        # django默认的objects 是Manager类型   *.objects.get()
        user=self.get(phone=tele)
        user.delete()
    def createUser(self,tele):
        # self.model 可以获取模型类构造函数
        user=self.model()
        user.phone=tele
        user.save()
class User(models.Model):
    phone=models.CharField(max_length=11,null=True,blank=True,verbose_name="手机号")
    # 自定义过管理字段之后不在有objects， 自定义了一个新的objects
    objects=UserManager()
    def __str__(self):
        return self.phone
    class Meta:
        db_table="用户类"
        ordering=["-phone"]
        # admin页面进入模型类显示名字
        verbose_name="用户模型类a"
        # admin页面在应用下方显示的模型名
        verbose_name_plural="用户模型类b"
#  一找一
class Account(models.Model):
    username=models.CharField(max_length=20,verbose_name="用户名")
    password=models.CharField(max_length=20,verbose_name="密码")
    regist_date=models.DateField(auto_now_add=True,verbose_name="注册日期")
class Concact(models.Model):
    telephone=models.CharField(max_length=11,verbose_name="手机号")
    email=models.EmailField(default="87411@qq.com")
    account=models.OneToOneField(Account,on_delete=models.CASCADE,related_name="acc")
#   多找多
class Article(models.Model):
    title=models.CharField(max_length=20,verbose_name="标题")
    sumary=models.TextField(verbose_name="正文")
class Tag(models.Model):
    name=models.CharField(max_length=10,verbose_name="标签名")
    articles=models.ManyToManyField(Article,verbose_name="tages")
# django orm 关联查询
# 多方Hero    一方Book  关系字段只能定义在多方
# 1. 多找一    多方对象.关系字段   exp：h1.book

# 2. 一找多    一方对象.多方对象类名小写_set.all()  exp：b1.hero_set.all()
##   如果一找多中的外键中写了related_name="heros"时，只可以使用 一方对象.heros.all() 它就等于 一方对象.多方对象类名小写_set.all()

# 3. 一对一   一方Account 实例a  一方Concact 实例c  关系字段可以定义在任意一方
##  a 找 c： a.concact
##  c 找 a： c.account
##  如果你在 OneToOneField 里写了 related_name="acc" 时
##  a 找 c： a.acc
##  c 找 a： c.account

# 4. 多找多  多方Article 实例a  多方Tag 实例t 关系字段定义在任意一方
#  如果关系字段在Tag 添加关系：t.articles.add(a) 移除关系：t.articles.remove(a)
# a找t  a.tag_set.all()
# t找a  a.articles.all()
# 如果在关系字段里的 ManyToManyField 写了 verbose_name="tages"
# a找t  a.tags.all()
# t找a  a.articles.all()