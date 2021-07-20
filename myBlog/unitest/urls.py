from django.urls import path
from django.conf.urls import  url
from . import views

urlpatterns = [
    path('', views.index, name='index1'),
    url(r'^index', views.index, name='index2'),
    url(r'^showAll', views.showAll),
    url(r'^toaddUser', views.toaddUser),
    url(r'^addUser', views.addUser),
    url(r'^deleteUser/', views.deleteUser),
    url(r'^updateUser/', views.toUpdate),
    url(r'^updatedUser', views.updateUser),

]
