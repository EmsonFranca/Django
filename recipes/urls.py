from django.urls import path
from recipes.views import home, about, contact
    
urlpatterns = [
    path('', home), # Pagina inicial
    path('about/', about), # sobre
    path('contact/', contact), # Pagina inicial
]
