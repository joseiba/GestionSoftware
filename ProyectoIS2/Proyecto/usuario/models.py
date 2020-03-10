from django.db import models
from proyecto.models import Proyecto
from django.contrib.auth.models import User
# Create your models here.

class Usuario(models.Model):
	usuario = models.OneToOneField(User,on_delete=models.CASCADE)
	#perfil_redes = models.URLField(blank=True)
	proyecto = models.ForeignKey(Proyecto, null=True, blank=True, on_delete=models.CASCADE)
	def __str__(self):
  		return self.usuario.username