from django import forms
from django.db.models.fields import PositiveIntegerField
from .models import PlataformaWebPeatonal,PlataformaWebVehiculo, IngresoPeatonal, Residente,Visitante,Correspondencia,Interior,Apartamento,VisitanteVehiculo,ActivoFijo,Contrato,Proveedor,Obra,MiembroConsejo
from .models import Reparacion,AvanceObra,CompromisoConsejo,MiembroStaff,InformeRevisor,RecomendacionRevisor,ProcesoJuridico,TipoProceso,ZonaComun,ResidenteTemp,TipoAsamblea
from .models import Reservas,Proponente,Proyecto,ProponenteProyecto,TipoProyecto,TipoContrato,TipoActivo,PrestamoActivoFijo,GestionProcesoJuridico,Asamblea,DecisionAsamblea
from .models import MiembroComiteConvivencia,BajaActivoFijo
#from searchableselect.widgets import SearchableSelect
#from bootstrap_datepicker_plus import DatePickerInput
#from material import Layout, Row, Column, Fieldset, Span2, Span3, Span5, Span6, Span10
from .models import Vigilante, UserPerfil,Vehiculo,Mascota,Parqueadero,Deposito,Autorizado,IngresoVehiculo,Mantenimiento,ServicioProveedor,ReunionConsejo,DecisionConsejo,AutorizacionVehiculo
from django.contrib.auth.models import User
from datetime import datetime
from bootstrap_datepicker_plus.widgets import DatePickerInput,DateTimePickerInput,MonthPickerInput, YearPickerInput
#from .widgets import DateTimePickerInput
#from django.conf.global_settings import DATETIME_INPUT_FORMATS
#from bootstrap_modal_forms.forms import BSModalModelForm
from ckeditor.widgets import CKEditorWidget
from bootstrap3_datetime.widgets import DateTimePicker

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class ProfileForm(forms.ModelForm):
    class Meta:
        model =  UserPerfil
        fields = ('interior', 'apartamento')

class DatosIngresoPeatonalForm(forms.ModelForm):

    class Meta:
        
        model = IngresoPeatonal
        fields = ['tipoingreso','interior','apartamento',]
        
        widgets = {
            'tipoingreso':  forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo de Ingreso'}),
            'interior':  forms.Select(attrs={'class':'form-control', 'placeholder':'Interior'}),
            'apartamento':  forms.Select(attrs={'class':'form-control', 'placeholder':'Apartamento'}),
        }    
  
class DatosIngresoVehicularForm(forms.ModelForm):

    class Meta:
        model = IngresoVehiculo
        fields = ['interior','apartamento',]
        
        widgets = {
            #'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'interior':  forms.Select(attrs={'class':'form-control', 'placeholder':'Interior'}),
            'apartamento':  forms.Select(attrs={'class':'form-control', 'placeholder':'Apartamento'}),
        } 

class VisitanteForm(forms.ModelForm):

    class Meta:
        model = Visitante
        fields = ['nombre']
        widgets = {
            #'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            #'identificacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de Identificación'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
        }        

class VisitanteVehiculoForm(forms.ModelForm):

    class Meta:
        model = VisitanteVehiculo
        fields = ['identificacion','nombre']
        widgets = {
            #'foto': forms.ClearableFileInput(attrs={'class':'form-control-file mt-3'}),
            'identificacion': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Número de Identificación'}),
            'nombre': forms.TextInput(attrs={'class':'form-control', 'placeholder':'Nombre'}),
        }        

class DatosCorrespondenciaForm(forms.ModelForm):

    class Meta:
        model = Correspondencia
        fields = ['clase_correspondencia','tipo_correspondencia','interior','apartamento']
        
        widgets = {
            'remitente': forms.TextInput(attrs={'class':'form-control','rows':3,'placeholder':'Remitente'}),
            #'destinatario': forms.TextInput(attrs={'class':'form-control','rows':3,'placeholder':'Destinatario'}),
            'clase_correspondencia': forms.Select(attrs={'class':'form-control', 'placeholder':'Clase Correspondencia'}),
            'tipo_correspondencia': forms.Select(attrs={'class':'form-control', 'placeholder':'Tipo Correspondencia'}),
            #'detalle': forms.TextInput(attrs={'class':'form-control','rows':3,'placeholder':'Detalle'}),
            'interior': forms.Select(attrs={'class':'form-control', 'placeholder':'Interior'}),
            'apartamento': forms.Select(attrs={'class':'form-control', 'placeholder':'Apartamento'}),
                       
        }

