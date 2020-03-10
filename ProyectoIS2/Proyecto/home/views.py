from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def index_portal(request):
	return render(request,'login/login.html')
@login_required
def special(request):
	return HttpResponse("You are logged in !")
@login_required
def user_logout(request):
	logout(request)
	return HttpResponseRedirect(reverse('portal'))

def user_login(request):
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		usuario = authenticate(username=username, password=password)
		if usuario is not None:
			if usuario.is_active:
				login(request, usuario)
				return redirect('proyecto:index_proyecto')
			else:
				messages.error(request,'Tu usuario esta inactivo')
				return render(request, 'login/login.html')
		else:
			messages.error(request,'El nombre de usuario y/o contraseña son incorrectos')
			return render(request, 'login/login.html')
	else:
		return render(request, 'login/login.html')