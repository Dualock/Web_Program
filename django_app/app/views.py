from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Estadio
from .forms import LoginForm, SignupForm

def index(request):

    #return HttpResponse("Hello, world. You're at the polls index.")
    print(request.user.is_authenticated)
    return render(request, "Home.html", {'isAuthenticated':request.user.is_authenticated})


def estadios(request):
    estadios_disponibles = Estadio.objects.all
    context = {
        'estadios_disponibles': estadios_disponibles
    }
    return render(request, 'Estadios.html', context)

def estadio(request, estadio_id):
    info_estadio = Estadio.objects.get(id=estadio_id)
    print(info_estadio)
    context = {
        'estadio': info_estadio
    }
    return render(request, 'Estadio.html', context)

def log_in(request):
    context = {
        'isAuthenticated':request.user.is_authenticated,
        'form': None,
        'formInputSent': False,
        'userLoggedIn': False,
        'error': None,
        'is_login_active': True
    }

    if (context['isAuthenticated']):
        return HttpResponseRedirect('/')

    if request.method == 'POST':
        context['formInputSent'] = True
        context['form'] = LoginForm(request.POST)
        if context['form'].is_valid():
            data = context['form'].cleaned_data
            user = authenticate(request, username = data['username'], password = data['password'])
            if user is not None:
                login(request, user)
                context['userLoggedIn'] = True
                return HttpResponseRedirect('/')
            else:
                context['error'] = "Datos Inválidos."
    else:
        context['form'] = LoginForm()

    return render(request, 'Login.html', context)

def signup(request):
    context = {
        'isAuthenticated':request.user.is_authenticated,
        'form': None,
        'formInputSent': False,
        'userCreated': False,
        'error': None,
        'is_signup_active': True
    }
    if (context['isAuthenticated']):
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context['formInputSent'] = True
        context['form'] = SignupForm(request.POST)
        if context['form'].is_valid():
            try:
                data = context['form'].cleaned_data
                if User.objects.filter(email = data['email']).exists():
                    context['error'] = "El email ya existe, debe ser único."
                elif User.objects.filter(username = data['username']).exists():
                    context['error'] = "El nombre de usuario ya existe, debe ser único."
                else:
                    user = User.objects.create_user(data['username'], data['email'], data['password'])
                    user.first_name = data['nombre']
                    user.last_name = data['apellido']
                    user.save()
                    context['userCreated'] = True
            except Exception as e:
                print("Error desconocido en Signup")
                print(e)
                context['error'] = 'Error desconocido'
    else:
        context['form'] = SignupForm()
    print(context)
    return render(request, 'Signup.html', context)

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def eventos(request):
    return render(request, 'Eventos.html')
