from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('blog/<slug:slug>/', views.blog_detail, name='blog_detail'),
    path('category/<str:category_name>/', views.category_posts, name='category_posts'),
]
