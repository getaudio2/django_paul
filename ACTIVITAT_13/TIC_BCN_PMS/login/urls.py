from django.urls import path
from . import views

urlpatterns = [
    path('login', views.login, name="loginUsuari"),
    path('main_page', views.main_page, name="paginaPrincipal"),
]