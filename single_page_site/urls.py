from django.contrib import admin
from django.urls import path
from django.shortcuts import render
from users import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('', lambda request: render(request, 'home.html'), name='home'),
]
