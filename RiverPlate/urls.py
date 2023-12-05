from django.urls import path
from RiverPlate import views

urlpatterns = [
    path('', views.inicio),
    path('registro/', views.registro),
    path('socios/', views.socios),
    path('entradas/', views.entradas),
    path('registro_formulario/', views.registro_formulario),
    path('socios_formulario/', views.socios_formulario),
    path('entradas_formulario/', views.entradas_formulario),
    path('buscarSocio/', views.buscar_socio),
    path('buscar/', views.buscar),
]