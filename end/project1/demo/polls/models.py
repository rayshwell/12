from django.db import models

# Create your models here.

class Article(models.Model):
    title=models.CharField(max_length=20,verbose_name="标题")

    def __str__(self):
        return self.title


class Ticket(models.Model):
    content = models.CharField(verbose_name="投票内容",max_length=20)
    count = models.FloatField(verbose_name="投票数量",default=6)
    contact=models.ForeignKey(Article,on_delete=models.CASCADE,related_name="articles")
    def __str__(self):
        return self.content