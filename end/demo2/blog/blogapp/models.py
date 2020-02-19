from django.db import models

# Create your models here.

class Ads(models.Model):
    img=models.ImageField(upload_to='ads')
    desc=models.CharField(max_length=20,null=True,blank=True,verbose_name="图片描述")

class Category(models.Model):
    name=models.CharField(max_length=20,verbose_name="分类名")
class Tag(models.Model):
    name=models.CharField(max_length=20,verbose_name="标签名")
class Article(models.Model):
    title=models.CharField(max_length=50,verbose_name="标题")
    category=models.ForeignKey(Category,on_delete=models.CASCADE,verbose_name="分类")
    create_ime=models.DateTimeField(auto_now_add=True,verbose_name="创建时间")
    update_time=models.DateTimeField(auto_now=True,verbose_name="修改时间")
    author=models.CharField(max_length=20,verbose_name="作者")
    views=models.CharField(default=0,verbose_name="浏览量")
    body=models.TextField(verbose_name="正文")
    tags=models.ManyToManyField(Tag)
class Comment(models.Model):
    name=models.CharField(max_length=20,verbose_name="评论人")
    url=models.URLField(default="",verbose_name="个人主页")
    email=models.EmailField(default="",verbose_name="个人邮箱")
    create_name=models.DateTimeField(auto_now_add=True,verbose_name="评论时间")
    body=models.CharField(max_length="500",verbose_name="评论内容")
    article=models.ForeignKey(Article,on_delete=models.CASCADE,verbose_name="所属文章")