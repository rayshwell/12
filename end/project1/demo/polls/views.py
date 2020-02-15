from django.shortcuts import render,redirect,reverse
from django.template import loader
# Create your views here.
from django.http import HttpResponse,HttpResponseRedirect
from .models import Ticket,Article
def index(request):

    Articles=Article.objects.all()

    return render(request,'polls/index.html',{'Articles':Articles})
