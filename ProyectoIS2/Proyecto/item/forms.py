from django import forms

from item.models import Item

class ItemForm(forms.ModelForm):
	class Meta:
		model = Item
		fields = [
			'nombre',
			'fecha_creacion',
			'descripcion',
			'fecha_modificacion',
			'linea'
		]
		labels = {
			'nombre' : 'Nombre del Item',
			'fecha_creacion': 'Fecha Creacion',
			'descripcion': 'Descripcion',
			'fecha_modificacion': 'Fecha Modificacion',
			'linea': 'Linea Base'
		}
		widgets = {
			'nombre' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_creacion' : forms.TextInput(attrs={'class':'form-control'}),
			'descripcion' : forms.TextInput(attrs={'class':'form-control'}),
			'fecha_modificacion' : forms.TextInput(attrs={'class':'form-control'}),
			'linea' : forms.Select(attrs={'class':'form-control'})
		}