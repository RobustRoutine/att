from django.contrib import admin
from django.urls import path
from account import views


urlpatterns = [
    path('login',views.login,name='login'),
    path('register',views.register,name='register'),
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    #path('/logbtn',views.logbtn,name='logbtn'),
   # path('create', views.create, name='create'),
]
