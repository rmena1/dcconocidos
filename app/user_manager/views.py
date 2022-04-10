from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import createUserForm, profileForm
from .models import Profile

def index(request):
    return HttpResponse("Hello, world. You're at the user manager index.")

def register_user(request):
    #Falta agregar mas datos de los usuarios que piden en enunciado
    form = createUserForm(request.POST or None)
    profile_form = profileForm(request.POST or None)
    if request.method == 'POST':

        if form.is_valid():
            user = form.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            login_user = authenticate(username=username, password=password)

            login(request, login_user)
        else:
            messages.success(request, ("Hubo un problema registrando el usuario, intenta nuevamente."))
        return(redirect('/'))
    else:
        context = {'form': form, 'profile_form': profile_form}
        return render(request, 'user_manager/register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return(redirect('/'))
        else:
            messages.success(request, ("Hubo un problema iniciando sesión, intenta nuevamente."))
            return redirect('/user_manager/login')
    else:
        return render(request, 'user_manager/login.html', {})

def logout_user(request):
    logout(request)
    return(redirect('/'))
