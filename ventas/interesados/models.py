from django.db import models

import financiero.validaciones as val_fin
import ventas.validaciones 
class CanalContacto(models.Model):
	nombre = models.CharField(max_length=75, validators=[ventas.validaciones.validate_letras])
	def __str__(self):
		return self.nombre
class Interesado(models.Model):
	nombre = models.CharField(max_length=50, validators=[ventas.validaciones.validate_letras])
	apellido = models.CharField(max_length=50, validators=[ventas.validaciones.validate_letras])
	celular = models.CharField(max_length=20, validators=[ventas.validaciones.validate_celular])
	correo = models.EmailField(max_length=100)
	canal_de_contacto = models.ForeignKey(CanalContacto, on_delete=models.SET_NULL, blank=False, null=True)
