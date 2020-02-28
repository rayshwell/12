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
# 引入DRF自带的路由类
from  rest_framework import routers
# 引入API文档路由
from  rest_framework.documentation import include_docs_urls
router=routers.DefaultRouter()
# 可以通过router默认路由注册资源
router.register("categorys",CategoryViewSets)
router.register("goods",GoodViewSets)
router.register("goodImgs",GoodImgsViewSets)
urlpatterns = [
    path('admin/', admin.site.urls),
    url('media/(?P<path>.*)',serve,{'document_root': MEDIA_ROOT}),
    # 配置restfulAPI
    path('api/v1/',include(router.urls)),
    # 配置API文档路由
    path('api/v1/docs/',include_docs_urls(title="RestfulAPI",description="RestfulAPIv1")),
    # 为了在drf路由调试页面能够使用用户相关功能需要使用以下路由
    path('',include('rest_framework.urls'))
]
