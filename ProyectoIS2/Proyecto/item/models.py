from django.db import models

# Create your models here.
from  lineab.models import Linea_Base
class Item (models.Model):
	nombre = models.CharField(max_length=50)
	fecha_creacion = models.DateField()
	descripcion = models.CharField(max_length=100)
	fecha_modificacion= models.DateField(null=True, blank=True)
	linea = models.ForeignKey(Linea_Base, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre