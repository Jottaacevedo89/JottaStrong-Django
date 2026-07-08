from django.contrib import admin
from .models import Postulante


@admin.register(Postulante)
class PostulanteAdmin(admin.ModelAdmin):

    list_display = (
        'nombre',
        'email',
        'edad',
        'objetivo',
        'compromiso',
        'fecha'
    )

    list_filter = (
        'objetivo',
        'compromiso',
        'fecha'
    )

    search_fields = (
        'nombre',
        'email'
    )