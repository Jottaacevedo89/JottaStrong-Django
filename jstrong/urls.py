"""
URL configuration for jstrong project.
"""

from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from landing.views import home

from ecommerce.views import (
    catalogo,
    agregar_carrito,
    ver_carrito,
    quitar_carrito,
    confirmar_compra
)


urlpatterns = [

    path('admin/', admin.site.urls),

    path('', home, name='home'),

    # LOGIN / LOGOUT
    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        auth_views.LogoutView.as_view(),
        name='logout'
    ),

    # ECOMMERCE

    path('programas/', catalogo, name='catalogo'),

    path(
        'agregar/<int:producto_id>/',
        agregar_carrito,
        name='agregar_carrito'
    ),

    path(
        'carrito/',
        ver_carrito,
        name='carrito'
    ),

    path(
        'quitar/<int:producto_id>/',
        quitar_carrito,
        name='quitar_carrito'
    ),

    path(
        'confirmar-compra/',
        confirmar_compra,
        name='confirmar_compra'
    ),
]