from django.shortcuts import render
from .forms import UserForm

# Create your views here.
def login(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'login.html', context)

def main_page(request):
    return render(request, 'main_page.html')