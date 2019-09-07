from django.db import models

# Create your models here.
class Juridica(models.Model):
	nombre = models.CharField(max_length=200)
	ruc = models.CharField(max_length=13)
	tipo_empresa = models.CharField(max_length=200)
	sector = models.CharField(max_length=200)
	direccion = models.CharField(max_length=200)
	ciudad = models.CharField(max_length=50)
	provincia = models.CharField(max_length=35)
	telefono = models.CharField(max_length=20)
	celular = models.CharField(max_length=20)
	correo = models.CharField(max_length=100)
	representante = models.CharField(max_length=250)
	maximo_facturas = models.DateField()
	forma_pago = models.CharField(max_length=100)


	contacto_cedula = models.CharField(max_length=13)
	contacto_nombres = models.CharField(max_length=75)
	contacto_apellidos = models.CharField(max_length=75)
	contacto_cargo = models.CharField(max_length=150)
	contacto_telefono = models.CharField(max_length=20)
	contacto_celular = models.CharField(max_length=20)
	contacto_correo = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre+" - "+self.ruc


