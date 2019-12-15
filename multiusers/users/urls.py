from django.urls import path
from . import views

urlpatterns = [
    path('', views.index ,name='index'),
    path("register",views.register,name="register"),
    path("login",views.login,name="login"),
    path("logout",views.logout,name="logout"),
    path("user_details",views.user_details,name="user_details"),
    path("home",views.home,name="home"),
    path("allusers",views.allusers,name="allusers"),
]
