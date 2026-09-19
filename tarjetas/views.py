from django.shortcuts import render
from django.core.paginator import Paginator
from .services import obtener_cartas_blue_eyes, obtener_carta_por_id

def lista_tarjetas(request):
    cartas = obtener_cartas_blue_eyes()
    paginator = Paginator(cartas, 12)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'tarjetas/lista_tarjetas.html', {'page_obj': page_obj})

def detalle_tarjeta(request, carta_id):
    tarjeta = obtener_carta_por_id(carta_id)
    return render(request, 'tarjetas/detalle_tarjeta.html', {'tarjeta': tarjeta})