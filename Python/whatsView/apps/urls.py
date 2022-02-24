from django.conf.urls import url, include
from django.urls import path
from . import views

urlpatterns = [
    # url(r'^', views.index, name='index'),
    path('', views.index, name='index'),
    # path('all/', views.all, name="all"),
    path('all', views.all, name='all'),
    # url(r'all/$', views.all, name="all"),
    url(r'info/', views.get_request_url, name="info"),
    url(r'video/', views.youtube, name="video"),
]