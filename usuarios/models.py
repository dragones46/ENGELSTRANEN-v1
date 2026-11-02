from datetime import date
from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):
    ROL_CHOICES = [
        ("cliente", "Cliente"),
        ("productor", "Productor"),
        ("admin", "Administrador"),
    ]

    email = models.EmailField("correo electrónico", unique=True)
    rol = models.CharField("rol", max_length=10, choices=ROL_CHOICES, default="cliente")
    fecha_nacimiento = models.DateField("fecha de nacimiento", null=True, blank=True)
    telefono = models.CharField("teléfono", max_length=20, blank=True)
    direccion = models.CharField("dirección", max_length=200, blank=True)

    def save(self, *args, **kwargs):
        if self.is_superuser:
            self.rol = "admin"
        super().save(*args, **kwargs)

    @property
    def es_admin(self):
        return self.rol == "admin" or self.is_superuser

    @property
    def es_productor(self):
        return self.rol == "productor"

    @property
    def edad(self):
        if not self.fecha_nacimiento:
            return None
        hoy = date.today()
        return hoy.year - self.fecha_nacimiento.year - (
            (hoy.month, hoy.day) < (self.fecha_nacimiento.month, self.fecha_nacimiento.day)
        )

    def __str__(self):
        return f"{self.username} ({self.get_rol_display()})"
