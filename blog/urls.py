from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/next', views.next, name='next'),
    path('/post_liste', views.post_liste, name='post_liste'),
    path('post/new/', views.post_new, name='post_new'),
]