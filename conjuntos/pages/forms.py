from django import forms
from .models import Pqr,Clasificado, RespuestaPqr,Legislacion,Comunicado,Normatividad
from ckeditor.widgets import CKEditorWidget

class PQRForm(forms.ModelForm):
    
    class Meta:
        model = Pqr
        fields = ['tipo_pqr','title','content','remitente','foto','interior','apartamento']
        #content = forms.CharField(widget=CKEditorWidget())       

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'}),
            'remitente': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Informes'})
                       
        }

class ClasificadosForm(forms.ModelForm):

    class Meta:
        model = Clasificado
        fields = ['title','content','foto','informes']

        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'}),
            'informes': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Informes'})
                       
        }

class AnexoFotoClasificadoForm(forms.ModelForm):
    
    class Meta:
        model = Clasificado
        fields = ['foto']

class RespuestaPQRForm(forms.ModelForm):
    
    class Meta:
        model =  RespuestaPqr
        fields = ['content']
        content = forms.CharField(widget=CKEditorWidget())

class LegislacionForm(forms.ModelForm):

    class Meta:
        model = Legislacion
        fields = ['title','content','order']
        content = forms.CharField(widget=CKEditorWidget())
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'})
        }

class ComunicadoForm(forms.ModelForm):
    #foto = forms.ImageField()
    class Meta:
        model = Comunicado
        fields = ['title','content','dias_publicacion','publicar','comunidad','foto','order']
        content = forms.CharField(widget=CKEditorWidget())
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'})
        }

class LegislacionForm(forms.ModelForm):

    class Meta:
        model = Legislacion
        fields = ['title','content','order']
        content = forms.CharField(widget=CKEditorWidget())
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'})
        }

class NormatividadForm(forms.ModelForm):

    class Meta:
        model = Normatividad
        fields = ['title','order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control','rows':1,'placeholder':'Título'})
        }