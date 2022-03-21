from django.urls import path

from . import views

urlpatterns = [
    path('', views.login, name="login"),  #
    path('register/', views.reginter, name="register"),  #
    path('pswd_update/', views.pswd_update, name="pswd_update"),  #
    path('logout/', views.logout, name="logout"),  #

]
