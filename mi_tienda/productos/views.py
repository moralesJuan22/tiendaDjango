from django.shortcuts import render
from django.http import JsonResponse
from .models import Producto


def buscar_productos(request):
    
    termino_busqueda = request.GET.get('termino', '')
    productos = Producto.objects.filter(nombre__icontains=termino_busqueda)
    resultados = [{'id': producto.id, 'nombre': producto.nombre, 'precio': 
        str(producto.precio)} for producto in productos]
    
    return JsonResponse({'productos': resultados})

def lista_productos(request):
    productos = Producto.objects.all()
    
    return render(request, 'productos/lista_productos.html', {'productos': productos})

def detalle_producto(request, producto_id):
    producto = Producto.objects.get(pk=producto_id)
    
    return render(request, 'productos/detalle_producto.html', {'producto': producto})