class AutorizadoForm(forms.ModelForm):
    
    class Meta:
        model = Autorizado
        fields = ['identificacion','nombre','permanente','fecha_inicial','fecha_final','interior','apartamento','tipo_autoriza','permanente']

        widgets = {
        'fecha_inicial': DatePickerInput(format='%d/%m/%Y'),   
        'fecha_final' : DatePickerInput(format='%d/%m/%Y')              
        }
        
class AutorizadoPlataformaWebPeatonalForm(forms.ModelForm):
   
    class Meta:
        model = PlataformaWebPeatonal
        fields = ['identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma']

        widgets = {
        'fecha_inicial': DatePickerInput(format='%d/%m/%Y'),   
        'fecha_final' : DatePickerInput(format='%d/%m/%Y')              
        }

class AutorizadoVehicularForm(forms.ModelForm):
   
    class Meta:
        model = AutorizacionVehiculo
        fields = ['placa','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_autoriza']

        widgets = {
        'fecha_inicial': DatePickerInput(format='%d/%m/%Y'),   
        'fecha_final' : DatePickerInput(format='%d/%m/%Y')              
        }

class AutorizadoPlataformaWebVehiculoForm(forms.ModelForm):
   
    class Meta:
        model = PlataformaWebVehiculo
        fields = ['placa','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma']

        widgets = {
        'fecha_inicial': DatePickerInput(format='%d/%m/%Y'),   
        'fecha_final' : DatePickerInput(format='%d/%m/%Y')              
        }

class DatosReservaZonasComunesForm(forms.ModelForm):
    
    class Meta:
        model = Reservas
        fields = ['fecha','hora_inicio','hora_final']
        widgets = {
            'fecha': DatePickerInput()
        }
        

from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, ButtonHolder, Submit

class CorrespondenciaListFormHelper(FormHelper):
    #model = Correspondencia
    form_method = 'GET'
    #fields = ['interior','apartamento','vigilante','entregado']
    #form_tag = False
    form_style = 'inline'
    layout = Layout(
        'interior',
        'apartamento',
        'vigilante',
        'entregado',
        Submit('submit', 'Filtrar'),
    )

class CreaCorrespondenciaForm(forms.ModelForm):
    class Meta:
        model = Correspondencia
        fields = ['clase_correspondencia','tipo_correspondencia','interior','apartamento']

""" class FechaReservaZonasComunesForm(BSModalModelForm):
    
    class Meta:
        model = ReservaZonasComunes
        fields = ['fecha_inicial']
        
        widgets = {
         'fecha': DatePickerInput(format='%d/%m/%Y')
                       
        } """

""" class FiltroCorrespondenciaForm(BSModalModelForm):
    
    class Meta:
        model = Filtros
        fields = ['fecha']
        
        widgets = {
         'fecha': DatePickerInput(format='%d/%m/%Y')
                       
        } """

class ResidenteForm(forms.ModelForm):

    class Meta:
        model = Residente
        fields =['interior','apartamento','identificacion','nombre','tipo_residente','telefono','celular','email','edad','genero','persona_discapacitada']

class ResidenteTempForm(forms.ModelForm):

    class Meta:
        model = ResidenteTemp
        fields =['interior','apartamento','identificacion','nombre','tipo_residente','telefono','celular','email','edad','genero','persona_discapacitada']

class ParqueaderoForm(forms.ModelForm):

    class Meta:
        model = Parqueadero
        fields =['numero','coeficiente']

class VehiculoForm(forms.ModelForm):

    class Meta:
        model = Vehiculo
        fields =['placa','tipo_vehiculo','uso','marca','modelo','color','parqueadero']

class ResidenteLoginForm(forms.ModelForm):

    class Meta:
        model = Residente
        fields =['email','interior','apartamento','token']

class SolicitudTokenForm(forms.ModelForm):

    class Meta:
        model = Residente
        fields =['email','interior','apartamento']

""" class ResidenteOtroForm(forms.ModelForm):
    
    class Meta:
        model = ResidenteOtro
        fields = fields =['identificacion','nombre','telefono','celular','email','edad','genero','persona_discapacitada','genero'] """
        
class MascotaForm(forms.ModelForm):
    
    class Meta:
        model = Mascota
        fields = ['nombre','tipo_mascota','raza','edad',]
        
class DepositoForm(forms.ModelForm):
    
    class Meta:
        model = Deposito
        fields = ['numero']

class UserPerfilForm(forms.ModelForm):

    class Meta:
        model = UserPerfil
        fields =['interior','apartamento']

