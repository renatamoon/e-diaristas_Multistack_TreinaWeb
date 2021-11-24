
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model


#transformar os usuarios a partir do Usuarioform em superuser
class UsuarioForm(UserCreationForm):
    class Meta: #definir meta atributos
        model = get_user_model()
        fields = ['username', 'first_name', 'email', 'password1', 'password2']
        #para que o formulário seja valido, precisa desses campos acima dentro do formulario

    def save(self, commit=True): #persistindo as infos no banco de dados
        user = super(UserCreationForm, self).save(commit=False) #nao quer salvar no banco de dados
        user.is_superuser = True #pegando o user que estamos criando e transformando o superuser em True
        user.set_password(self.cleaned_data['password1']) #salvando a senha dentro do banco de dados
        if commit:
            user.save()
        return user