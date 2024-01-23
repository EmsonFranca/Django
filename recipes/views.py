from django.shortcuts import render
from utils.recipes.factory import make_recipe
from .models import Recipe

# Create your views here.
def home(request):
    recipe = Recipe.objects.all().order_by('-id')
    return render(request, 'recipes/pages/index.html', context={
        'recipes' : recipe,
    })
def category(request, category_id):
    recipe = Recipe.objects.filter(category__id=category_id).order_by('-id')
    return render(request, 'recipes/pages/index.html', context={
        'recipes' : recipe,
    })
   
def recipe(request, id):
   
    return render(request, 'recipes/pages/recipe-views.html', context={
        'recipe' : make_recipe(),
        'is_detail_page': True,
    })
