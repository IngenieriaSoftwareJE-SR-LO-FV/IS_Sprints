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

	tipo_cliente=models.CharField(max_length=15, choices=TIPO_CHOICES)
	fecha=models.CharField(max_length=12)
	cod_orden_ing=models.CharField(max_length=15, blank=True)
	numeroTramite=models.PositiveIntegerField()
	numeroFactura=models.PositiveIntegerField()
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
	estado=models.BooleanField(default=None,null=True,blank=True)

	def delete(self, *arg, **kwargs):
		self.anexo_factura.delete()
		super().delete(*arg,**kwargs)

