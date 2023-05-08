from django.db import models
from ckeditor.fields import RichTextField
from core.models import Interior,Apartamento
from django.contrib.auth.models import User
from datetime import datetime, timedelta 

# Create your models here.

class Page(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "página"
        verbose_name_plural = "páginas"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

class Panel(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "panel"
        verbose_name_plural = "panel"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

from ckeditor_uploader . fields import RichTextUploadingField

class Comunicado(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(null=True,blank=True,default='',verbose_name="Contenido")
    foto = models.ImageField(verbose_name="Foto Comunicado", upload_to="pages",null=True,blank=True)
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    dias_publicacion = models.SmallIntegerField(verbose_name='Dias Comunicación',default=0)
    publicar = models.BooleanField(default=False,verbose_name='Publicar en Web')
    comunidad = models.BooleanField(default=False,verbose_name='Publicar sólo a Cominidad') 
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "Comunicado"
        verbose_name_plural = "Comunicado"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

class Legislacion(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(null=True,blank=True,default='',verbose_name="Contenido")
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "legislacion"
        verbose_name_plural = "legislacion"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

class TipoPqr(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Pqr'
		verbose_name_plural='Tipos Pqr'

	def __str__(self):
		return self.descripcion

class Pqr(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    tipo_pqr = models.ForeignKey(TipoPqr,on_delete=models.CASCADE)
    user = models.ForeignKey(User,verbose_name="Usuario",default='',on_delete=models.CASCADE)
    remitente = models.CharField(max_length=60,default='',blank=True,verbose_name='Remitente')
    interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
    apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
    foto = models.ImageField(verbose_name="Foto Pqr", upload_to="pages",null=True,blank=True)
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    recibida = models.DateTimeField(blank=True,null=True,default=None,verbose_name="Fecha de recibida")
    fecha_respuesta = models.DateTimeField(null=True,blank=True,auto_now=False,default=None,verbose_name="Fecha de Respuesta")
    pendiente = models.BooleanField(null=True,blank=True,default=True,verbose_name="Pendiente")
    
    class Meta:
        verbose_name = "Pqr"
        verbose_name_plural = "Pqr"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

class RespuestaPqr(models.Model):
    pqr = models.ForeignKey(Pqr,on_delete=models.CASCADE,verbose_name='Pqr')
    content = RichTextField(verbose_name="Contenido")
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")

    class Meta:
        verbose_name = "Respuesta Pqr"
        verbose_name_plural = "Respuestas Pqr"
        ordering=['content']
    
    def __str__(self):
        return self.content

class Clasificado(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    content = RichTextField(verbose_name="Contenido")
    foto = models.ImageField(verbose_name="Foto Clasificado", upload_to="pages",null=True,blank=True)
    user = models.ForeignKey(User,verbose_name="Residente",default='',on_delete=models.CASCADE)
    informes = models.CharField(max_length=100,default='',verbose_name='Informes')
    vigente = models.BooleanField(default=True,verbose_name='Venta vigente')
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    
    class Meta:
        verbose_name = "Clasificado"
        verbose_name_plural = "Clasificados"
        ordering=['order','title']
    
    def __str__(self):
        return self.title

class Normatividad(models.Model):
    title = models.CharField(verbose_name="Título", max_length=200)
    order = models.SmallIntegerField(verbose_name='Orden',default=0)
    created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
    updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
    
    class Meta:
        verbose_name = "Normatividad Interna"
        verbose_name_plural = "Normatividad Interna"
        ordering=['order','title']
    
    def __str__(self):
        return self.title