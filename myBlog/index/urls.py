from django.urls import path

from . import views
app_name = 'indexManage'
urlpatterns = [

    # path('hello/', views.index2, name='index2'),
    path('', views.index, name='index'),
    #path('/', views.index, name='index'),
    path('registerIt', views.toRegister, name='toRegister'),
    path('RegisterUser', views.registerUser, name='registerUser'),
    path('checkRegister', views.checkRegister, name='checkRegister'),
    path('toLogin', views.toLogin, name='toLogin'),
    path('logined', views.logined, name='logined'),
    path('Logout', views.Logout, name='Logout'),
]