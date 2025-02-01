from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('next/', views.post_list, name='post_list'),
    path('next/', views.next, name='next'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
]