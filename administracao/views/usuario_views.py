from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import render

#usaremos o sistema de autenticação do proprio django
def cadastrar_usuario(request):
    #formulario já aumtomatico do Django para cadastro de usuários // nao transforma em super usário
    form_usuario = UsuarioForm(request.POST)
    if form_usuario.is_valid():
        form_usuario.save()
    else: #se o metodo não for POST saberemos que temos que renderizar um form vazio
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})
