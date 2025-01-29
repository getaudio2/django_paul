from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def show_students(request):
    return render(request,
                  'students.html')

def show_teachers(request):
    image = {"username": "getaudio2", "ranking": 5}
    return render(request,
                  'teachers.html',{'username': image["username"]})