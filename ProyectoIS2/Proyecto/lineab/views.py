from django.shortcuts import render, redirect
from lineab.forms import LineaForm
from lineab.models import Linea_Base
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse
# Create your views here.
def linea_list_total(request):
	linea = Linea_Base.objects.all().order_by('id')
	contenido = {'lineas':linea}
	return render(request, 'lineab/listar_total_linea.html', contenido)


class LineaList(ListView):#Aca se agrega el filtro
	model = Linea_Base
	template_name = 'lineab/listar_linea.html'
	def get_queryset(self):
		return Linea_Base.objects.filter(proyecto=self.kwargs['id']).order_by('id')


class LineaCreate(CreateView):
	model = Linea_Base
	form_class = LineaForm
	template_name = 'lineab/linea_form.html'
	success_url = reverse_lazy('lineab:lista_total' )
	

class LineaUpdate(UpdateView):
	model = Linea_Base
	form_class = LineaForm
	template_name = 'lineab/linea_form.html'
	success_url = reverse_lazy('lineab:lista_total')


class LineaDelete(DeleteView):
	model = Linea_Base
	template_name = 'lineab/linea_delete.html'
	success_url = reverse_lazy('lineab:lista_total')