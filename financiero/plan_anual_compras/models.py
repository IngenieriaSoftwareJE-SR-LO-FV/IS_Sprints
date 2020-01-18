from django.db import models
import financiero.validaciones

# Create your models here.

class PlanAnualCompras(models.Model):
	nombre = models.CharField(max_length=100, blank=True)
	año = models.PositiveIntegerField()
	fecha = models.CharField(max_length=30, blank=True)

class Partida(models.Model):
	UNIDAD_CHOICES = [("Caja","Caja"),("Paquete","Paquete"),("Litro","Litro"),("Galón","Galón"),("Caneca","Caneca"),("Resma","Resma"),("Otros","Otros"),]
	CENTRO_COSTOS_CHOICES = [("FUNDESPOL","FUNDESPOL"), ("ESPOLTECH","ESPOLTECH"),]
	TIPO_COMPRAS_CHOICES = [("Bien","Bien"), ("Servicios","Servicios"),]
	codigo = models.CharField(max_length=15, blank=True, null=True)
	año = models.PositiveIntegerField()
	centro_costos = models.CharField(max_length=10, choices=CENTRO_COSTOS_CHOICES, blank=True, null=True)
	partida = models.CharField(max_length=200)
	tipo_compra = models.CharField(max_length=10, choices=TIPO_COMPRAS_CHOICES, blank=True, null=True)
	producto = models.CharField(max_length=200)
	cantidad_anual = models.PositiveIntegerField()
	unidad_medida = models.CharField(max_length=10 ,choices=UNIDAD_CHOICES, blank=True, null=True)
	costo_unitario = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	subtotal = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	total = models.DecimalField(max_digits=10 ,decimal_places=2, blank=True, null=True, validators=[financiero.validaciones.validate_positivo])
	pac = models.ForeignKey(PlanAnualCompras, on_delete=models.SET_NULL, blank=True, null=True)

