from django.contrib import admin
from import_export import resources
from import_export.admin import ImportExportModelAdmin
from .models import Contrato

class ContratoResource(resources.ModelResource):
    class Meta:
        model = Contrato
        fields = ('id', 'ANO', 'contrato_no', 'tipo_de_contrato', 'nombre', 'entidad', 'rup', 'contrato', 'smmlv',
                  'secop', 'contrato2', 'acta_final', 'objeto', 'fecha_inicio', 'fecha_final', 'valor', 'smmlv3',
                  'adicion', 'part_porc', 'valor_total', 'smmlv4')
        export_order = ('id', 'ANO', 'contrato_no', 'tipo_de_contrato', 'nombre', 'entidad', 'rup', 'contrato', 'smmlv',
                        'secop', 'contrato2', 'acta_final', 'objeto', 'fecha_inicio', 'fecha_final', 'valor', 'smmlv3',
                        'adicion', 'part_porc', 'valor_total', 'smmlv4')

@admin.register(Contrato)
class ContratoAdmin(ImportExportModelAdmin):
    resource_class = ContratoResource
    list_display = ('ANO', 'contrato_no', 'tipo_de_contrato', 'nombre', 'entidad', 'fecha_inicio', 'fecha_final', 'valor_total')
    search_fields = ('contrato_no', 'nombre', 'entidad')
    list_filter = ('ANO', 'tipo_de_contrato', 'entidad')
    ordering = ('-ANO',)

    fieldsets = (
        (None, {
            'fields': ('ANO', 'contrato_no', 'tipo_de_contrato', 'nombre', 'entidad', 'rup', 'contrato', 'smmlv', 
                       'secop', 'contrato2', 'acta_final', 'objeto', 'fecha_inicio', 'fecha_final', 'valor', 
                       'smmlv3', 'adicion', 'part_porc', 'valor_total', 'smmlv4','is_visible')
        }),
    )
