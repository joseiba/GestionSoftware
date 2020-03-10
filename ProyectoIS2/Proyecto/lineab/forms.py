from django import forms
from lineab.models import Linea_Base

class LineaForm(forms.ModelForm):
	class Meta:
		model = Linea_Base
		fields = [
            'nombre_linea',
			'estado',
			'proyecto'
		]
		labels = {
            'nombre_linea':'Nombre de la Linea Base',
			'estado': 'Estado',
			'proyecto': 'Proyecto'
			
		}
		widgets = {
            'nombre_linea' : forms.TextInput(attrs={'class':'form-control'}),
			'estado' : forms.Select(attrs={'class':'form-control'}),
			'proyecto' : forms.Select(attrs={'class':'form-control'})
		}
