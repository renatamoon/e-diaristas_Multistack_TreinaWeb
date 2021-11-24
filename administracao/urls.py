from django.urls import path
from .views import servico_views, usuario_views
from django.contrib.auth import views as auth_views
from django.urls.base import reverse_lazy

urlpatterns = [
    path('servicos/cadastrar', servico_views.cadastrar_servico, name='cadastrar_servico'),
    path('servicos/listar', servico_views.listar_servicos, name='listar_servico'),
    path('servicos/editar/<int:id>', servico_views.editar_servico, name='editar_servico'),
    path('servicos/remover/<int:id>', servico_views.remover_servico, name='remover_servico'),
    path('usuarios/cadastrar', usuario_views.cadastrar_usuario, name='cadastrar_usuario'),
    path('usuarios/listar', usuario_views.listar_usuarios, name='listar_usuarios'),
    path('usuarios/editar<int:id>', usuario_views.editar_usuario, name='editar_usuario'),
    path('autenticacao/login', auth_views.LoginView.as_view(), name='logar_usuario'),
    path('autenticacao/logout', auth_views.LogoutView.as_view(), name='deslogar_usuario'),
    path('alterar_senha', auth_views.PasswordChangeView.as_view(success_url=reverse_lazy('listar_servico')),
     name='alterar_senha'),
]

#quando fazer o login com a autenticacao padrão do django, podemos redirecionar para a página que queremos
#apenas adicionando a seguinte configuração no settings.py:
#LOGIN_REDIRECT_URL = 'listar_servico'
#LOGOUT_REDIRECT_URL = 'logar_usuario' - aqui iremos deslogar e redirecionar para a pagina de logar_usuario