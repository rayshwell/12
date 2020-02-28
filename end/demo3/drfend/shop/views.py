# from django.shortcuts import render
# from django.http import HttpResponse,JsonResponse
# from .models import *
# from django.core import serializers
# # django自带的序列化
# # Create your views here.
# def index(request):
#     category=Category.objects.all()
#     result=serializers.serialize("json",category)
#     return JsonResponse(result,safe=False)
from rest_framework import viewsets
from .models import *
from .serializers import *
class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    queryset = Category.objects.all()
    serializer_class=CategorySerizlizer

class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer

class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerizlizer