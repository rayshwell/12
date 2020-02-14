from django.conf.urls import url
from . import views

app_name="booktest"

urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^about/$',views.about,name='about'),
    # 使用正则分组可以像视图函数中传递参数
    # 第一个参数就是路由，第二个参数就是视图函数
    # 第一个参数中如果有正则分组 （） 则正则分组,匹配的内容会作为实参传递给视图函数
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^deletebook/(\d+)/$',views.deletebook,name='deletebook'),
    url(r'^deletehero/(\d+)/$',views.deletehero,name='deletehero'),
    url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
    url(r'^edithero/(\d+)/$',views.edithero,name='edithero'),

]

