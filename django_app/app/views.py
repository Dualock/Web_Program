from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from .models import Estadio, TipoAsiento
from .forms import LoginForm, SignupForm, CreateEstadioForm, AdminSignupForm

def getBaseContext(request):
    context = {
        'isAuthenticated':request.user.is_authenticated,
        'user': None
    }
    if context['isAuthenticated']:
        context['user'] = request.user
    return context

def index(request):
    context = getBaseContext(request=request)
    context['is_home_active'] = True
    return render(request, "Home.html", context)

def estadios(request):
    context = getBaseContext(request=request)
    context['is_estadio_active'] = True
    context['estadios_disponibles'] = Estadio.objects.all
    return render(request, 'Estadios.html', context)

def estadio(request, estadio_id):
    context = getBaseContext(request=request)
    context['is_estadio_active'] = True
    context['estadio'] = Estadio.objects.get(id=estadio_id)
    return render(request, 'Estadio.html', context)

def log_in(request):
    context = getBaseContext(request=request)
    context['is_login_active'] = True
    context['form'] = None
    context['formInputSent'] = False
    context['userLoggedIn'] = False
    context['error'] = None
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
    context = getBaseContext(request=request)
    context['is_signup_active'] = True
    context['form'] = None
    context['formInputSent'] = False
    context['userCreated'] = False
    context['error'] = None
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
    context = getBaseContext(request=request)
    context['is_eventos_active'] = True
    return render(request, 'Eventos.html', context)

def yo(request):
    context = getBaseContext(request=request)
    context['is_perfil_active'] = True
    if not context['isAuthenticated']:
        return HttpResponseRedirect('/')
    return render(request, 'Eventos.html', context)

def perfil(request):
    context = getBaseContext(request=request)
    context['is_perfil_active'] = True
    if not context['isAuthenticated']:
        return HttpResponseRedirect('/')
    return render(request, 'Eventos.html', context)

def admin(request):
    context = getBaseContext(request=request)
    if not (context['isAuthenticated'] and (context['user'].is_staff or context['user'].is_superadmin)):
        return HttpResponseRedirect('/')
    context['is_admin_active'] = True
    context['userList'] = True
    context['create_estadio_form'] = CreateEstadioForm()
    context['admin_signup_form'] = AdminSignupForm()
    context['estadios_disponibles'] = Estadio.objects.all
    context['usuarios_disponibles'] = User.objects.all

    return render(request, 'Admin.html', context)
