from django.urls import path
from lineab.views import LineaCreate, LineaList, LineaUpdate, LineaDelete, linea_list_total
app_name = 'lineab'

urlpatterns = [
    path("registrar/", LineaCreate.as_view(), name="registrar_linea"),
    path("listar/<int:id>", LineaList.as_view(), name="listar_linea"),   
    path('listaDeLineas/', linea_list_total, name= 'lista_total'),
    path("editar/<int:pk>", LineaUpdate.as_view(), name="editar_linea"),   
    path("eliminar/<int:pk>", LineaDelete.as_view(), name="eliminar_linea"),   

]