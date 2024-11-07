from django.db import models

class Contrato(models.Model):
    ANO = models.CharField(max_length=4, blank=True, null=True)  # cambiado a CharField
    contrato_no = models.CharField(max_length=100, blank=True, null=True)
    tipo_de_contrato = models.CharField(max_length=100, blank=True, null=True)
    nombre = models.CharField(max_length=255, blank=True, null=True)
    entidad = models.CharField(max_length=255, blank=True, null=True)
    rup = models.CharField(max_length=100, blank=True, null=True)
    contrato = models.CharField(max_length=100, blank=True, null=True)
    smmlv = models.CharField(max_length=20, blank=True, null=True)
    secop = models.CharField(max_length=100, blank=True, null=True)
    contrato2 = models.CharField(max_length=100, blank=True, null=True)
    acta_inicial = models.CharField(max_length=100, blank=True, null=True)
    acta_final = models.CharField(max_length=100, blank=True, null=True)
    objeto = models.TextField(blank=True, null=True)
    fecha_inicio = models.CharField(max_length=100, blank=True, null=True)
    fecha_final = models.CharField(max_length=100, blank=True, null=True)
    valor = models.CharField(max_length=20, blank=True, null=True)
    smmlv3 = models.CharField(max_length=20, blank=True, null=True)
    adicion = models.CharField(max_length=20, blank=True, null=True)
    part_porc = models.CharField(max_length=10, blank=True, null=True, verbose_name="Part. %")
    valor_total = models.CharField(max_length=20, blank=True, null=True)
    smmlv4 = models.CharField(max_length=20, blank=True, null=True)
    is_visible = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.contrato_no} - {self.nombre}"

    class Meta:
        verbose_name = "Contrato"
        verbose_name_plural = "Contratos"
        ordering = ['-ANO']
