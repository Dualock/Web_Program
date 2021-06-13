from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

from django.core.paginator import EmptyPage, Paginator

from .models import Estadio, TipoAsiento, Partido
from .forms import *

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

def estadios(request, pagina=1, per_page=5):
    context = getBaseContext(request=request)
    context['is_estadio_active'] = True
    estadios = Paginator(Estadio.objects.all(),per_page)
    try:
        context['estadios_disponibles'] = estadios.page(pagina)
    except EmptyPage:
        return HttpResponseRedirect('/estadios/%s' % estadios.num_pages)

    context['pagina'] = pagina
    context['paginas'] = range(1,estadios.num_pages+1)
    context['num_paginas'] = estadios.num_pages
    return render(request, 'Estadios.html', context)

def estadio(request, estadio_id):
    context = getBaseContext(request=request)
    context['is_estadio_active'] = True
    if request.user.is_authenticated:
        context['create_tipo_asiento_form'] = CreateTipoAsientoForm()
        context['create_partido_form'] = CreatePartidoForm()
    try:
        context['estadio'] = Estadio.objects.get(id=estadio_id)
        context['tipo_asientos_disponibles'] = TipoAsiento.objects.filter(estadio=estadio_id)
        context['eventos_creados'] = Partido.objects.filter(estadio = estadio_id)
    except Estadio.DoesNotExist:
        context['estadio'] = None

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
    context['create_tipo_asiento_form'] = CreateTipoAsientoForm()
    context['create_partido_form'] = CreatePartidoForm()

    return render(request, 'Admin.html', context)

def create_admin(request):
    context = getBaseContext(request=request)
    if not (context['isAuthenticated'] and (context['user'].is_staff or context['user'].is_superadmin)):
        return HttpResponseRedirect('/')
    context['is_admin_active'] = True
    context['userList'] = True
    context['create_estadio_form'] = CreateEstadioForm()
    context['admin_signup_form'] = AdminSignupForm()
    context['estadios_disponibles'] = Estadio.objects.all
    context['usuarios_disponibles'] = User.objects.all
    if request.method == 'POST':
        context['formInputSentSignup'] = True
        context['admin_signup_form'] = AdminSignupForm(request.POST)
        if context['admin_signup_form'].is_valid():
            try:
                data = context['admin_signup_form'].cleaned_data
                if User.objects.filter(email = data['email']).exists():
                    context['error'] = "El email ya existe, debe ser único."
                elif User.objects.filter(username = data['username']).exists():
                    context['error'] = "El nombre de usuario ya existe, debe ser único."
                else:
                    user = User.objects.create_user(data['username'], data['email'], data['password'])
                    user.first_name = data['nombre']
                    user.last_name = data['apellido']
                    if data['isStaff']:
                        user.is_staff = True
                    else:
                        user.is_staff = False
                    user.save()
                    return HttpResponseRedirect('/perfil/%s' %user.username)
            except Exception as e:
                print("Error desconocido en Signup")
                print(e)
                context['error'] = 'Error desconocido'
    return render(request, 'Admin.html', context)





def create_estadio(request):
    context = getBaseContext(request=request)
    if not context['isAuthenticated'] or not context['user'].is_staff:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context['formInputSent'] = True
        context['create_estadio_form'] = CreateEstadioForm(request.POST, request.FILES)
        if context['create_estadio_form'].is_bound:
            try:
                data = request.POST
                estadio = Estadio(nombre=data['nombre'], descripción=data['descripción'])
                estadio.save()
                print('estadio.id: %s' % estadio.id)
                #u_file = request.FILES
                #for s_file in u_file: print(s_file.name)
                context['userCreated'] = True
            except Exception as e:
                print("Error desconocido en Creación de Estadio")
                print(e)
                context['error'] = 'Error desconocido'
    else:
        return HttpResponseRedirect('/')
        # print(context)
    return HttpResponseRedirect('/estadios/')

def perfil_view(request, user_username):
    context = getBaseContext(request=request)
    context['is_perfil_active'] = True
    try:
        context['usuario'] = User.objects.get(username=user_username)
        if (not request.user.is_superuser) and (not request.user.id == context['usuario'].id):
            return HttpResponseRedirect('/')
    except User.DoesNotExist:
        context['usuario'] = None
        return HttpResponseRedirect('/')

    return render(request, 'Perfil.html', context)

def delete_estadio(request, estadio_id):
    context = getBaseContext(request=request)
    if not context['isAuthenticated'] or not context['user'].is_staff:
        return HttpResponseRedirect('/')

    try:
        Estadio.objects.get(id=estadio_id).delete()
        print('estadio borrado')
    except Estadio.DoesNotExist:
        print('ERROR: estadio no borrado')

    return HttpResponseRedirect('/estadios')

def create_tipo_asiento(request):
    context = getBaseContext(request=request)
    if not context['isAuthenticated'] or not context['user'].is_staff:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context['formInputSent'] = True
        context['create_tipo_asiento_form'] = CreateTipoAsientoForm(request.POST)
        if context['create_tipo_asiento_form'].is_valid():
            try:
                data = context['create_tipo_asiento_form'].cleaned_data
                estadio = Estadio.objects.all().get(id=request.POST['estadio_id'])
                tipoAsiento = TipoAsiento(
                    estadio=estadio,
                    nombre=data['nombre'],
                    costo=data['costo'],
                    capacidad=data['capacidad'],
                    descripcion=data['descripción']
                )
                tipoAsiento.save()
                context['tipoAsientoCreated'] = True
            except Exception as e:
                print("Error desconocido en Creación de Tipo de Asiento")
                print(e)
                context['error'] = 'Error desconocido'
    else:
        return HttpResponseRedirect('/')
        # print(context)
    return HttpResponseRedirect('/estadios/')

def create_event(request):
    context = getBaseContext(request=request)
    if not context['isAuthenticated'] or not context['user'].is_staff:
        return HttpResponseRedirect('/')
    if request.method == 'POST':
        context['formInputSent'] = True
        context['create_partido_form'] = CreatePartidoForm(request.POST)
        if context['create_partido_form'].is_valid():
            try:
                data = context['create_partido_form'].cleaned_data
                estadio = Estadio.objects.all().get(id=request.POST['estadio_id'])
                Partido = Partido(
                    estadio=estadio,
                    nombre=data['nompre_evento'],
                    inicio=data['inicio_tiempo'],
                    fin=data['fin_tiempo']
                )
                Partido.save()
                context['EventoCreated'] = True
            except Exception as e:
                print("Error desconocido en Creación del evento")
                print(e)
                context['error'] = 'Error desconocido'
    else:
        return HttpResponseRedirect('/')
        # print(context)
    return HttpResponseRedirect('/estadios/')