from django import forms
from django.contrib.auth.forms import UserCreationForm

class NewUserForm(UserCreationForm):
	email = forms.EmailField(required=True)

	class Meta:
		model = User
		fields = ("username", "email", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.email = self.cleaned_data['email']
		if commit:
			user.save()
		return user

from django import forms

""" class ImageUploadWCForm(forms.Form):

    print("Image upload from WC form.")        
    foto = forms.ImageField(label='Select a file')              
    print ('Hi in Webcam', foto)        

class DocScanUploadForm(forms.Form):
    print("Image upload from WC form.")        
    foto = forms.ImageField(label='Select a file')              
    print ('Hi in Webcam', foto)       """  

class ActivoFijoForm(forms.ModelForm):
    
    class Meta:
        model = ActivoFijo
        fields = ['nombre','tipo_activo','descripcion','marca','serial','valor_libros','cantidad','mantenimiento','frecuencia_mantenimiento','ultimo_mantenimiento','placa_numero','prestado']
        nombre = forms.TextInput(attrs={'required': True})
        
        widgets = {
        'descripcion': forms.Textarea(attrs={'cols':50,'rows':5})
                       
        }

class MantenimientoForm(forms.ModelForm):
    
    class Meta:
        model = Mantenimiento
        fields = ['fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado']
        activo_fijo = forms.TextInput(attrs={'required': True})
        proveedor = forms.TextInput(attrs={'required': True})
        contrato = forms.TextInput(attrs={'required': True})
        

        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5})                  
        }

class PrestamoActivoForm(forms.ModelForm):
    
    class Meta:
        model = PrestamoActivoFijo
        fields = ['activo_fijo','fecha','responsable','cantidad',]
        activo_fijo = forms.TextInput(attrs={'required': True})
        fecha = forms.TextInput(attrs={'required': True})
        cantidad = forms.TextInput(attrs={'required': True})
        
        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'responsable': forms.Textarea(attrs={'cols':50,'rows':5}),
         'activo_fijo': forms.HiddenInput()                  
        }

class BajaActivoForm(forms.ModelForm):
    
    class Meta:
        model = BajaActivoFijo
        fields = ['activo_fijo','fecha','detalle','cantidad','causa_baja']
        activo_fijo = forms.TextInput(attrs={'required': True})
        fecha = forms.TextInput(attrs={'required': True})
        cantidad = forms.TextInput(attrs={'required': True})
        
        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'responsable': forms.Textarea(attrs={'cols':50,'rows':5}),
         'activo_fijo': forms.HiddenInput()                  
        }

class ProveedorForm(forms.ModelForm):
    
    class Meta:
        model = Proveedor
        fields = ['cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion']
        cc_nit = forms.TextInput(attrs={'required': True})
        nombre = forms.TextInput(attrs={'required': True})
        email = forms.TextInput(attrs={'required': True})
        
class ProponenteForm(forms.ModelForm):
    
    class Meta:
        model = Proponente
        fields = ['cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion']
        cc_nit = forms.TextInput(attrs={'required': True})
        nombre = forms.TextInput(attrs={'required': True})
        email = forms.TextInput(attrs={'required': True})

class ContratoForm(forms.ModelForm):
    
    class Meta:
        model = Contrato
        fields = ['numero','proveedor','tipo_contrato','objeto','fecha_contrato','valor','valor_anticipo','descripcion','activo','vigencia']
        numero = forms.TextInput(attrs={'required': True})
        objeto = forms.TextInput(attrs={'required': True})
        fecha_contrato = forms.TextInput(attrs={'required': True})
        descripcion = forms.TextInput(attrs={'required': True})
        vigencia = forms.TextInput(attrs={'required': True})

        widgets = {
        'fecha_contrato' : DatePickerInput(format='%d/%m/%Y')              
        }    

class ServicioProveedorForm(forms.ModelForm):
    
    class Meta:
        model = ServicioProveedor
        fields = ['descripcion',]    

class TipoProyectoForm(forms.ModelForm):
    
    class Meta:
        model = TipoProyecto
        fields = ['descripcion',]  

class TipoContratoForm(forms.ModelForm):
    
    class Meta:
        model = TipoContrato
        fields = ['descripcion',]    

class TipoActivoFijoForm(forms.ModelForm):
    
    class Meta:
        model = TipoActivo
        fields = ['descripcion',]    

