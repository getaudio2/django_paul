from django.shortcuts import render

# Create your views here.
def login(request):
    return render(request, 'login.html')

def main_page(request):
    return render(request, 'main_page.html')