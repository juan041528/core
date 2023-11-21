from django.http import HttpResponse
from django.contrib.auth import login
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .models import User
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.db.utils import IntegrityError
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required

#def principal(request):
    #return HttpResponse("hola")

def principal(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        # Intenta autenticar al usuario
        user = authenticate(request, username=email, password=password)
        if user is not None:
            # El usuario y la contraseña son válidos, inicia sesión y redirige a la página "logged".
            login(request, user)
            return redirect('logged')  # Asegúrate de que 'logged' sea el nombre correcto de tu URL.

        # Si la autenticación falla, muestra un mensaje de error.
        error_message = "Usuario o contraseña incorrectos. Por favor, inténtelo de nuevo."
        return render(request, 'registration/login.html', {'error_message': error_message})

    return render(request, 'registration/login.html')

def crear(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        if not email or not password:
            # Si uno de los campos está vacío, muestra un mensaje de error.
            error_message = "Por favor, complete todos los campos."
            return render(request, 'crearUsuario.html', {'error_message': error_message})
        try:
            subject = 'Correo registrado'
            message = f'Se ha registrado correctamente, esperamos que pueda generar sus recetas \n Su contraseña es: {password}'
            email_from = 'recetasyareya@gmail.com'
            recipient_list = [email]
            user = User.objects.create_user(username=email, email=email, password=password)
            send_mail(subject, message, email_from, recipient_list)
            return redirect('index')
        except IntegrityError:
            # El correo ya está registrado, muestra un mensaje de error.
            error_message = "El correo ya está registrado. Por favor, use otro correo."
            return render(request, 'crearUsuario.html', {'error_message': error_message})
    return render(request, 'crearUsuario.html')

@login_required
def comida1(request):
    return render(request, 'pages/comida-1.html')

@login_required
def comida2(request):
    return render(request, 'pages/comida-2.html')

@login_required
def comida3(request):
    return render(request, 'pages/comida-3.html')


@login_required
def perfil(request):
    return render(request, 'pages/perfil.html')

@login_required
def menu(request):
    return  render(request, 'pages/menu.html')
