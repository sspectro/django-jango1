from django.shortcuts import render


def index(request):
    context = {
        'curso': 'Programação Web com Django Framework',
        'outro': 'Programação Web com Django Framework'
    }
    return render(request, 'index.html',context)


def contato(request):
    return render(request, 'contato.html')