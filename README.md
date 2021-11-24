# e-diaristas_Multistack_TreinaWeb
<i>E-CLEANER PLATFORM</i>

<p align="center">
  <a href="#projeto">Sobre o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#tecnologias">Tecnologias utilizadas</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#instalacao">Como Executar o projeto</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp; 
  <a href="#links_apps">Links Úteis</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
  <a href="#imagens">Algumas Imagens</a>&nbsp;&nbsp;&nbsp;|&nbsp;&nbsp;&nbsp;
 
</p>

## <a id="projeto"> 💻 SOBRE ESTE PROJETO </a>

> 🟩 Status do projeto: EM ANDAMENTO ... <br>
> 🟥 <b>EXECUTÁVEL APENAS A PARTE DE ADMINISTRAÇÃO DO DJANGO ...</b>


Desenvolvimento progressivo do projeto de uma plataforma chamada E-diaristas que ajudará a encontrar o melhor profissional de limpeza com segurança e praticidade. No Painel Administrativo, podemos cadastrar, deletar, editar, listar e visualizar todos os dados da aplicação. 
O projeto ainda está em fase de desenvolvimento, juntamente com a TreinaWeb.<br>

<hr>
  
  ## <a id="tecnologias"> 🧪 TECNOLOGIAS QUE SERÃO UTILIZADAS </a>

Tecnologias que serão usadas neste projeto de E-diaristas:

![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Next.js](https://img.shields.io/badge/next.js-000000?style=for-the-badge&logo=next-dot-js&logoColor=white)
![Typescript](https://img.shields.io/badge/TypeScript-007ACC?style=for-the-badge&logo=typescript&logoColor=white)

Desenvolvimento da parte de Administração:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=green)
![Bootstrap](https://img.shields.io/badge/Bootstrap-563D7C?style=for-the-badge&logo=bootstrap&logoColor=white)
![JQuery](https://img.shields.io/badge/jQuery-0769AD?style=for-the-badge&logo=jquery&logoColor=white)
![Bower version](https://img.shields.io/bower/v/adminlte.svg)

<hr>

## <a id="instalacao"> 🔴 PASSO A PASSO DE COMO EXECUTAR A APLICAÇÃO </a> 

*No Windows:

<b>-Clone o repositório com o camando:</b> `git clone https://github.com/renatamoon/e-diaristas_Multistack_TreinaWeb.git` <br>
<b>-Criando virtual environment:</b> `python -m venv venv`<br>
<b>-Ativando o virtual environment: </b>`. venv\Scripts\Activate.ps1`<br>
<b>Obs: Caso ocorra um erro na ativação:</b> entre no powershell e digite o seguinte comando: `Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy RemoteSigned`<br>
<b>-Execução do arquivo requirements: </b>`pip install -r requirements.txt`<br>

*No Linux:

<b>-Baixe o repositorio<br>
<b>-Criando virtual environment:</b> `virtualenv venv`<br>
<b>-Ativando o virtual environment:</b> `. venv/bin/activate`<br>
<b>-Execução do arquivo requirements e instalar dependencias:</b> `pip install -r requirements.txt`<br>
  
 <hr> 
  
*Alterar as configurações do DataBase no arquivo <b>`settings.py`</b> <br>

```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'HOST': 'host_bd',
        'PORT': 'porta_bd',
        'NAME': 'ediaristas',
        'USER': 'usuario_bd',
        'PASSWORD': 'senha_bd'    
    }
}
```

 *Migre o banco de dados com: `python manage.py migrate` <br>
 *Execute o servidor: `python manage.py runserver` <br>
  
<hr>

## <a id="links_apps"> 🔴 LINKS ÚTEIS </a> 

*USANDO CDN - jquery.mask - A jQuery Plugin to make masks on form fields and html elements.<br>
<br>
https://cdnjs.com/libraries/jquery.mask/1.11.2<br>
<br>
*USANDO O ADMINLTE - Bootstrap Admin Dashboard Template<br>
<br>
https://adminlte.io/<br>
  
<hr>

## <a id="imagens"> 🔴 ALGUMAS IMAGENS DO PROJETO ATÉ AGORA: </a> 

- Visual da Página de Administração do AdminLTE com Django + Bootstrap:<br>
  -Conseguimos entrar nos links da Nav side bar e também links criados para a HOME do Admin que é a lista de cleaners.<br>
  -Funcionalidaes de Edição e Remoção de cleaners cadastradas ok;
  
  ![image](https://user-images.githubusercontent.com/87100340/143248789-506d6e42-0a78-4f0b-a1e7-8c1d2d8b8780.png)

- Página de Cadastro de Usuários ainda sem modelos de autenticação:
  
 ![image](https://user-images.githubusercontent.com/87100340/143249535-c0504540-0e00-42f2-bb57-cf69cd4f022d.png)
   
- Página de listagem de Usuários:<br>
  -Funcionalidades criadas: cadastrar usuário com forms;
  
  ![image](https://user-images.githubusercontent.com/87100340/143249093-deccdebe-eea9-48f2-bc3c-35bbea494426.png)
