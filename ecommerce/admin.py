from django.contrib import admin
from .models import Producto, Orden, ItemOrden


@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = (
        'nombre',
        'precio',
        'duracion'
    )

    search_fields = (
        'nombre',
    )


@admin.register(Orden)
class OrdenAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'usuario',
        'fecha',
        'total'
    )

    list_filter = (
        'fecha',
        'usuario'
    )


@admin.register(ItemOrden)
class ItemOrdenAdmin(admin.ModelAdmin):
    list_display = (
        'orden',
        'producto',
        'cantidad',
        'subtotal'
    )