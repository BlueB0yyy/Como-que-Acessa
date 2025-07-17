#Arquivo criado para lidar com os formulários da página (pesquisa, login, etc.)
#Carregamento das tags de input para o back do Django
from django import forms


class NameForm(forms.Form):
    #label = O que aparece antes do nome
    nome = forms.CharField(label='Nome', max_length=100)

class Pesquisa(forms.Form):
    pesquisa = forms.CharField(label='O que deseja saber?', max_length=120) #caso precise de mais, só adicionar