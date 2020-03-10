from django import forms
from usuario.models import Usuario
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
class UserForm(UserCreationForm):
	class Meta:
		model = User       
		fields = [
				'first_name',
				'last_name',
				'username',
				'email',
			]
		labels = {
				'first_name' : 'Nombre',
				'last_name' : 'Apellido',
				'username' : 'Nombre de usuario',
				'email' : 'Correo Electronico',
		}     

		help_texts = {
					'username' : None,
					'password2' : None,
					} 


'''
class UserProfileInfoForm(forms.ModelForm):
	class Meta:
		model = Usuario
		fields = ['proyecto']

		labels = {'proyecto' : 'Proyecto'}

		widget = {'proyecto' : forms.Select(attrs={'class':'form-control'})}
'''