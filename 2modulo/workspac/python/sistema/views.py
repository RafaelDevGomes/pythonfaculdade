from django.shortcuts import render
from django.http import HttpResponse

# VIEWS --> funções que retornam algo: request --> response
# View responsável pela tela inicial do médico

def home_view(request):
    print('--------------Página funcionou!--------------')
    return HttpResponse('Seja bem-vindo a home!')

def medico_view(request):
    print('--------------Página funcionou!--------------')
    return HttpResponse('Página inicial do Médico')
