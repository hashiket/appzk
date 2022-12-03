from django.urls import path
from . import views

urlpatterns = [
   
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('logout', views.logout, name='logout'),
    path('post', views.post, name='post'),
    path('allpost', views.allpost, name='allpost')


]

