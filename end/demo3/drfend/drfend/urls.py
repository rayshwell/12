"""drfend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url
from shop.views import *
from .settings import MEDIA_ROOT
from django.views.static import serve
# 引入jwt路由
# from rest_framework_jwt.views import obtain_jwt_token
# 引入simplejwt路由
from rest_framework_simplejwt.views import token_obtain_pair,token_refresh
# 引入DRF自带的路由类
from  rest_framework import routers
# 引入API文档路由
from  rest_framework.documentation import include_docs_urls
router=routers.DefaultRouter()
# 可以通过router默认路由注册资源
router.register("categorys",CategoryViewSets)
router.register("goods",GoodViewSets)
router.register("goodImgs",GoodImgsViewSets)
router.register("users",UserViewSets)
router.register("orders",OrderViewSets)

from shop.views import *
urlpatterns = [
    path('admin/', admin.site.urls),
    url('media/(?P<path>.*)',serve,{'document_root': MEDIA_ROOT}),

    # 配置restfulAPI(最终版本)
    path('api/v1/',include(router.urls)),
    # 配置API文档路由
    path('api/v1/docs/',include_docs_urls(title="RestfulAPI",description="RestfulAPIv1")),
    # 为了在drf路由调试页面能够使用用户相关功能需要使用以下路由
    path('',include('rest_framework.urls')),
    # 设置jwt路由
    # url(r'^obtain_jwt_token/$',obtain_jwt_token),
    # 设置simplejwt路由
    url(r'^loginn/$',token_obtain_pair,name="loginn"),
    url(r'^refresh/$',token_refresh,name="refresh"),
    # 基于混合类的视图路由
    # url(r'^categorys/$', CategoryViewSets4.as_view({'get':'list','post':'create'})),
    # url(r'^categorys/(?P<pk>\d+)/$', CategoryViewSets4.as_view({'get':'retrieve','put':'update','patch':'update','delete':'destroy'})),

    # 基于类的混合视图路由（CategoryListView2和CategoryListView3）
    # url(r'^categorylist/$', CategoryListView2.as_view(), name="categorylist"),
    # url(r'^categorydetail/(?P<pk>\d+)/$', CategoryDetailView2.as_view(), name="categorydetail"),

    # # 基于类的视图路由
    # url(r'^categorylist/$', CategoryListView1.as_view(), name="categorylist"),
    # url(r'^categorydetail/(\d+)/$', CategoryDetailView1.as_view(), name="categorydetail"),

    # 基于函数的视图路由
    # url(r'^categorylist/$', categoryList, name="categorylist"),
    # url(r'^categorydetail/(\d+)/$', categoryDetail, name="categorydetail"),
]
