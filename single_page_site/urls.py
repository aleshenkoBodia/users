from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from users import views
from users.api_views import UserListAPI, UserDetailAPI

urlpatterns = [
    path('api/users/', UserListAPI.as_view(), name='user-list'),
    path('api/users/<int:pk>/', UserDetailAPI.as_view(), name='user-detail'),
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', lambda request: render(request, 'home.html'), name='home'),
]
