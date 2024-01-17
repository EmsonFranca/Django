from django.urls import path
# Importando o modulo 
from  recipes import views

app_name = 'recipes'
  
urlpatterns = [
    
    path('', views.home, name='home'), # Pagina inicial
    path('recipes/<int:id>/', views.recipe, name='recipe'),
]
