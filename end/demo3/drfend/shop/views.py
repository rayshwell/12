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

from rest_framework import viewsets, permissions
from django.http import HttpResponse
from .models import *
from .serializers import *
from . import permissions as mypermissions
# 通过api_view装饰器可以将基于函数的视图转换成apiview基于类的视图
from rest_framework.decorators import api_view,action
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
# 引入频率限制
from rest_framework import throttling
from .throttling import *
# 引入分页
from .pagination import *
from django.views import View
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework import mixins
# 引入django过滤类
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
##   基于函数的视图
@api_view(['GET','POST'])
def categoryList(request):

    if request.method=="GET":
        # instance 为需要序列化的对象 来源于数据库
        queryset = Category.objects.all()
        seria = CategorySerizlizer(instance=queryset,many=True)
        return Response(seria.data)
    elif request.method=="POST":
        # data 为序列化对象，来源于从请求中提取的数据
        seria=CategorySerizlizer(data=request.data)
        # 从请求中提取的数据序列化之前需要检验
        if seria.is_valid():
            seria.save()
            return Response(seria.data)
        else:
            return Response(seria.errors,status=status.HTTP_404_NOT_FOUND)
@api_view(['GET','PUT','PATCH','DELETE'])
def categoryDetail(request,cid):
    model=get_object_or_404(Category,pk=cid)
    if request.method=="GET":
        seria=CategorySerizlizer(model)
        return Response(seria.data)
    elif request.method=="PUT" or  request.method=="PATCH":
        # 更新就是从请求中提取参数 替换掉数据库中取出的参数
        seria=CategorySerizlizer(instance=model,data=request.data)
        # 验证是否合法
        if seria.is_valid():
            seria.save()
            return Response(seria.data)
        else:
            return Response(seria.errors,status=status.HTTP_404_NOT_FOUND)
    elif request.method=="DELETE" :
        model.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return HttpResponse("当前路由不允许"+request.method+"操作")
##  基于类的视图
class CategoryListView1(APIView):
    """
    1 对django自带的view类需要重写对应的Http方法
    2 继承DRF自带的APIView类即可完成请求响应的封装
    """
    def get(self,request):
        # instance 从数据库中取
        seria=CategorySerizlizer(instance=Category.objects.all(),many=True)
        return Response(seria.data)
    def post(self,request):
        # data 从请求中取
        seria=CategorySerizlizer(data=request.data)
        # if seria.is_valid():
        #     seria.save()
        #     return Response(seria.data)
        # else:
        #     return Response(seria.errors)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)
class CategoryDetailView1(APIView):
    def get(self, request,cid):
        seria=CategorySerizlizer(instance=get_object_or_404(Category,pk=cid))
        return Response(seria.data)
    def put(self, request,cid):
        seria=CategorySerizlizer(instance=get_object_or_404(Category,pk=cid),data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)
    def patch(self,request,cid):
        seria = CategorySerizlizer(instance=get_object_or_404(Category, pk=cid), data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(seria.data)
    def delete(self,request,cid):
        get_object_or_404(Category,pk=cid).delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
##  基于类的混合视图
class CategoryListView2(generics.GenericAPIView,mixins.ListModelMixin,mixins.CreateModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer
    def get(self,request):
        return self.list(request)
    def post(self,request):
        return self.create(request)
class CategoryDetailView2(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer
    def get(self, request,pk):
        return self.retrieve(request,pk)
    def put(self, request,pk):
        return self.update(request,pk)
    def patch(self, request,pk):
        return self.update(request,pk)
    def delete(self, request,pk):
        return self.destroy(request,pk)
##  基于类的混合视图（高级）
class CategoryListView3(generics.ListCreateAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer
class CategoryDetailView3(generics.RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer
# 基于混合类的视图路由
class CategoryViewSets4(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerizlizer
# 最终版本
class CategoryViewSets(viewsets.ModelViewSet):
    """
    分类视图
    继承ModelViewSet 之后拥有GET POST PUT PATCH DELETE等HTTP动词操作
    queryset 指明需要操作的模型列表
    serializer_class 指明序列化类
    """
    # 如果你只是返回列表，那么用queryset
    # 如果需要处理，那么可以使用base_anme 结合get_queryset
    queryset = Category.objects.all()
    # def get_queryset(self):
    #     return  Category.objects.all()[:2]
    serializer_class=CategorySerizlizer

    # @action(methods=['GET'],detail=False)
    # def getlatestcategory(self,request):
    #     seria=CategorySerizlizer(instance=Category.objects.all()[:2],many=True)
    #     return  Response(data=seria.data,status=status.HTTP_200_OK)
    # permission_classes = [permissions.IsAdminUser]
    #
    def get_permissions(self):
        if self.action=="create" or self.action=="update"or self.action=="partial_update" or self.action=="destroy":
            return [permissions.IsAdminUser()]
            # 自定义权限
            # return [mypermissions.CategoryPermission()]
        else:
            return []
    # throttle_classes = [MyAnon, MyUser]
    pagination_class = MyPagination
    filter_backends = [DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields=["name"]
    search_fields=["name"]
class GoodViewSets(viewsets.ModelViewSet):
    queryset = Good.objects.all()
    serializer_class = GoodSerizlizer
class GoodImgsViewSets(viewsets.ModelViewSet):
    queryset = GoodImgs.objects.all()
    serializer_class = GoodImgsSerizlizer
class UserViewSets1(viewsets.GenericViewSet,mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    # 声明用户资源类 用户操作 获取个人信息，更新个人信息 删除用户
    # 扩展出action路由 用户操作 创建用户
    queryset = User.objects.all()
    serializer_class = UserSerizlizer
    # 使用action扩展资源的http方法
    @action(methods=['POST'], detail=False)
    def regist(self, request):
        seria = UserRegistSerizlizer(data=request.data)
        seria.is_valid(raise_exception=True)
        seria.save()
        return Response(data=seria.data, status=status.HTTP_200_OK)
class UserViewSets(viewsets.GenericViewSet,mixins.CreateModelMixin, mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    queryset = User.objects.all()
    def get_serializer_class(self):
        if self.action=="create":
            return UserRegistSerizlizer
        return UserSerizlizer
class OrderViewSets(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerizlizer
    def get_permissions(self):
        # 超级管理员可以展示所有订单
        # 普通用户可以创建修改订单，不可以操作其他用户的订单
        if self.action=="create":
            return [permissions.IsAuthenticated()]
        elif self.action=="update"or self.action=="partial_update" or self.action=="retrieve":
            return [mypermissions.OrderPermission()]
        else:
            return [permissions.IsAdminUser()]


# http方法                          混合类关键字                   action关键字
# GET列表                             List                          get
# POST创建对象                        Create                        create
# GET 单个对象                        Retrieve                      retrieve
# PUT 修改对象提供全属性              Update                        update
# PATCH 修改对象提供部分属性          Update                        partial_update
# DELETE 删除对象                     Destroy                       destroy

