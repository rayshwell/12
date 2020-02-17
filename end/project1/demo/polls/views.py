from django.shortcuts import render,redirect,reverse
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ticket,Article
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
