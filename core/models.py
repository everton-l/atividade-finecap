from pickle import TRUE
from django.db import models
from django.utils import timezone

# Create your models here.

class Stand(models.Model):
    localizacao = models.CharField(max_length=100)
    valor = models.FloatField()

    def __str__(self) -> str:
        return self.localizacao


class Reserva(models.Model):
    cnpj = models.CharField(max_length=14)
    nome_empresa = models.CharField(max_length=100)
    categoria_empresa = models.CharField(max_length=100)
    quitado = models.BooleanField(blank=True)
    stand = models.ForeignKey(Stand, on_delete=models.CASCADE)
    data = models.DateField(default=timezone.now)  

    def __str__(self) -> str:
        return self.nome_empresa