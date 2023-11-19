from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.home, name="home"),
    path('company', views.company, name="company"),
    path('service', views.service, name="service"),
    path('technology', views.technology, name="technology"),
    path('contact', views.contact, name="contact"),
    path('home', views.home, name="home"),
    # path('search', views.search, name="search"),
    # path('signup', views.handleSignUp, name="handleSignUp"),
    # path('login', views.handeLogin, name="handleLogin"),
    # path('logout', views.handelLogout, name="handleLogout"),
    # path('feedback',views.feedback, name="feedback"),
]



