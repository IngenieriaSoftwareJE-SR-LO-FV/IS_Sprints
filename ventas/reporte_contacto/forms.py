from django import forms
from .models import ReporteContacto, Capacitacion,Asesoria
from dal import autocomplete


class ReporteContactoForm(forms.ModelForm):
    class Meta:
        model = ReporteContacto

        fields=[
            'id',
            'empresa',
            'canal_de_contacto',
            'motivo_de_contacto',
            'lugar',
            'fecha',
            'hora_inicio',
            'hora_fin',
            'nombre_contacto',
            'telefono',
            'cargo',
            'correo_electronico',
            'asistentes',
            'situacion_actual',
            'situacion_deseada',
            'servicios_requeridos',
        ]

        labels={
            'id':'Código del reporte',
            'empresa': 'Empresa',
            'canal_de_contacto': 'Canal de contacto',
            'motivo_de_contacto': 'Motivo de Contacto',
            'lugar':'Lugar',
            'fecha':'Fecha',
            'hora_inicio':'Hora de inicio',
            'hora_fin':'Hora de fin',
            'nombre_contacto':'Nombre del contacto de la Empresa',
            'telefono':'Teléfono',
            'cargo':'Cargo',
            'correo_electronico':'Correo electrónico',
            'asistentes':'Asistentes',
            'situacion_actual':'Situación actual',
            'situacion_deseada':'Situación deseada',
            'servicios_requeridos': 'Servicios requeridos',
        }
        widgets={
            'empresa':autocomplete.ModelSelect2(url='empresa-autocomplete'),
            'acuerdos':forms.Textarea(attrs={'rows':2}),
            'motivo_de_contacto':forms.Textarea(attrs={'rows':2}),
            'situacion_actual':forms.Textarea(attrs={'rows':2}),
            'situacion_deseada':forms.Textarea(attrs={'rows':2}),
            'fecha':forms.DateInput(attrs={'type':'date'}),
            'hora_inicio':forms.TimeInput(attrs={'type':'time'}),
            'hora_fin':forms.TimeInput(attrs={'type':'time'})
        }

class CapacitacionForm(forms.ModelForm):
    class Meta:
        model = Capacitacion

        fields=[
            'tema',
            'tipo',
            'modalidad',
            'area',
            'nivel_organizacion',
            'numero_participantes',
            'horario_trabajo',
            'nivel_educacion',
            'edad_promedio',
            'lugar',
            'ciudad',
            'fecha_evento',
            'horario_evento_inicio',
            'horario_evento_fin',
            'observaciones',
            'acuerdos',
            'exclusivo_acad',
        ]

        labels={
            'tema':'Tema de capacitación sugerido',
            'tipo':'Tipo de capacitación sugerido',
            'modalidad':'Modalidad',
            'area':'Área(s) del evento',
            'nivel_organizacion':'Nivel organizacional de los participantes',
            'numero_participantes':'Número de participantes',
            'horario_trabajo':'Horario normales de trabajo',
            'nivel_educacion':'Nivel de educación',
            'edad_promedio':'Edad promedio de los participantes',
            'lugar':'Lugar para la capacitación',
            'ciudad':'Ciudad',
            'fecha_evento':'Fechas estimadas para el evento',
            'horario_evento_inicio':'Hora de inicio',
            'horario_evento_fin':'Hora de fin',
            'observaciones':'Observaciones',
            'acuerdos':'Acuerdos',
            'exclusivo_acad':'Para uso exclusivo del área académica',
        }
        widgets={
            'observaciones':forms.Textarea(attrs={'rows':2}),
            'acuerdos':forms.Textarea(attrs={'rows':2}),
            'exclusivo_acad':forms.Textarea(attrs={'rows':2}),
            'fecha_evento':forms.DateInput(attrs={'type':'date'}),
            'horario_evento_inicio':forms.TimeInput(attrs={'type':'time'}),
            'horario_evento_fin':forms.TimeInput(attrs={'type':'time'})
        }

class AsesoriaForm(forms.ModelForm):
    class Meta:
        model=Asesoria

        fields = [
            'tipo_servicio',
            'descripcion',
            'alcance',
            'con_sin_imple',
            'fecha_inicio',
            'fecha_fin',
            'proveedor',
            'entregables',
            'observaciones',
            'acuerdos',
            'exclusivo_acad',
        ]

        labels={
            
            'tipo_servicio':'Tipo de servicio',
            'descripcion':'Descripción',
            'alcance':'Alcance',
            'con_sin_imple':'Con/Sin Implementación',
            'fecha_inicio':'Fecha de inicio',
            'fecha_fin':'Fecha de fin',
            'proveedor':'Proveedor de la información',
            'entregables':'Entregables',
            'observaciones':'Observaciones',
            'acuerdos':'Acuerdos',
            'exclusivo_acad':'Para uso exclusivo del área acedémica',
        }
        widgets={
            'observaciones':forms.Textarea(attrs={'rows':2}),
            'acuerdos':forms.Textarea(attrs={'rows':2}),
            'exclusivo_acad':forms.Textarea(attrs={'rows':2}),
            'fecha_inicio':forms.DateInput(attrs={'type':'date'}),
            'fecha_fin':forms.DateInput(attrs={'type':'date'}),

        }