from django.urls import path
from django.contrib import admin
from . import views

urlpatterns = [
    path('', views.home, name='homepage'),
    path('search/', views.event_search, name='searchpage'),
    path('profile/', views.profile, name='profilepage'),
    path('eventcreate/',views.eventcreate,name='eventcreatepage'),
    path('profile/profileupdate/',views.profileupdate,name='profileupdate'),
    path('profile/deleteuser/<int:user_id>',views.delete_user,name='deleteuser'),
    path('createaccount/', views.create_account, name='createaccount'),
    path('login/', views.login, name='login'),
    path('update/<int:event_id>/', views.update_event, name='updateevent'),
    path('delete/<int:event_id>/', views.delete_event, name='deleteevent'),
    path('eventlanding/<int:event_id>/', views.event_landing_page, name='eventlanding'),
    path('eventlanding/<int:event_id>/comment', views.add_comment, name='addcomment'),
    path('eventlanding/<int:event_id>/rsvp', views.rsvp_to_event, name='addrsvp'),
    path('logout/', views.logout, name='logout'),
    path('profile/deletersvp/<int:rsvp_id>/', views.delete_rsvp, name='deletersvp')
]
