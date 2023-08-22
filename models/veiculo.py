from django.db import models

from models.cor import Cor
from models.modelo import Modelo
from uploader.models import Image


class Veiculo(models.Model):
    id = models.BigAutoField(primary_key=True)
    cor = models.ForeignKey(
        Cor, on_delete=models.PROTECT, related_name="veiculos"
    )
    modelo = models.ForeignKey(
        Modelo, on_delete=models.PROTECT, related_name="veiculos"
    )
    ano = models.IntegerField(null=True, blank=True)
    descricao = models.CharField(max_length=255, null=True, blank=True)
    preco = models.DecimalField(
        decimal_places=3, max_digits=6, null=True, blank=True
    )
    imagem = models.ManyToManyField(Image)

    def __str__(self):
        return f"{self.modelo} ({self.ano})"

    class Meta:
        verbose_name = "Veiculo"
        verbose_name_plural = "Veiculos"
