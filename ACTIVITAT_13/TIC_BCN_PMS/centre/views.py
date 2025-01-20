from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_students(request):
    return render(request,
                  'students.html')

def show_teachers(request):
    return render(request,
                  'teachers.html')