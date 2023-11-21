from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('index/', views.principal, name="index"),
    path('crear/', views.crear, name="Crear"),
    path('menu/', views.menu, name="logged"),
    path('comida1/', views.comida1, name="comida1"),
    path('comida2/', views.comida2, name="comida2"),
    path('comida3/', views.comida3, name="comida3"),
    path('perfil/', views.perfil, name="perfil"),
]
