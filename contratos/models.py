from django.db import models

# Create your models here.
from django.db import models

from django.db import models

class Contrato(models.Model):
    ANO = models.IntegerField()
    contrato_no = models.CharField(max_length=100)
    tipo_de_contrato = models.CharField(max_length=100)
    nombre = models.CharField(max_length=255)
    entidad = models.CharField(max_length=255)
    rup = models.CharField(max_length=100, blank=True, null=True)
    contrato = models.CharField(max_length=100)
    smmlv = models.DecimalField(max_digits=10, decimal_places=2)
    secop = models.CharField(max_length=100, blank=True, null=True)
    contrato2 = models.CharField(max_length=100, blank=True, null=True)
    acta_final = models.CharField(max_length=100, blank=True, null=True)
    objeto = models.TextField()
    fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
    fecha_final = models.CharField(max_length=100, blank=True, null=True)
    valor = models.DecimalField(max_digits=15, decimal_places=2)
    smmlv3 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    adicion = models.DecimalField(max_digits=15, decimal_places=2, blank=True, null=True)
    part_porc = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="Part. %")
    valor_total = models.DecimalField(max_digits=15, decimal_places=2)
    smmlv4 = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contrato_no} - {self.nombre}"

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['-ANO']
