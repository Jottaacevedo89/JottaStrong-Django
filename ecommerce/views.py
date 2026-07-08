from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Producto, Orden, ItemOrden


def catalogo(request):
    productos = Producto.objects.all()
    return render(request, 'catalogo.html', {'productos': productos})


def agregar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})

    producto_id = str(producto_id)

    if producto_id in carrito:
        carrito[producto_id] += 1
    else:
        carrito[producto_id] = 1

    request.session['carrito'] = carrito

    return redirect('carrito')


def ver_carrito(request):
    carrito = request.session.get('carrito', {})
    items = []
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal

        items.append({
            'producto': producto,
            'cantidad': cantidad,
            'subtotal': subtotal
        })

    return render(request, 'carrito.html', {
        'items': items,
        'total': total
    })


def quitar_carrito(request, producto_id):
    carrito = request.session.get('carrito', {})
    producto_id = str(producto_id)

    if producto_id in carrito:
        del carrito[producto_id]

    request.session['carrito'] = carrito

    return redirect('carrito')


@login_required
def confirmar_compra(request):
    carrito = request.session.get('carrito', {})

    if not carrito:
        return redirect('catalogo')

    orden = Orden.objects.create(usuario=request.user)
    total = 0

    for producto_id, cantidad in carrito.items():
        producto = get_object_or_404(Producto, id=producto_id)
        subtotal = producto.precio * cantidad
        total += subtotal

        ItemOrden.objects.create(
            orden=orden,
            producto=producto,
            cantidad=cantidad,
            subtotal=subtotal
        )

    orden.total = total
    orden.save()

    request.session['carrito'] = {}

    return render(request, 'compra_exitosa.html', {'orden': orden})