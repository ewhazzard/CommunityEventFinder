from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.event_search, name='searchpage')
]
