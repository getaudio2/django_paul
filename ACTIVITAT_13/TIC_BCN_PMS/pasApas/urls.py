from django.urls import path
from . import views

urlpatterns = [
    path('user/guardar_sesion', views.guardar_sesion, name="guardar_sesion"),
    path('user/recuperar_sesion', views.recuperar_sesion, name="recuperar_sesion"),
    path('user/eliminar_sesion', views.eliminar_sesion, name="eliminar_sesion"),
]