from django.shortcuts import render,redirect,reverse
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ticket,Article
# 基于FBV的形式来实现视图
def index(request):
    articles=Article.objects.all()
    return render(request,'polls/index.html',{'articles':articles})
def detail(request,articleid):
    article=Article.objects.get(id=articleid)
    tickets=article.articles.all()
    if request.method == "GET":
        return render(request,'polls/detail.html',{'article':article,'tickets':tickets})
    elif request.method == "POST":
        ticketid = request.POST.get("choice")
        ticketid=int(ticketid)
        print(ticketid,type(ticketid))
        ticket=Ticket.objects.get(id=ticketid)
        ticket.count+=1
        ticket.save()
        url = reverse("polls:result", args=(articleid,))
        return redirect(to=url)
def result(request,articleid):
    article = Article.objects.get(id=articleid)
    tickets = article.articles.all()
    # url = reverse("polls:result", args=(articleid,))
    # return redirect(to=url)
    # return HttpResponse("这是关于页面")tickets
    return render(request,'polls/result.html',{'article':article,'tickets':tickets})


# 基于CBV的形式实现视图
from django.views.generic import View,TemplateView,CreateView,ListView,DeleteView,UpdateView

# View类是所有视图响应类的父类
class IndexView(TemplateView):
    # 方法一 继承ListView
    #  template_name 指明返回的模板
    # template_name = 'polls/index.html'
    # queryset 指明返回的结果
    # queryset=Article.objects.all()
    # 指明返回字典参数的键
    # content_object_name = "articles"

    # 方法二：继承的TemplateView
    template_name = 'polls/index.html'
    def get_context_data(self, **kwargs):
        return {"articles":Article.objects.all()}
class DetailView(View):
    def get(self,request,articleid):
        article = Article.objects.get(id=articleid)
        tickets = article.articles.all()
        return render(request,'polls/detail.html',{'article':article,'tickets':tickets})
    def post(self,request,articleid):
        ticketid = request.POST.get("choice")
        ticketid = int(ticketid)
        print(ticketid, type(ticketid))
        ticket = Ticket.objects.get(id=ticketid)
        ticket.count += 1
        ticket.save()
        url = reverse("polls:result", args=(articleid,))
        return redirect(to=url)
class ResultView(View):
    def get(self,request,articleid):
        article = Article.objects.get(id=articleid)
        tickets = article.articles.all()
        return render(request, 'polls/result.html', {'article': article, 'tickets': tickets})

