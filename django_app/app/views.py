from django.http import HttpResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect

from django.contrib.auth import authenticate, login, logout

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
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LoginForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # login(request=request)
                login(request, user)
                # Redirect to a success page.
                return HttpResponseRedirect('/')
            else:
                # Return an 'invalid login' error message.
                return render(request, 'Login.html', {'form': form, 'isError': True})
            # ...
            # print(form.cleaned_data)
            # redirect to a new URL:
    # if a GET (or any other method) we'll create a blank form
    else:
        form = LoginForm()

    return render(request, 'Login.html', {'form': form})

def signup(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SignupForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/thanks/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SignupForm()

    return render(request, 'Signup.html', {'form': form})

def log_out(request):
    logout(request)
    return HttpResponseRedirect('/')

def eventos(request):
    return render(request, 'Eventos.html')
