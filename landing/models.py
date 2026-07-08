from django.db import models


class Postulante(models.Model):
    OBJETIVOS = [
        ('Perder grasa', 'Perder grasa'),
        ('Ganar masa muscular', 'Ganar masa muscular'),
        ('Recomposición corporal', 'Recomposición corporal'),
        ('Mejorar rendimiento', 'Mejorar rendimiento'),
    ]

    nombre = models.CharField(max_length=120)
    email = models.EmailField()
    edad = models.IntegerField()
    objetivo = models.CharField(max_length=100, choices=OBJETIVOS)
    compromiso = models.IntegerField()

    dificultad_actual = models.TextField()
    experiencia_previa = models.TextField()
    motivacion = models.TextField()

    fecha = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nombre
