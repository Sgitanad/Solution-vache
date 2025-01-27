from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='main'),
    path('/next', views.next, name='next'),
]