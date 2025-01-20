from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('students', views.show_students, name="students"),
    path('teachers', views.show_teachers, name="teachers"),
]
