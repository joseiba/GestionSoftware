from django import forms

from proyecto.models import Proyecto

class ProyectoForm(forms.ModelForm):
	class Meta:
		model = Proyecto
		fields = [
			'nombre',
			'objetivo',
			'fecha_ini',
			'fecha_limite',
			'estado',
			'fase',
            'usu',
			
		]
		labels = {
			'nombre' : 'Nombre Proyecto',
			'objetivo' : 'Objetivo',
			'fecha_ini': 'Fecha Inicial',
			'fecha_limite': 'Fecha Limite',
			'estado': 'Estado',
			'fase':'Fase',
            'usu':'Usuario',
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'objetivo' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_ini' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_limite' : forms.TextInput(attrs={'class':'form-control'}),
			'estado' : forms.Select(attrs={'class':'form-control'}),
			'fase' : forms.Select(attrs={'class':'form-control'}),
            'usu' : forms.Select(attrs={'class':'form-control'}),
		}