from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.event_search, name='searchpage'),
    path('profile/', views.profile, name='profilepage'),
    path('login/', views.login, name='loginpage'),
    path('eventcreate/',views.eventcreate,name='eventcreatepage')
]
