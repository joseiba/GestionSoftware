from django.urls import path
from usuario.views import index_usuario, UsuarioCreate, UsuarioList,UsuarioUpdate,UsuarioDelete

app_name = 'usuario'

urlpatterns = [
    path("", index_usuario, name="index_usuario"),
    path("registrar/", UsuarioCreate.as_view(), name="registrar_usuario"),
    path("editar/<int:pk>", UsuarioUpdate.as_view(), name="usuario_editar"),   
    path("eliminar/<int:pk>", UsuarioDelete.as_view(), name="usuario_eliminar"),   
    path("listar/", UsuarioList.as_view(), name="listar_usuario"),
    
]