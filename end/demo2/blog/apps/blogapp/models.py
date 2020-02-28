from django.db import models
# 导入副文本
from DjangoUeditor.models import UEditorField
# Create your models here.

class Ads(models.Model):
    # 使用图片字段需要使用pillow模块
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20,null=True,blank=True,verbose_name="图片描述")
    def __str__(self):
        return self.desc
class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name="分类名")
    def __str__(self):
        return self.name
class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name="标签名")
    def __str__(self):
        return self.name
class Article(models.Model):
    title=models.CharField(max_length=50,verbose_name="标题")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    create_ime=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    author=models.CharField(max_length=20,verbose_name="作者")
    views=models.PositiveIntegerField(default=0,verbose_name="浏览量")
    # 使用百度Ueditor富文本类型
    body=UEditorField(imagePath='imgs/',width='100%')
    tags=models.ManyToManyField(Tag)
    def __str__(self):
        return self.title
class Comment(models.Model):
    name=models.CharField(max_length=20,verbose_name="评论人")
    url=models.URLField(default="http://127.0.0.1:8000",verbose_name="个人主页")
    email=models.EmailField(default="87411@qq.com",verbose_name="个人邮箱")
    create_name=models.DateTimeField(auto_now_add=True,verbose_name="评论时间")
    body=models.CharField(max_length=100,verbose_name="评论内容")
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="所属文章")
    def __str__(self):
        return self.name