class ObrasForm(forms.ModelForm):
    
    class Meta:
        model = Obra
        fields = ['fecha','proveedor','interventor','descripcion','contrato','valor','valor_anticipo','valor_pagado','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada']
        activo_fijo = forms.TextInput(attrs={'required': True})
        proveedor = forms.TextInput(attrs={'required': True})
        valor = forms.DecimalField(label=u'Valor Obra (R$)', required=False, max_digits=11, decimal_places=2, min_value=1)
       
        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'terminado': forms.RadioSelect(),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5})                  
        }        

class ProyectosFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        'status',
        Submit('submit', 'Apply Filter'),
    )

class ProyectoFilterFormHelper(FormHelper):
    form_method = 'GET'
    layout = Layout(
        'status',
        Submit('submit', 'Apply Filter'),
    )

class ProyectosForm(forms.ModelForm):

    presupuesto = forms.FloatField( )    
    class Meta:
        model = Proyecto
        fields = ['fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto']
        

class ProponenteProyectoForm(forms.ModelForm):
    
    class Meta:
        model = ProponenteProyecto
        fields = ['proyecto','proponente','fecha','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra']
        widgets = {'obra': forms.HiddenInput()}
           

        widgets = {
         'fecha' : forms.DateField(widget=forms.DateInput(attrs={'type': 'date'})),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5})                  
        }        

class AvanceObrasForm(forms.ModelForm):
    
    class Meta:
        model = AvanceObra
        fields = ['obra','fecha','descripcion','valor','porcentaje_avance']
        widgets = {'obra': forms.HiddenInput()}
           

        widgets = {
         'fecha' : DatePickerInput(format='%d/%m/%Y'),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5})                  
        }        

class ReparacionesForm(forms.ModelForm):
    
    class Meta:
        model = Reparacion
        fields = ['fecha','proveedor','descripcion','valor','valor_anticipo','observacion','calificacion','fecha_terminacion','terminado']
        activo_fijo = forms.TextInput(attrs={'required': True})
        proveedor = forms.TextInput(attrs={'required': True})
     
        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'terminado': forms.RadioSelect(),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5}) ,
         'observacion': forms.Textarea(attrs={'cols':50,'rows':5})                 
        }

from bootstrap3_datetime.widgets import DateTimePicker

class ReunionConsejoForm(forms.ModelForm):
    
    class Meta:
        model = ReunionConsejo
        fields = ['fecha','contenido','numero_acta','hora_inicio','hora_final']
        
        widgets = {
         'fecha': forms.DateInput(format='%d/%m/%Y'),
         'contenido': forms.Textarea(attrs={'cols':50,'rows':5}),
         'hora_inicio': forms.TimeInput(format='%H:%M'),
         'hora_final': forms.TimeInput(format='%H:%M'),
        }
        
        
class DecisionConsejoForm(forms.ModelForm):

    class Meta:
        model = DecisionConsejo
        fields = ['reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion']
        widgets = {
            'reunion_consejo': forms.HiddenInput(),
            'decision': forms.Textarea(attrs={'cols':50,'rows':5})}    


class CompromisoConsejoForm(forms.ModelForm):

    class Meta:
        model = CompromisoConsejo
        fields = ['compromiso']
        widgets = {
            'compromiso': forms.Textarea(attrs={'cols':50,'rows':5})}

class MiembroConsejoForm(forms.ModelForm):
    
    envio = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)
    
    class Meta:
        model = MiembroConsejo
        fields = ['interior','apartamento','nombre','cargo','email','envio','publicar','comunidad','activo','foto','orden']

class ComiteConvivenciaForm(forms.ModelForm):
    
    envio = forms.BooleanField(required=False)
    activo = forms.BooleanField(required=False)
    publicar = forms.BooleanField(required=False)
    
    class Meta:
        model = MiembroComiteConvivencia
        fields = ['interior','apartamento','nombre','email','envio','activo','publicar','comunidad','foto','orden']

class VigilanteForm(forms.ModelForm):
    
    publicar = forms.BooleanField(required=False)
    comunidad = forms.BooleanField(required=False)
       
    class Meta:
        model = Vigilante
        fields = ['nombre','email','publicar','comunidad','foto','orden']

class InformeRevisorForm(forms.ModelForm):
    
    class Meta:
        model = InformeRevisor
        fields = ['fecha','contenido']
        widgets = {
            'fecha': forms.DateInput(attrs={'required': True},format='%d/%m/%Y'),
            'contenido': forms.Textarea(attrs={'cols':50,'rows':5})}

        
