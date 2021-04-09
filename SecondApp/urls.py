#from django.conf.urls import url
from django.urls import path
from SecondApp import views

urlpatterns = [
    path('home',views.home),
    path('login',views.create),
    path('success',views.success,name="success"),   
]