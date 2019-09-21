from django.db import models
from ventas.reporte_contacto.models import ReporteContacto
from ventas.personas_juridicas.models import Juridica
from multiselectfield import MultiSelectField

# Create your models here.
class PropuestaCorporativo(models.Model):
    TIPO_EMPRESA_CHOICES=   [
                                ('PB','Pública'),
                                ('IN','Industriales'),
                                ('CO','Comerciales'),
                                ('PR','Privadas'),
                            ]

    ESTADO_CHOICES= [
                        ('SG','Seguimiento'),
                        ('PD','Pendiente'),
                        ('ACP','Aceptada'),
                        ('NACP','No aceptada'),
                    ]

    SERVICIOS_CHOICES=  [
                            ('CBR','Coffe Break'),
                            ('ALM','Almuerzo'),
                            ('MIP','Material impreso'),
                            ('MDG','Material digital'),
                        ]

    cod_propuesta=models.CharField(max_length=20, primary_key=True)
    version=models.PositiveIntegerField()
    nombre_propuesta=models.CharField(max_length=250)
    tipo_empresa=models.CharField(max_length=50,
                                    choices=TIPO_EMPRESA_CHOICES,
                                    default='PR')
    reporte=models.ForeignKey(ReporteContacto, on_delete=models.SET_NULL, null=True, blank=True)
    estado=models.CharField(max_length=15,
                            choices=ESTADO_CHOICES,
                            default='SG')
    empresa=models.ForeignKey(Juridica, on_delete=models.SET_NULL, null=True, blank=True)
    sector=models.CharField(max_length=25)
    fecha_solicitud=models.CharField(max_length=12)
    numero_participantes=models.PositiveIntegerField()
    total_horas=models.TimeField()
    cantidad_cursos=models.PositiveIntegerField()
    monto_propuesta=models.FloatField()
    margen_contribucion=models.FloatField( max_length=3)
    utilidad_esperada=models.FloatField()
    exito=models.FloatField( max_length=4)
    lugar=models.CharField(max_length=25)
    servicios_incluidos=MultiSelectField(choices=SERVICIOS_CHOICES,
                                            blank=True,
                                            null=True)
    fecha_inicio_estimada=models.CharField(max_length=12)
    observacion=models.CharField(max_length=250,blank=True,null=True)
    anexo=models.FileField(upload_to='uploads/',blank=True, null=True)
    nombre=models.CharField(max_length=50)

    def delete(self, *arg, **kwargs):
        self.anexo.delete()
        super().delete(*arg,**kwargs)
