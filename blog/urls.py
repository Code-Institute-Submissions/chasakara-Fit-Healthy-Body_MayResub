from django.urls import path
from . import views

urlpatterns = [
    path('', views.allblogs, name='allblogs'),
    path('<int:blog_id>/', views.blog_detail, name='blog_detail'),
    path('add/', views.add_blog, name='add_blog'),
]