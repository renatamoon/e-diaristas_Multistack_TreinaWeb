from django.shortcuts import redirect, render
from .forms import ServicoForm
from .models import Servico

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
    return render(request, 'servicos/form_servico.html', {'form_servico': form_servico})

def listar_servicos(request):
    servicos = Servico.objects.all() #fazendo uma consulta de todos os serviços e salvando na variavel servicos
    return render(request, 'servicos/lista_servicos.html', {'servicos': servicos})

def editar_servico(request, id):
    servico = Servico.objects.get(id=id)
    form_servico = ServicoForm(request.POST or None, instance=servico)
    #a instancia do nosso servico form venha com todos os servicos já preenchidos
    if form_servico.is_valid():
        form_servico.save()
        return redirect('listar_servico')
    return render(request, 'servicos/form_servico.html', {'form_servico': form_servico})

def remover_servico_db(servico):
    servico.delete()    

def remover_servico(request, id):
    servico = Servico.objects.get(id=id)
    form_servico = ServicoForm(request.POST or None, instance=servico)
    if request.method == 'POST':
        remover_servico_db(servico)
        return redirect('listar_servico')
    return render(request, 'servicos/confirma_exclusao.html', {'form_servico': form_servico})
