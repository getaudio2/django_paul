from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="loginUsuari"),
    path('loginSession', views.loginSession, name="loginUsuariSession"),
    path('main_page', views.main_page, name="paginaPrincipal"),
    path('logout', views.logout, name="logout")
]