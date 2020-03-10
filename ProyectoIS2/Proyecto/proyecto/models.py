from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Proyecto (models.Model):
	nombre = models.CharField(max_length=200)
	objetivo = models.CharField(max_length=300)
	fecha_ini = models.DateField()
	fecha_limite = models.DateField()
	cant_dias_atrasados = models.IntegerField(default=0)
	vence = 'NO'
	vence_mes = models.CharField(max_length=3, default=vence)
	ACTIVO ='ACT'
	BLOQUEADO='BLO'
	FINALIZADO='FIN'
	tipo_estado=((ACTIVO, 'Activo'),
				(BLOQUEADO, 'Bloqueado'),
				(FINALIZADO, 'Finalizado'))
	estado = models.CharField(max_length=15, choices = tipo_estado, default = ACTIVO) 
	ANALISIS = 'ANA'
	DISENHO = 'DIS'
	CODIFICACION = 'COD'
	PRUEBA = 'PRU'
	MANTENIMIENTO = 'MAN'
   
	tipo_fase = ((ANALISIS, 'Analisis'),
				(DISENHO, 'Diseño'),
				(CODIFICACION, 'Codificacion'),
				(PRUEBA, 'Prueba'),
				(MANTENIMIENTO, 'Mantenimiento'))
	fase =  models.CharField(max_length=15, choices = tipo_fase, default = ANALISIS)
	usu = models.ForeignKey(User, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
		return self.nombre