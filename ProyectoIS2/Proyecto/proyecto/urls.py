from django.urls import path
from proyecto.views import index_proyecto, ProyectoCreate, ProyectoList, ProyectoUpdate, ProyectoDelete, proyecto_list_total

app_name = 'proyecto'

urlpatterns = [
    path("", index_proyecto, name="index_proyecto"),
    path("registrar/", ProyectoCreate.as_view(), name="registrar_proyecto"),
    path("listar/<int:id>", ProyectoList.as_view(), name="proyecto_listar"),
    path('listaDeProyecto/', proyecto_list_total, name= 'lista_total'),
    path("editar/<int:pk>", ProyectoUpdate.as_view(), name="editar_proyecto"),
    path("eliminar/<int:pk>", ProyectoDelete.as_view(), name="eliminar_proyecto"),
]