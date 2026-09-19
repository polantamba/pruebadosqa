from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_tarjetas, name='lista_tarjetas'),
    path('detalles/<int:carta_id>/', views.detalle_tarjeta, name='detalle_tarjeta'),
]