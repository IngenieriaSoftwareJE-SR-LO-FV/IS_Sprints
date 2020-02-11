from django.db import models

# Create your models here.

"""class Lista_Rubros(models.Model):
	nombre = models.CharField(max_length=50)
	def __str__(self):
		return self.nombre"""

class Centro_Costos(models.Model):
	nombre = models.CharField(max_length=10)

	def __str__(self):
		return self.nombre


class Egresos(models.Model):
	codigo = models.CharField(max_length=15)
	nombre = models.CharField(max_length=200)
	centroc = models.ForeignKey(Centro_Costos, on_delete=models.CASCADE)

	def __str__(self):
		return self.nombre


class OrdenPago(models.Model):
	ESTADO_CHOICES = [("GRBD","Grabado"),("ENVD","Enviado"),("AUTR","Autorizado"),("ANLD","Anulado"),("PGDO","Pagado")]
	FORMAPAGO_CHOICES = [("TR","Transferencia"),("CH","Cheque"),]
	PROVEEDORES_CHOICES = [("Natural", "Natural"),("Jurídica", "Jurídica"),]
	COMPROBANTE_CHOICES = [("FC","Factura"),("NV","Nota de venta"),("LC","Liquidación de compra"),("CP","Comprobantes de pago"),]

	cod_ord_pago = models.CharField(max_length=15, blank=True, null=True)
	n_tramite = models.CharField(max_length=15, blank=True, null=True)
	fecha = models.CharField(max_length=30)
	fecha_tramite = models.CharField(max_length=30)
	fecha_pago = models.CharField(max_length=30)
	estado = models.CharField(max_length=5, default="GRBD",choices=ESTADO_CHOICES, blank=True, null=True)
	tipo_proveedor = models.CharField(max_length=10, choices=PROVEEDORES_CHOICES, blank=False, null=True)
	proveedor = models.CharField(max_length=200)
	centro_costos = models.ForeignKey(Centro_Costos, on_delete=models.SET_NULL, blank=False, null=True)
	egreso = models.ForeignKey(Egresos, on_delete=models.SET_NULL, blank=False, null=True)
	tipo_comprobante = models.CharField(max_length=5, choices=COMPROBANTE_CHOICES, blank=False, null=True)
	n_comprobante = models.CharField(max_length=20, blank=True, null=True)
	concepto = models.CharField(max_length=500)
	forma_pago = models.CharField(max_length=5, choices=FORMAPAGO_CHOICES, blank=False, null=True)
	observacion = models.CharField(max_length=500, blank=True, null=True)
	documentos=models.CharField(max_length=500, blank=True, null=True)
	anexo = models.FileField(upload_to='uploads/orden_pago/', blank=True, null=True)
	motivo_anular = models.CharField(max_length=500, blank=True, null=True)
	

	def __str__(self):
		return self.cod_ord_pago

	def delete(self, *arg, **kwargs):
		self.anexo.delete()
		super().delete(*arg,**kwargs)


"""class Rubro(models.Model):
	orden_pago = models.ForeignKey(OrdenPago, on_delete=models.SET_NULL, blank=True, null=True)
	#nombre_rubro = models.ForeignKey(Lista_Rubros, on_delete=models.SET_NULL, blank=True, null=True)
	cod_evento = models.CharField(max_length=15)
	act_prod = models.CharField(max_length=50)
	c_c = models.PositiveIntegerField()
	subtotal = models.DecimalField(decimal_places=2)
	iva = models.DecimalField(decimal_places=2)
	otros_cargos = models.DecimalField(decimal_places=2)
	total = models.DecimalField(decimal_places=2)
	centro_costos = models.CharField(max_length=100)

	def __str__(self):
		return self.cod_evento+" - "+self.act_prod"""