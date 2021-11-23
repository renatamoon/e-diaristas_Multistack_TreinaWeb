from ..forms.usuario_forms import UsuarioForm
from django.shortcuts import redirect, render
from django.contrib.auth import get_user_model

#usaremos o sistema de autenticação do proprio django
def cadastrar_usuario(request):
    if request.method == 'POST':
    #formulario já aumtomatico do Django para cadastro de usuários // nao transforma em super usário
        form_usuario = UsuarioForm(request.POST)
        if form_usuario.is_valid():        
            form_usuario.save()
            return redirect('listar_usuarios')
    else: #se o metodo não for POST saberemos que temos que renderizar um form vazio
        form_usuario = UsuarioForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})

def listar_usuarios(request):
    User = get_user_model() #pegando o model de autenticacao do proprio django para renderizar e listar
    usuarios = User.objects.filter(is_superuser=True)
    return render(request, 'usuarios/lista_usuarios.html', {'usuarios': usuarios})
