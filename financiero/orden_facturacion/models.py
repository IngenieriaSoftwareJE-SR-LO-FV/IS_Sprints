from django.db import models
from ventas.personas_juridicas.models import Juridica
from ventas.personas_naturales.models import Persona_Natural
import ventas.validaciones as val

# Create your models here.
class OrdenFacturacion(models.Model):
    class Meta:
        ordering = ['-cod_orden_fact']

    TIPO_CHOICES=[('Natural','Natural'),('Jurídica','Jurídica'),]

    tipo_cliente=models.CharField(max_length=15, choices=TIPO_CHOICES)
    cod_orden_fact=models.CharField(max_length=15, blank=True)
    n_tramite=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
    n_factura=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
    anexo_factura=models.FileField(upload_to='uploads/facturas/',blank=True, null=True)
    fecha=models.DateField()
    ruc_ci=models.CharField(max_length=13)
    razon_nombres=models.CharField(max_length=200)
    contacto=models.CharField(max_length=200)
    direccion=models.CharField(max_length=200)
    telefono=models.CharField(max_length=15)
    concepto=models.CharField(max_length=300)
    centro_costo=models.CharField(max_length=100)
    n_participantes=models.PositiveIntegerField()
    valor_total=models.FloatField(max_length=12)
    observaciones=models.CharField(max_length=500)
    comentarios=models.CharField(max_length=500, blank=True, null=True)
    estado = models.BooleanField(default=None,null=True,blank=True)
    participantes=models.ManyToManyField(Persona_Natural)


    def delete(self, *arg, **kwargs):
        self.anexo_factura.delete()
        super().delete(*arg,**kwargs)



