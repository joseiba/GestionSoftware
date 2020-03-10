from django.shortcuts import render, redirect
from django.http import HttpResponse
from item.forms import ItemForm
from item.models import Item
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.contrib import messages 
from django.contrib.messages.views import SuccessMessageMixin 
from django.urls import reverse

# Create your views here.
def item_list_total(request):
	item = Item.objects.all().order_by('id')
	contenido = {'items':item}
	return render(request, 'item/listar_total_item.html', contenido)


class ItemList(ListView):
	model = Item
	template_name = 'item/listar_item.html'
	paginate_by = 10
	def get_queryset(self):
		return Item.objects.filter(linea=self.kwargs['id']).order_by('id')

class ItemCreate(CreateView):
	model = Item
	form_class = ItemForm
	template_name = 'item/item_form.html'
	success_url = reverse_lazy('item:lista_total')


class ItemUpdate(UpdateView):
	model = Item
	form_class = ItemForm
	template_name = 'item/item_form.html'
	success_url = reverse_lazy('item:lista_total')


class ItemDelete(DeleteView):
	model = Item
	template_name = 'item/item_delete.html'
	success_url = reverse_lazy('item:lista_total')

