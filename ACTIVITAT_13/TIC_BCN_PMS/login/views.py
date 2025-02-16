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
                # El login funciona correctament sense sessions
                # En el login sense sessions, com sabem que l'usuari no ha fet login
                # per a que el main page pugui retornar al login?
                # A més, ha de permetre una primera redirecció al main page quan es fa login correctament.
                # Farem servir un session per comprovar aquest accés temporal,
                # tot i que aquest sessió no té el propósit d'emmagatzemar l'id de l'usuari
                request.session["acces_temporal"] = True
                return redirect("paginaPrincipal")
            else:
                form.add_error(None, "Email o contrasenya incorrectes")
        except User.DoesNotExist:
            form.add_error(None, "Email o contrasenya incorrectes")

    context = {'form': form}
    return render(request, 'form.html', context)

def loginSession(request):
    # Evitem que l'usari logejat amb sessions
    # pugui accedir al login
    usuari = request.session.get('usuari', 'Invitado')
    if usuari is not "Invitado":
        return render(request, 'main_page.html')

    form = UserForm()

    if request.method == 'POST':
        form = UserForm(request.POST)
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            user = User.objects.get(email=email)
            if user.password == password and not (user is None):
                request.session['usuari'] = user.id
                return redirect("paginaPrincipal")
            else:
                form.add_error(None, "Email o contrasenya incorrectes")
        except User.DoesNotExist:
            form.add_error(None, "Email o contrasenya incorrectes")

    context = {'form': form}
    return render(request, 'formSessions.html', context)

def main_page(request):
    usuari = request.session.get('usuari', 'Invitado')

    if usuari is not "Invitado":
        try:
            usuari_obj = User.objects.get(id=usuari)
            return render(request, 'main_page.html', {"usuari": usuari_obj})
        except User.DoesNotExist:
            return redirect("loginUsuariSession")

    if request.session.get("acces_temporal"):
        # Esborrem l'accés temporal per a que l'usuari sense sessions
        # no pugui retornar al main page ja que
        # es suposa que no emmagatzemem el seu id
        # Només li donem accés al main page un cop
        del request.session["acces_temporal"]
        return render(request, "main_page.html")

    # Finalment, redireccionem al login
    # Nota: només es redirigeix al login sense sessions
    # quan s'intenta accedir al main_page sense sessió
    return redirect("loginUsuari")

def logout(request):
    if "usuari" in request.session:
        del request.session['usuari']

    return redirect("loginUsuariSession")