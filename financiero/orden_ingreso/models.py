from django.db import models

# Create your models here.
class OrdenIngreso(models.Model):
	class Meta:
		ordering = ['-cod_orden_ing']

	FORMAS_PAGO=[
		("Cheque","Cheque"),
		("Transferencia","Transferencia"),
		("Depósito","Depósito"),
		("Tarjeta de Crédito","Tarjeta de Crédito"),
	]
	TARJETAS=[
		("Visa","Visa"),
		("Mastercard","Mastercard"),
		("American Express","American Express"),
		("Diners","Diners"),
		("Discover","Discover"),
	]
	TIPO_CHOICES=[('Natural','Natural'),('Jurídica','Jurídica'),]

	
	cod_orden_ing=models.CharField(max_length=15, blank=True)
	tipo_cliente=models.CharField(max_length=15, choices=TIPO_CHOICES)
	fecha=models.CharField(max_length=12)
	n_tramite=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
	n_factura=models.CharField(max_length=15,blank=True, null=True, default='No asignado')
	ruc_ci=models.CharField(max_length=13)
	razon_nombres=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	formaPago=models.CharField(max_length=30, choices=FORMAS_PAGO,default='cheque')
	valor=models.FloatField()
	anexo=models.FileField(upload_to='uploads/', blank=True)
	fechaPago=models.CharField(max_length=12)
	numeroDocumento=models.PositiveIntegerField()
	banco=models.CharField(max_length=30)
	emisoraTarjeta=models.CharField(max_length=20,choices=TARJETAS, blank=True)

	def delete(self, *arg, **kwargs):
		self.anexo.delete()
		super().delete(*arg,**kwargs)

