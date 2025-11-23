from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_aviones, name='lista_aviones'),
    path('agregar/', views.agregar_avion, name='agregar_avion'),
    path('editar/<int:pk>/', views.editar_avion, name='editar_avion'),
    path('eliminar/<int:pk>/', views.eliminar_avion, name='eliminar_avion'),
]