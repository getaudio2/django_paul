from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

students = [
    {
        'id': '1',
        'nom': 'Paúl',
        'cognom1': 'Maigua',
        'cognom2': 'Sarango',
        'correu': 'paul@gmail.com',
        'curs': 'DAW2A',
        'moduls': 'M6, M7, M8, PROJECTE'
    },
    {
        'id': '2',
        'nom': 'Alex',
        'cognom1': 'Johnson',
        'cognom2': 'Miller',
        'correu': 'alex.johnson.miller@example.com',
        'curs': 'DAW2A',
        'moduls': 'M6, M7, M8, PROJECTE'
    },
    {
        'id': '3',
        'nom': 'Emma',
        'cognom1': 'Smith',
        'cognom2': 'Taylor',
        'correu': '	emma.smith.taylor@example.com',
        'curs': 'DAW2A',
        'moduls': 'M6, M7, M8, PROJECTE'
    }
]

teachers = [
    {
        'id': '1',
        'nom': 'Roger',
        'cognom1': 'Sobrino',
        'cognom2': 'SegonCognom',
        'correu': 'roger@gmail.com',
        'curs': 'DAW2A',
        'tutor': 'Sí',
        'moduls': 'M7'
    },
    {
        'id': '2',
        'nom': 'Daniel',
        'cognom1': 'Brown',
        'cognom2': 'Wilson',
        'correu': '	daniel.brown.wilson@example.com',
        'curs': 'DAW2B',
        'tutor': 'No',
        'moduls': 'M6'
    },
    {
        'id': '3',
        'nom': 'Sophia',
        'cognom1': 'Martinez',
        'cognom2': 'Garcia',
        'correu': '	sophia.martinez.garcia@example.com',
        'curs': 'DAM2A',
        'tutor': 'No',
        'moduls': 'M8'
    }
]

def show_students(request):
    return render(request,
                  'students_table.html', {'students': students})

def student(request, pk):
    student_obj = None
    for i in students:
        if i['id'] == pk:
            student_obj = i
    return render(request, 'student_table.html', {'students': student_obj})

def show_teachers(request):
    return render(request,
                  'teachers.html',{'teachers': teachers})