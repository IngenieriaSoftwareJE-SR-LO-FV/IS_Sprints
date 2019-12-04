from django.db import models
from financiero.orden_facturacion.models import OrdenFacturacion
import financiero.validaciones as val_fin
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
	orden_facturacion = models.ForeignKey(OrdenFacturacion, on_delete=models.SET_NULL, blank=False, null=True)
	razon_nombres=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	formaPago=models.CharField(max_length=30, choices=FORMAS_PAGO,default='cheque')
	valor=models.DecimalField(max_digits=15,decimal_places=3,validators=[val_fin.validate_positivo])
	anexo=models.FileField(upload_to='uploads/', blank=True)
	fechaPago=models.CharField(max_length=12)
	numeroDocumento=models.PositiveIntegerField()
	banco=models.CharField(max_length=30)
	emisoraTarjeta=models.CharField(max_length=20,choices=TARJETAS, blank=True)

	def delete(self, *arg, **kwargs):
		self.anexo.delete()
		super().delete(*arg,**kwargs)

