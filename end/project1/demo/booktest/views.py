from django.shortcuts import render
from django.template import loader
# Create your views here.
from django.http import HttpResponse
from .models import Book,Hero
def index(request):
    # # 1 获取模板
    # template=loader.get_template('index.html')
    # # 2 渲染模板数据
    books=Book.objects.all()
    # context={'books':books}
    # result=template.render(context)
    # # 3 将渲染结果使用HttpResponse返回
    # return HttpResponse(result)
    return render(request,'index.html',{'books':books})

def detail(request,bookid):
    # template=loader.get_template('detail.html')
    book=Book.objects.get(id=bookid)
    # context={"book":book}
    # result=template.render(context)
    # return HttpResponse(result)
    return render(request,'detail.html',{'book':book})

def about(request):
    return HttpResponse("这是关于页面")