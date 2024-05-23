# views.py
from django.shortcuts import render
from .models import Contrato

def lista_contratos(request):
    contratos = Contrato.objects.all()
    return render(request, 'contratos.html', {'contratos': contratos})
