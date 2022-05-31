from django.http import HttpResponse
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'recipes/home.html', context={
        'name': 'Master Chef',
    })


def contato(request):
    return render(request, 'me_apague/temp.html')


def sobre(request):
    return HttpResponse('sobre')
