from django.db import models
from ventas.personas_juridicas.models import Juridica
from ventas.personas_naturales.models import Persona_Natural

# Create your models here.
class OrdenFacturacion(models.Model):
    TIPO_CHOICES=[('p_natural','Natural'),('p_juridica','Jurídica')]
    cod_orden_fact=models.CharField(max_length=10, primary_key=True)
    tipo_cliente=models.CharField(max_length=10, choices=TIPO_CHOICES)
    n_tramite=models.PositiveIntegerField(blank=True, null=True)
    n_factura=models.PositiveIntegerField(blank=True, null=True)
    anexo_factura=models.FileField(upload_to='uploads/facturas/',blank=True, null=True)
    fecha=models.DateField()
    ruc_ci=models.CharField(max_length=13)
    razon_nombres=models.CharField(max_length=200)
    contacto=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=15)
    concepto=models.CharField(max_length=300)
    centro_costo=models.CharField(max_length=100)
    n_participantes=models.PositiveIntegerField(blank=True, null=True)
    valor_total=models.FloatField(max_length=10)
    observaciones=models.CharField(max_length=500)
    comentarios=models.CharField(max_length=500, blank=True, null=True)
    participantes=models.ManyToManyField(Persona_Natural, blank=True)

    def delete(self, *arg, **kwargs):
        self.anexo_factura.delete()
        super().delete(*arg,**kwargs)



