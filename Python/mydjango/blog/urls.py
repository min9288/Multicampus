from django.urls import path
from . import views

urlpatterns = [
    # http://localhost:8000/blog
    path('', views.post_list, name='post_list_home'),
    # http://localhost:8000/blog/post/5
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    # http://localhost:8000/blog/post/new
    path('post/new', views.post_new, name='post_new'),
]