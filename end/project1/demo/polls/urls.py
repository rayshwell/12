from django.conf.urls import url
from . import views

app_name="polls"

urlpatterns = [

    url(r'^$', views.index,name='index'),
    # url(r'^detail/(\d+)/$',views.detail,name='detail'),


    # url(r'^addhero/(\d+)/$',views.addhero,name='addhero'),
]