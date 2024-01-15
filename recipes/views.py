from django.shortcuts import render
from utils.recipes.factory import make_recipe

# Create your views here.
def home(request):
    # NAME ESPECER = informa a pasta e o arquivo que vai ser lido primeiro
    return render(request, 'recipes/pages/index.html', context={
        'recipes' : [make_recipe() for _ in range(10)],
    })
    #
    # Vai mostrar  a pagina "base_template/global/idex.html" 
    # return render(request, 'global/index.html', status=404)
def recipe(request, id):
    # NAME ESPECER = informa a pasta e o arquivo que vai ser lido primeiro
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe' : make_recipe(),
    })
