from django.urls import path
from . import views

urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'),
    path('cliente/<int:pk>/', views.cliente_detalle, name='cliente_detalle'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('agregar_tratamiento/', views.agregar_tratamiento, name='agregar_tratamiento'),
]
