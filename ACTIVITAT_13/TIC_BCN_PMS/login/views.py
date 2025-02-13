from wsgiref.util import request_uri

from django.shortcuts import render, redirect
from .forms import UserForm
from .models import User

# Create your views here.
def login(request):
    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if user.password == password and not(user is None):
                return redirect("paginaPrincipal")
            else:
                form.add_error(None, "Email o contrasenya incorrectes")
        except User.DoesNotExist:
            form.add_error(None, "Email o contrasenya incorrectes")

    context = {'form': form}
    return render(request, 'form.html', context)

def main_page(request):
    return render(request, 'main_page.html')