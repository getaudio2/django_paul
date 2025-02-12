from django.shortcuts import render
from .forms import UserForm
from .models import User

# Create your views here.
def login(request):
    form = UserForm()
    context = {'form': form}
    return render(request, 'form.html', context)

def main_page(request):
    return render(request, 'main_page.html')