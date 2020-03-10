from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from proyecto.forms import ProyectoForm
from proyecto.models import Proyecto
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from datetime import datetime, timedelta, date
# Create your views here.
def index_proyecto(request):
	for proy in Proyecto.objects.exclude(fecha_limite__gt=datetime.now()):
		fecha_ahora = date.today()
		fecha_prov = fecha_ahora - proy.fecha_limite
		proy.cant_dias_atrasados = int(fecha_prov.days)
		proy.save()
	proyecto = Proyecto.objects.exclude(fecha_limite__gt=datetime.now()).order_by('id')
	
	cantidad = 0
	for proy in Proyecto.objects.all():
		if (proy.fecha_limite.day > date.today().day and proy.fecha_limite.month == date.today().month and proy.fecha_limite.year == date.today().year):
			cantidad = cantidad + 1
			proy.vence_mes ='SI'
			proy.save()
	contenido = {'proyectos':proyecto,'cantidad':cantidad}
	return render(request, 'proyecto/index.html', contenido)
'''
def registrar_proyecto(request):	
	if request.method == 'POST':
		form = ProyectoForm(request.POST)
		if form.is_valid():
			form.save()
		return redirect('proyecto:listar_proyecto')
	else:
		form = ProyectoForm()
	return render(request, 'proyecto/proyecto_form.html', {'form':form})
'''
def proyecto_list_total(request):
	proyecto = Proyecto.objects.all().order_by('id')
	contenido = {'proyectos':proyecto}
	return render(request, 'proyecto/lista_total_proyecto.html', contenido)


class ProyectoList(ListView):
	model = Proyecto
	template_name = 'proyecto/listar_proyecto.html'
	def get_queryset(self):
		return Proyecto.objects.filter(usu=self.kwargs['id']).order_by('id')

class ProyectoCreate(CreateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:lista_total')	

class ProyectoUpdate(UpdateView):
	model = Proyecto
	form_class = ProyectoForm
	template_name = 'proyecto/proyecto_form.html'
	success_url = reverse_lazy('proyecto:lista_total')


class ProyectoDelete(DeleteView):
	model = Proyecto
	template_name = 'proyecto/proyecto_delete.html'
	success_url = reverse_lazy('proyecto:lista_total')	