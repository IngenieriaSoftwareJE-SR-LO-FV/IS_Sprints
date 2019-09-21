from django import forms
from .models import PropuestaCorporativo
from ventas.personas_juridicas.models import Sector
from dal import autocomplete

class PropuestaCorporativoForm(forms.ModelForm):
    class Meta:
        model = PropuestaCorporativo

        fields=[
            'cod_propuesta',
            'version',
            'nombre_propuesta',
            'tipo_empresa',
            'reporte',
            'estado',
            'empresa',
            'sector',
            'fecha_solicitud',
            'numero_participantes',
            'total_horas',
            'cantidad_cursos',
            'monto_propuesta',
            'margen_contribucion',
            'utilidad_esperada',
            'exito',
            'lugar',
            'servicios_incluidos',
            'fecha_inicio_estimada',
            'observacion',
            'anexo',
            'nombre',
        ]

        labels = {
            'cod_propuesta':'Código de la propuesta',
            'version':'Versión',
            'nombre_propuesta':'Nombre Propuesta',
            'tipo_empresa':'Tipo de Empresa',
            'reporte':'Reporte de contacto asociado',
            'estado':'Estado',
            'empresa':'Empresa',
            'sector':'Sector',
            'fecha_solicitud':'Fecha de solicitud',
            'numero_participantes':'Número de participantes',
            'total_horas':'Total horas',
            'cantidad_cursos':'Cantidad de Cursos',
            'monto_propuesta':'Monto propuesta',
            'margen_contribucion':'% Margen de contribución',
            'utilidad_esperada':'Utilidad esperada',
            'exito':'% Éxito',
            'lugar':'Lugar',
            'servicios_incluidos':'Servicios incluidos',
            'fecha_inicio_estimada':'Fecha de inicio estimada',
            'observacion':'Observación',
            'anexo':'Anexo',
            'nombre':'Nombre',
        }
        
        widgets={
            'reporte':autocomplete.ModelSelect2(url='reporte-autocomplete'),
            'empresa':autocomplete.ModelSelect2(url='empresa-autocomplete'),
            'observacion':forms.Textarea(attrs={'rows':2}),
            'fecha_solicitud':forms.DateInput(attrs={'type':'date'}),
            'fecha_inicio_estimada':forms.DateInput(attrs={'type':'date'}),
            'total_horas':forms.TimeInput(attrs={'type':'time'})
        }