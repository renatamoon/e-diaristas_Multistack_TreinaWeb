from django.urls import path
from .views import servico_views, usuario_views

urlpatterns = [
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servico_views.listar_servicos, name='listar_servico'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('servicos/remover/<int:id>', servico_views.remover_servico, name='remover_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar_usuarios'),
]