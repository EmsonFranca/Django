from django.urls import path
from recipes.views import home, sobre, contact
    
urlpatterns = [
    path('', home), # Pagina inicial
    path('about/', sobre), # sobre
    path('contact/', contact), # Pagina inicial
]
