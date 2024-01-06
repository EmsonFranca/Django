from django.urls import path
# Importando o modulo 
from  recipes import views
    
urlpatterns = [
    path('', views.home), # Pagina inicial
    path('recipes/<id>/', views.recipe),
    
]
