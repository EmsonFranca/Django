from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return HttpResponse('Você está na pagina principal!')

def about(request):
    return HttpResponse('Você está na pagina sobre!')

def contact(request):
    return HttpResponse('Você está na pagina contato!')