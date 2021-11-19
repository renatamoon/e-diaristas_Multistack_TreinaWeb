from django.shortcuts import render
from .forms import ServicoForm

# Create your views here.

def cadastrar_servico(request):
    if request.method == "POST":
        form_servico = ServicoForm(request.POST)
        #tenhamos uma instancia do nosso ServicoForm com base nas informacoes que pegamos dentro do formulario (metodo POST)
        if form_servico.is_valid(): #verifica se todos os campos satisfazem as regras que definimos dentro do nosso models.py
            form_servico.save() #salvando as infos dentro do banco de dados
    else:
        #se o metodo nao for post, significa que estamos apenas abrindo a nossa pagina
        form_servico = ServicoForm()
    return render(request, 'servicos/form_servico.html', {"form_servico": form_servico})