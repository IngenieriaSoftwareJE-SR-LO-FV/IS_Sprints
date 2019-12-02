from django.db import models
import ventas.validaciones

class Provincia(models.Model):
	nombre = models.CharField(max_length=50,verbose_name="Provincia")
	def __str__(self):
		return self.nombre


class Ciudad(models.Model):
	provincia=models.ForeignKey(Provincia, on_delete=models.CASCADE)
	nombre = models.CharField(max_length=50,verbose_name="Ciudad")
	def __str__(self):
		return self.nombre

class TipoEmpresa(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Tipo de Empresa")
	def __str__(self):
		return self.nombre

class Sector(models.Model):
	nombre = models.CharField(max_length=100,verbose_name="Sector")
	def __str__(self):
		return self.nombre

class FormaPago(models.Model):
	nombre = models.CharField(max_length=100, verbose_name="Forma de Pago")
	def __str__(self):
		return self.nombre

class Juridica(models.Model):
	nombre = models.CharField(max_length=200)
	ruc = models.CharField(max_length=13, primary_key=True, validators=[ventas.validaciones.validate_ruc])
	tipo_empresa = models.ForeignKey(TipoEmpresa,on_delete=models.SET_NULL, null=True)
	sector = models.ForeignKey(Sector,on_delete=models.SET_NULL, null=True)
	direccion = models.CharField(max_length=200)
	ciudad = models.CharField(max_length=50)
	provincia = models.ForeignKey(Provincia, on_delete=models.SET_NULL, null=True)
	ciudad = models.ForeignKey(Ciudad, on_delete=models.SET_NULL, null=True)
	telefono = models.CharField(max_length=20, validators=[ventas.validaciones.validate_fono_convencional])
	celular = models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular])
	correo = models.CharField(max_length=100)
	representante = models.CharField(max_length=250)
	maximo_facturas = models.DateField()
	forma_pago = models.ForeignKey(FormaPago, on_delete=models.SET_NULL, null=True)


	contacto_cedula = models.CharField(max_length=13, validators=[ventas.validaciones.validate_cedula])
	contacto_nombres = models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras])
	contacto_apellidos = models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras])
	contacto_cargo = models.CharField(max_length=150)
	contacto_telefono = models.CharField(max_length=20, validators=[ventas.validaciones.validate_fono_convencional])
	contacto_celular = models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular])
	contacto_correo = models.CharField(max_length=100)

	def __str__(self):
		return self.nombre+" - "+self.ruc






