from django.urls import path 
from . import views 


urlpatterns  = [
    path("", views.index, name="index"),
    path("user-login", views.user_login, name="login"),
    path("user-logout", views.user_logout, name="logout"),
    path('user-registration', views.user_register, name="registration")
]