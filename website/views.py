from django.shortcuts import render
from website.models import Pessoa
# Create your views here.

def index(request):
    if request.method == 'POST':
        


    contexto = {

    }
    return render(request, 'index.html', contexto)


def sobre(request):
    contexto = {
        
    }
    return render(request, 'sobre.html', contexto)