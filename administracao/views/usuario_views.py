from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render

#usaremos o sistema de autenticação do proprio django
def cadastrar_usuario(request):
    #formulario já aumtomatico do Django para cadastro de usuários
    form_usuario = UserCreationForm(request.POST)
    if form_usuario.is_valid():
        form_usuario.save()
    else: #se o metodo não for POST saberemos que temos que renderizar um form vazio
        form_usuario = UserCreationForm()
    return render(request, 'usuarios/form_usuario.html', {'form_usuario': form_usuario})
