from django.db import models
from ventas.personas_juridicas.models import Juridica
from ventas.personas_naturales.models import Persona_Natural
from financiero.orden_pago.models import Centro_Costos
import ventas.validaciones



# Create your models here.
ESTADO_CHOICES = [  
        ('ACTV','Activo'),
        ('SLCE','Solicitud Enviada'),
	    ('ACPF', 'Autorizada por Financiero'),
        ('IMPE','Impreso Emitido'),
        ('RGAC','Registrado Académico'),
        ('FAES','Con factura ESPOLTECH'),
        ('ANLD','Anulada'),
	]

class OrdenFacturacion(models.Model):
    class Meta:
        ordering = ['-cod_orden_fact']

    TIPO_CHOICES=[('Natural','Natural'),('Jurídica','Jurídica'),]
    

    tipo_cliente=models.CharField(max_length=15, choices=TIPO_CHOICES)
    cod_orden_fact=models.CharField(max_length=15, blank=True)
    n_tramite=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
    n_factura=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
    anexo_factura=models.FileField(upload_to='uploads/facturas/',blank=True, null=True)
    fecha=models.CharField(max_length=30)
    ruc_ci=models.CharField(max_length=13)
    razon_nombres=models.CharField(max_length=200)
    #contacto=models.CharField(max_length=200)
    #direccion=models.CharField(max_length=200)
    #telefono=models.CharField(max_length=15)
    concepto=models.CharField(max_length=300)
    centro_costos = models.ForeignKey(Centro_Costos, on_delete=models.SET_NULL, blank=False, null=True)
    n_participantes=models.PositiveIntegerField(blank=True, default=0, null=True)
    observaciones=models.CharField(max_length=500)
    comentarios=models.CharField(max_length=500, blank=True, null=True)
    estado = models.CharField(max_length=5,default='ACTV',choices=ESTADO_CHOICES, blank=True, null=True)
    #participantes=models.ManyToManyField(Persona_Natural)
    subtotal=models.FloatField(blank=True, null=True ,default=0.0)
    descuento_fact=models.FloatField(blank=True, null=True,default=0.0)
    descuento_total=models.FloatField(blank=True, null=True,default=0.0)
    valor_total=models.FloatField(max_length=12, blank=True, null=True)

    def delete(self, *arg, **kwargs):
        self.anexo_factura.delete()
        super().delete(*arg,**kwargs)


class OrdenFacturacionParticipante(models.Model):
    participante=models.ForeignKey(Persona_Natural,on_delete=models.SET_NULL, blank=False, null=True)
    nombre_evento=models.CharField(max_length=500)
    cod_evento=models.CharField(max_length=20)
    valor_evento=models.FloatField(default=0)
    descuento=models.FloatField(default=0)
    valor=models.FloatField(default=0)
    orden=models.ForeignKey(OrdenFacturacion, on_delete=models.SET_NULL, blank=True, null=True)