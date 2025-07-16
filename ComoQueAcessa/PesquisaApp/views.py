from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader

from .forms import NameForm, Pesquisa

# Create your views here.

def main(request):
    form_da_pesquisa = Pesquisa()
    context = {
        'barra':form_da_pesquisa
    }
    template = loader.get_template('main.html')
    return HttpResponse(template.render(context, request))



def login(request):
    template = loader.get_template('login.html')
    return HttpResponse(template.render())


def teste(request):
    form = NameForm()
    context = {
        'form':form
    }
    return render(request, 'teste.html', context = context)