class MiembroStaffForm(forms.ModelForm):

    class Meta:
        model = MiembroStaff
        fields = ['nombre','cargo','email','envio','publicar','comunidad','foto','orden']


class ZonaComunForm(forms.ModelForm):

    class Meta:
        model = ZonaComun
        fields = ['descripcion','observaciones','tarifa','arrienda','foto','orden']

class CargaFotoMiembroConsejoForm(forms.ModelForm):

    class Meta:
        model = MiembroConsejo
        fields = ['foto']

class CargaFotoMiembroComiteForm(forms.ModelForm):

    class Meta:
        model = MiembroComiteConvivencia
        fields = ['foto']

class CargaFotoActivoFijoForm(forms.ModelForm):

    class Meta:
        model = ActivoFijo
        fields = ['foto']

class CargaFotoZonaComunForm(forms.ModelForm):

    class Meta:
        model = ActivoFijo
        fields = ['foto']
             
class CargaFotoMiembroStaffForm(forms.ModelForm):

    class Meta:
        model = MiembroStaff
        fields = ['foto']


class RecomendacionRevisorForm(forms.ModelForm):

    class Meta:
        model = RecomendacionRevisor
        fields = ['recomendacion']
        widgets = {
            'informe_revisor': forms.HiddenInput(),
            'recomendacion': forms.Textarea(attrs={'cols':50,'rows':5,'required': True})}

class ProcesoJuridicoForm(forms.ModelForm):
    
    class Meta:
        model = ProcesoJuridico
        fields = ['proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo']
               
        widgets = {
         'fecha': forms.DateInput(format='%d/%m/%Y'),
         'contenido': forms.Textarea(attrs={'cols':50,'rows':5}),
         'juzgado': forms.Textarea(attrs={'cols':50,'rows':1}),
         'hora_inicio': forms.TimeInput(format='%H:%M'),
         'hora_final': forms.TimeInput(format='%H:%M'),
        }

class TipoProcesoForm(forms.ModelForm):
    
    class Meta:
        model = TipoProceso
        fields = ['descripcion',]       

#from .forms import UserCreationFormWithEmail, ProfileForm, EmailForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
#from .models import Profile

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text="Requerido. 254 carácteres como máximo y debe ser válido.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("El email ya está registrado, prueba con otro.")
        return email

class ProponenteProyectoForm(forms.ModelForm):
    
    class Meta:
        model = ProponenteProyecto
        fields = ['proponente','fecha','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra']
        proyecto = forms.TextInput(attrs={'required': True})
        proponente = forms.TextInput(attrs={'required': True})
        descripcion = forms.TextInput(attrs={'required': True})
        
        widgets = {
         'fecha' : forms.DateInput(format='%d/%m/%Y'),
         'descripcion': forms.Textarea(attrs={'cols':50,'rows':5}),
        }        

class GestionProcesoJuridicoForm(forms.ModelForm):

    class Meta:
        model = GestionProcesoJuridico
        fields = ['proceso_juridico','fecha','titulo','gestion']
        widgets = {
            'proceso_juridico': forms.HiddenInput(),
            'gestion': forms.Textarea(attrs={'cols':50,'rows':5,'required': True})}
        
class AsambleaForm(forms.ModelForm):

    class Meta:
        model = Asamblea
        fields = ['fecha','tipo_asamblea','contenido','hora_inicio','hora_final','numero_acta']
        widgets = {
            'fecha': forms.DateInput(format='%d/%m/%Y'),
            'contenido': forms.Textarea(attrs={'cols':50,'rows':5})}

class DecisionAsambleaForm(forms.ModelForm):

    class Meta:
        model = DecisionAsamblea
        fields = ['asamblea','decision','numero_votos_favor','numero_votos_contra']
        widgets = {
            'asamblea': forms.HiddenInput(),
            'decision': forms.Textarea(attrs={'cols':50,'rows':5,'required': True})}        

class TipoAsambleaForm(forms.ModelForm):
    
    class Meta:
        model = TipoAsamblea
        fields = ['descripcion',]               


class ContactForm(forms.Form):
	Nombre = forms.CharField(max_length = 50)
	Apellido = forms.CharField(max_length = 50)
	email = forms.EmailField(max_length = 150)
	mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)
        
class EmailForm(forms.Form):
    #email = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    mensaje = forms.CharField(widget = forms.Textarea)        


class EmailAnexoForm(forms.Form):
    #email = forms.EmailField()
    asunto = forms.CharField(max_length=100)
    anexo = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}))
    mensaje = forms.CharField(widget = forms.Textarea)        
    