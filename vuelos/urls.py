from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_vuelos, name='lista_vuelos'),
    path('agregar/', views.agregar_vuelo, name='agregar_vuelo'),
    path('editar/<int:pk>/', views.editar_vuelo, name='editar_vuelo'),
    path('eliminar/<int:pk>/', views.eliminar_vuelo, name='eliminar_vuelo'),
]