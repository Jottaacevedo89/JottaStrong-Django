from django.db import models
from django.contrib.auth.models import User


class Producto(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    precio = models.IntegerField()
    incluye = models.TextField()
    duracion = models.CharField(max_length=50, default="12 semanas")

    def __str__(self):
        return self.nombre


class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.IntegerField(default=0)

    def __str__(self):
        return f"Orden #{self.id} - {self.usuario.username}"


class ItemOrden(models.Model):
    orden = models.ForeignKey(Orden, on_delete=models.CASCADE, related_name="items")
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    cantidad = models.IntegerField(default=1)
    subtotal = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.producto.nombre} x {self.cantidad}"