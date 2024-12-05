from django.urls import path
from app_cad_formulario import views


from app_cad_formulario.views import PaginaInicial

urlpatterns = [
    # rota, view responsável, nome de referência
    path('', PaginaInicial.as_view(), name='index'),
]
