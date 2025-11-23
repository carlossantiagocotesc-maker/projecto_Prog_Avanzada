from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_pasajeros, name='lista_pasajeros'),
    path('agregar/', views.agregar_pasajero, name='agregar_pasajero'),
    path('editar/<int:pk>/', views.editar_pasajero, name='editar_pasajero'),
    path('eliminar/<int:pk>/', views.eliminar_pasajero, name='eliminar_pasajero'),
]