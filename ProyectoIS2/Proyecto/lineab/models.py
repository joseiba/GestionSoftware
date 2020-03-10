from django.db import models
from  proyecto.models import Proyecto
# Create your models here.

class Linea_Base (models.Model):
	nombre_linea= models.CharField(max_length=300)
	HABILITADA = 'HAB'
	BLOQUEADA = 'BLO' 
	FINALIZADO = 'FIN'  
	tipo_estado = ((HABILITADA, 'Habilitada'),
				(BLOQUEADA, 'Bloqueada'),
				(FINALIZADO,'Finalizado'))
	estado =  models.CharField(max_length=15, choices = tipo_estado, default = HABILITADA)
	proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):	
		return self.nombre_linea