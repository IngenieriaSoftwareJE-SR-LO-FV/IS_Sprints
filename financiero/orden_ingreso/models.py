from django.db import models

# Create your models here.
class OrdenIngreso(models.Model):
	fecha=models.CharField(max_length=12)
	numeroTramite=models.PositiveIntegerField()
	numeroFactura=models.PositiveIntegerField()
	identificacion=models.CharField(max_length=10)
	razonSocial=models.CharField(max_length=50)
	centroCosto=models.CharField(max_length=50)
	descripcion=models.CharField(max_length=150)
	valor=models.FloatField()
	anexo=models.FileField(upload_to='uploads/')


