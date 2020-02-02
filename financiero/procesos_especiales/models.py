from django.db import models
import financiero.validaciones

# Create your models here.

class NotaCredito(models.Model):
	ESTADO_CHOICES = [("GRBD","Grabado"),("ENVD","Enviado"),("AUTR","Autorizado"),("ANLD","Anulado"),]
	FORMAPAGO_CHOICES = [("TR","Transferencia"),("CH","Cheque"),]
	PROVEEDORES_CHOICES = [("Natural", "Natural"),("Jurídica", "Jurídica"),]
	COMPROBANTE_CHOICES = [("FC","Factura"),("NV","Nota de venta"),("LC","Liquidación de compra"),("CP","Comprobantes de pago"),]
	MOTIVO_CHOICES = [("DVVL","Devolución de Valores"),]

	cod_nota_cred = models.CharField(max_length=15, blank=True, null=True)
	motivo = models.CharField(max_length=5, default="DVVL",choices=MOTIVO_CHOICES, blank=True, null=True)
	concepto = models.CharField(max_length=500, blank=True, null=True)
	estado = models.CharField(max_length=5, default="GRBD",choices=ESTADO_CHOICES, blank=True, null=True)
	documento = models.CharField(max_length=5, choices=COMPROBANTE_CHOICES, blank=True, null=True)
	n_documento = models.CharField(max_length=20, blank=True, null=True)
	evento = models.CharField(max_length=200, blank=True, null=True)
	valor_evento = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	descuento = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	valor_pagar = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	anexo = models.FileField(upload_to='uploads/nota_credito/', blank=True, null=True) 

