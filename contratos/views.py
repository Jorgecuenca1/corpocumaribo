# views.py
from django.shortcuts import render
from .models import Contrato
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Contrato

def lista_contratos(request):
    contratos = Contrato.objects.filter(is_visible=True)
    return render(request, 'contratos.html', {'contratos': contratos})

def detalle_contrato(request, id):
    contrato = get_object_or_404(Contrato, id=id)
    return render(request, 'detalle_contrato.html', {'contrato': contrato})

def index(request):
    return render(request, 'index.html')