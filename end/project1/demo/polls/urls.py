from django.conf.urls import url
from . import views

app_name="polls"

urlpatterns = [
    # FBV形式的url
    url(r'^$', views.index,name='index'),
    url(r'^detail/(\d+)/$',views.detail,name='detail'),
    url(r'^result/(\d+)/$',views.result,name='result'),
    url(r'^login/$',views.login,name='login'),
    url(r'^loginout/$',views.loginout,name='loginout'),
    url(r'^regist/$',views.regist,name='regist')
    # CBV形式的url
    # url(r'^$',views.IndexView.as_view(),name='index'),
    # url(r'^detail/(\d+)/$',views.DetailView.as_view(),name='detail'),
    # url(r'^result/(\d+)/$',views.ResultView.as_view(),name='result'),

]