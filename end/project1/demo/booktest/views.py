from django.shortcuts import render,redirect,reverse
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
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
    return render(request,'booktest/index.html',{'books':books})

def detail(request,bookid):
    # template=loader.get_template('detail.html')
    book=Book.objects.get(id=bookid)
    # context={"book":book}
    # result=template.render(context)
    # return HttpResponse(result)
    return render(request,'booktest/detail.html',{'book':book})

def about(request):
    return HttpResponse("这是关于页面")
def deletebook(request,bookid):
    book = Book.objects.get(id=bookid)
    book.delete()
    # 删除后返回原来的页面 重定向
    # return HttpResponseRedirect(redirect_to='/')
    # return  redirect(to='/')
    # 解除硬编码
    url=reverse("booktest:index")
    return redirect(to=url)
def deletehero(request,heroid):
    hero= Hero.objects.get(id=heroid)
    bookid=hero.book.id
    hero.delete()
    # 删除后返回原来的页面 重定向
    # return HttpResponseRedirect(redirect_to='/')
    # return  redirect(to='/')
    # 解除硬编码
    url=reverse("booktest:detail",args=(bookid,))
    return redirect(to=url)

def addhero(request,bookid):
    # 视图函数可以同时存在get和post 默认是get
    if request.method=="GET":
        return render(request,'booktest/addhero.html')
    elif request.method=="POST":
        hero = Hero()
        hero.name=request.POST.get("heroname")
        hero.content=request.POST.get("herocontent")
        hero.sex=request.POST.get("sex")
        hero.book=Book.objects.get(id=bookid)
        hero.save()
        url=reverse("booktest:detail",args=(bookid,))
        return redirect(to=url)

def edithero(request,heroid):
    hero= Hero.objects.get(id=heroid)
    if request.method=="GET":
        return render(request,'booktest/edithero.html',{"hero":hero})
    elif request.method =="POST":
        hero.name = request.POST.get("heroname")
        hero.content = request.POST.get("herocontent")
        hero.sex = request.POST.get("sex")
        print(hero.sex)
        hero.save()
        url = reverse("booktest:detail", args=(hero.book.id,))
        return redirect(to=url)

def editbook(request,bookid):
    # 创建查询集 是惰性执行的
    book = Book.objects.get(id=bookid)
    if request.method=="GET":
        return render(request,'booktest/editbook.html',{"book":book})

    elif request.method =="POST":
        book.title = request.POST.get("booktitle")
        book.price = request.POST.get("bookprice")
        book.pub_date = request.POST.get("pub_date")

        book.save()
        url = reverse("booktest:index")
        return redirect(to=url)

def addbook(request):
    # 视图函数可以同时存在get和post 默认是get
    if request.method=="GET":
        return render(request,'booktest/addbook.html')
    elif request.method=="POST":
        book = Book()
        book.title=request.POST.get("booktitle")
        book.price=request.POST.get("bookprice")
        book.pub_date=request.POST.get("pub_date")
        book.save()

        url=reverse("booktest:index")
        return redirect(to=url)