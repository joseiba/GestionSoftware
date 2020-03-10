from django.shortcuts import render, redirect
from usuario.forms import UserForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

# Create your views here.
def index_usuario(request):
	return render(request, "usuario/index.html")
'''
def usuario_create(request):
	if request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('usuario:listar_usuario')
	else:
		form = UserForm()
	return render(request, 'usuario/usuario_form.html', {'form':form})


def usuario_list(request):
	usuario = User.objects.all()
	contenido = {'usuarios':usuario}
	return render(request, 'usuario/listar_usuario.html', contenido)	
'''


class UsuarioList(ListView):
	model = User
	template_name = 'usuario/listar_usuario.html'

class UsuarioCreate(CreateView):
	model = User
	template_name = 'usuario/usuario_form.html'
	form_class = UserForm	
	success_url = reverse_lazy('usuario:listar_usuario')


class UsuarioUpdate(UpdateView):
	model = User
	form_class = UserForm
	template_name = 'usuario/usuario_form.html'
	success_url = reverse_lazy('usuario:listar_usuario')


class UsuarioDelete(DeleteView):
	model = User
	template_name = 'usuario/usuario_delete.html'
	success_url = reverse_lazy('usuario:listar_usuario')


def usuario_edit(request, id_usu):
	usuario = User.objects.get(id = id_usu)
	registered = False
	if request.method == 'GET' :
		form = UserForm(instance=usuario)
	else:
		form = UserForm(request.POST, instance=usuario)	
		if form.is_valid():
			form.save()
		return redirect('usuario:usuario_listar')
	return render(request,'usuario/usuario_form.html', {'form':form})
