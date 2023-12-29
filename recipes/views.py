from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    # NAME ESPECER = informa a pasta e o arquivo que vai ser lido primeiro
    return render(request, 'recipes/index.html', context={
        'name' : 'Emson França'
    })
    #
    # Vai mostrar  a pagina "base_template/global/idex.html" 
    # return render(request, 'global/index.html', status=404)

def sobre(request):
    return render(request, 'temp/temp.html')

def contact(request):
    return HttpResponse('contato!')