# views.py
from django.shortcuts import render
from .models import Contrato
from django.shortcuts import render, get_object_or_404
from django.shortcuts import render
from .models import Contrato
from django.db.models import Q


def lista_contratos(request):
    query = request.GET.get('q')
    if query:
        contratos = Contrato.objects.filter(
            Q(contrato_no__icontains=query) |
            Q(tipo_de_contrato__icontains=query) |
            Q(ANO__icontains=query) |
            Q(nombre__icontains=query) |
            Q(entidad__icontains=query) |
            Q(rup__icontains=query) |
            Q(contrato__icontains=query) |
            Q(smmlv__icontains=query) |
            Q(secop__icontains=query) |
            Q(contrato2__icontains=query) |
            Q(acta_final__icontains=query) |
            Q(objeto__icontains=query) |
            Q(fecha_inicio__icontains=query) |
            Q(fecha_final__icontains=query) |
            Q(valor__icontains=query) |
            Q(smmlv3__icontains=query) |
            Q(adicion__icontains=query) |
            Q(part_porc__icontains=query) |
            Q(valor_total__icontains=query) |
            Q(smmlv4__icontains=query)
        )
    else:
        contratos = Contrato.objects.filter(is_visible=True)

    return render(request, 'contratos.html', {'contratos': contratos, 'query': query})

def detalle_contrato(request, id):
    contrato = get_object_or_404(Contrato, id=id)
    return render(request, 'detalle_contrato.html', {'contrato': contrato})

def index(request):
    return render(request, 'index.html')