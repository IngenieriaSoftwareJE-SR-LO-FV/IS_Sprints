from django.db import models

# Create your models here.
class OrdenIngreso(models.Model):
	class Meta:
		ordering = ['-cod_orden_ing']
      
	FORMAS_PAGO=[
		("cheque","Cheque"),
		("transferencia","Transferencia"),
		("deposito","Depósito"),
		("tarjeta","Tarjeta de Crédito"),
	]
	TARJETAS=[
		("visa","Visa"),
		("mastercard","Mastercard"),
		("american","American Express"),
		("diners","Diners"),
		("discover","Discover"),
	]
	TIPO_CHOICES=[('Natural','Natural'),('Jurídica','Jurídica'),]

	ESTADO_CHOICES = [  
        ('ACTV','Activo'),
        ('SLCE','Solicitud Enviada'),
	    ('ACPF', 'Autorizada por Financiero'),
        ('IMPE','Impreso Emitido'),
        ('RGAC','Registrado Académico'),
        ('FAES','Con factura ESPOLTECH'),
        ('ANLD','Anulada'),
	]

	tipo_cliente=models.CharField(max_length=15, choices=TIPO_CHOICES)
	fecha=models.CharField(max_length=12)
	cod_orden_ing=models.CharField(max_length=15, blank=True)
	n_tramite=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
	n_factura=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
	ruc_ci=models.CharField(max_length=13)
	razon_nombres=models.CharField(max_length=50)
	centroCosto=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	formaPago=models.CharField(max_length=30, choices=FORMAS_PAGO,default='cheque')
	valor=models.FloatField()
	anexo=models.FileField(upload_to='uploads/')
	fechaPago=models.CharField(max_length=12)
	numeroDocumento=models.PositiveIntegerField()
	banco=models.CharField(max_length=30)
	emisoraTarjeta=models.CharField(max_length=20,choices=TARJETAS, blank=True,help_text="Obligatorio con Tarjeta Crédito.")
	estado = models.CharField(max_length=5,default='ACTV',choices=ESTADO_CHOICES, blank=True, null=True)

	def delete(self, *arg, **kwargs):
		self.anexo_factura.delete()
		super().delete(*arg,**kwargs)

