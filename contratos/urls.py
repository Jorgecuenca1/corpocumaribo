# urls.py
from django.urls import path
from .views import lista_contratos, detalle_contrato

urlpatterns = [
    path('', lista_contratos, name='contratos'),
    path('contrato/<int:id>/', detalle_contrato, name='detalle_contrato'),
]
