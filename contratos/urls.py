# urls.py
from django.urls import path
from .views import lista_contratos

urlpatterns = [
    path('', lista_contratos, name='contratos'),
]
