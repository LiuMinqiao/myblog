from django.urls import path

from . import views

urlpatterns = [

    path('hello/', views.index2, name='index2'),
    path('', views.index, name='index'),
]