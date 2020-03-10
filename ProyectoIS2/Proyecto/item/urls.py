from django.urls import path
from item.views import ItemCreate, ItemList, ItemUpdate, ItemDelete, item_list_total
app_name = 'item'

urlpatterns = [
    path("registrar/", ItemCreate.as_view(), name="registrar_item"),
    path("listar/<int:id>", ItemList.as_view(), name="listar_item"),   
    path('listaDeItem/', item_list_total, name= 'lista_total'),
    path("editar/<int:pk>", ItemUpdate.as_view(), name="editar_item"),   
    path("eliminar/<int:pk>", ItemDelete.as_view(), name="eliminar_item"),   

]