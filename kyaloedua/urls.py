from django.urls import path
from .import views


urlpatterns = [
    path('login', views.loginPage, name='login'),
    path('logout', views.logoutUser, name='logout'),
    path('register', views.registerPage, name='register'),

    path('', views.home, name='home'),
    path('home/room/<slug:pk>/', views.room, name='room'),

    path('about', views.about, name='about'),
    path('create_room', views.create_room, name='create_room'),
    path('home/update_room/<slug:pk>/', views.update_room, name='update_room'),
    path('home/delete_room/<slug:pk>/', views.delete_room, name='delete_room'),
    path('home/delete_message/<slug:pk>/', views.deleteMessage, name='delete_message'),
    
]
