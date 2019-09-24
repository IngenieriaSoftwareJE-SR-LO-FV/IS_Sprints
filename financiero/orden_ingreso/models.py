from django.db import models

# Create your models here.
class OrdenIngreso(models.Model):
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
	fecha=models.CharField(max_length=12)
	numeroTramite=models.PositiveIntegerField()
	numeroFactura=models.PositiveIntegerField()
	identificacion=models.CharField(max_length=10)
	razonSocial=models.CharField(max_length=50)
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


