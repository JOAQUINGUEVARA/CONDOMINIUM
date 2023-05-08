from django.forms import ModelForm, ClearableFileInput
from django import forms
from .models import AnexoContrato,AnexoMantenimiento,AnexoObra,AnexoAvanceObra,AnexoReparacion,AnexoReunionConsejo,AnexoProveedor,AnexoAsamblea,AnexoBajaActivoFijo,AnexoPagoReserva
from .models import AnexoInformeRevisor,AnexoLegislacion,AnexoNormatividad,AnexoProponente,AnexoComunicado,AnexoProponenteProyecto,AnexoProyecto,AnexoProcesoJuridico,AnexoGestionProcesoJuridico
from core.models import Contrato,Proponente


class AnexoProyectoForm(forms.ModelForm):
    
    class Meta:
        model = AnexoProyecto
        fields = ('archivo','proyecto','descripcion')
        widgets = {'proyecto': forms.HiddenInput()}


class AnexoContratoForm(forms.ModelForm):
    
    class Meta:
        model = AnexoContrato
        fields = ('archivo','contrato','descripcion')
        widgets = {'contrato': forms.HiddenInput()}
        
     
class AnexoMantenimientoForm(forms.ModelForm):
    
    class Meta:
        model = AnexoMantenimiento
        fields = ('archivo','mantenimiento','descripcion')
        widgets = {'mantenimiento': forms.HiddenInput()}

class AnexoObraForm(forms.ModelForm):
    
    class Meta:
        model = AnexoObra
        fields = ('archivo','obra','descripcion')
        widgets = {'obra': forms.HiddenInput()}

class AnexoAvanceObraForm(forms.ModelForm):
    
    class Meta:
        model = AnexoAvanceObra
        fields = ('archivo','avance_obra','descripcion')
        widgets = {'anexo_obra': forms.HiddenInput()}

class AnexoReparacionForm(forms.ModelForm):
    
    class Meta:
        model = AnexoReparacion
        fields = ('archivo','reparacion','descripcion')
        widgets = {'reparacion': forms.HiddenInput()}    

class AnexoReunionConsejoForm(forms.ModelForm):
    
    class Meta:
        model = AnexoReunionConsejo
        fields = ('archivo','reunion','descripcion')
        widgets = {'reunion': forms.HiddenInput()}  

class AnexoInformeRevisorForm(forms.ModelForm):
    
    class Meta:
        model = AnexoInformeRevisor
        fields = ('archivo','informe_revisor','descripcion')
        widgets = {'informe_revisor': forms.HiddenInput()} 

class AnexoLegislacionForm(forms.ModelForm):
    
    class Meta:
        model = AnexoLegislacion
        fields = ('archivo','legislacion','descripcion')
        widgets = {'legislacion': forms.HiddenInput()}  

class AnexoNormatividadForm(forms.ModelForm):
    
    class Meta:
        model = AnexoNormatividad
        fields = ('archivo','normatividad','descripcion')
        widgets = {'legislacion': forms.HiddenInput()} 

class AnexoComunicadosForm(forms.ModelForm):
    
    class Meta:
        model = AnexoComunicado
        fields = ('archivo','comunicado','descripcion')
        widgets = {'comunicado': forms.HiddenInput()} 

class AnexoProponenteProyectoForm(forms.ModelForm):
    
    class Meta:
        model = AnexoProponenteProyecto
        fields = ('archivo','proponente_proyecto','descripcion')
        widgets = {'proponente_proyecto': forms.HiddenInput()} 

class AnexoProponenteForm(forms.ModelForm):
    
    class Meta:
        model = AnexoProponente
        fields = ('archivo','proponente','descripcion')
        widgets = {'proponente': forms.HiddenInput()} 

class AnexoProveedorForm(forms.ModelForm):
    
    class Meta:
        model = AnexoProveedor
        fields = ('archivo','proveedor','descripcion')
        widgets = {'proveedor': forms.HiddenInput()} 


class AnexoProcesoJuridicoForm(forms.ModelForm):

       class Meta:
        model = AnexoProcesoJuridico
        fields = ('archivo','proceso_juridico','descripcion')
        widgets = {'proceso_juridico': forms.HiddenInput()} 

class AnexoGestionProcesoJuridicoForm(forms.ModelForm):

       class Meta:
        model = AnexoGestionProcesoJuridico
        fields = ('archivo','gestion_proceso_juridico','descripcion')
        widgets = {'gestion_proceso_juridico': forms.HiddenInput()} 

class AnexoAsambleaForm(forms.ModelForm):

       class Meta:
        model = AnexoAsamblea
        fields = ('archivo','asamblea','descripcion')
        widgets = {'asamblea': forms.HiddenInput()} 

class AnexoBajaActivoFijoForm(forms.ModelForm):

       class Meta:
        model = AnexoBajaActivoFijo
        fields = ('archivo','baja_activo','descripcion')
        widgets = {'baja_activo': forms.HiddenInput()} 

class AnexoPagoReservaForm(forms.ModelForm):

       class Meta:
        model = AnexoPagoReserva
        fields = ('archivo','reserva','descripcion')
        widgets = {'reserva': forms.HiddenInput()} 