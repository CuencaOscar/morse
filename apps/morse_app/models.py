from django.db import models

# Create your models here.
class Morse(models.Model):
    caracter = models.CharField(max_length=2)
    codigo = models.CharField(max_length=4)

    def __str__(self):
        return f"{self.caracter} --> ({self.codigo})"