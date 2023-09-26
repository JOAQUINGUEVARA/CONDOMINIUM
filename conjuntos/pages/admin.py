from django.contrib import admin
from pages.models import Page,Panel,Legislacion,Comunicado,Pqr,TipoPqr,RespuestaPqr,Clasificado,Normatividad
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
# Register your models here.

class PageAdmin(admin.ModelAdmin):

    list_display= ('title','content','order','created','updated',)
    list_filter=('title','content','order','created','updated',)

admin.site.register(Page, PageAdmin)

class PanelAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display= ('title','content','order','created','updated',)
    list_filter=('title','content','order','created','updated',)

admin.site.register(Panel, PanelAdmin)

class LegislacionResource(resources.ModelResource):
    class Meta:
        model = Legislacion
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','title','content','order','created','updated',)
        exclude = ('id')

@ admin.register (Legislacion)
class Legislacion(ImportExportModelAdmin):
    list_display= ('id','title','content','order','created','updated',)
    list_filter=('id','title','content','order','created','updated',)
    list_per_page = 15


class ComunicadoResource(resources.ModelResource):
    class Meta:
        model = Comunicado
        skip_unchanged = True
        report_skipped = True
        list_display=('title','content','dias_publicacion','publicar','comunidad','foto','order')
        exclude = ('id')

@ admin.register (Comunicado)
class Comunicado(ImportExportModelAdmin):
    list_display=('title','content','dias_publicacion','publicar','comunidad','foto','order')
    list_filter=('title',)
    list_per_page = 15

class RespuestaPqrResource(resources.ModelResource):
    class Meta:
        model = RespuestaPqr
        skip_unchanged = True
        report_skipped = True
        list_display=('pqr','content','created')
        exclude = ('id')

@ admin.register (RespuestaPqr)
class RespuestaPqr(ImportExportModelAdmin):
    list_display=('pqr','content','created')
    list_filter=('content','created')
    list_per_page = 15

class ClasificadoResource(resources.ModelResource):
    class Meta:
        model = Clasificado
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','foto','title','content','user','created','updated')
        exclude = ('id')

@ admin.register (Clasificado)
class Clasificado(ImportExportModelAdmin):
    list_display= ('id','foto','title','content','user','created','updated')
    list_filter=('user','created','updated')
    list_per_page = 15

class PqrResource(resources.ModelResource):
    class Meta:
        model = Pqr
        skip_unchanged = True
        report_skipped = True
        list_display= ('title','content','interior','apartamento','foto','order','created','updated','recibida','fecha_respuesta')
        exclude = ('id')

@ admin.register (Pqr)
class Pqr(ImportExportModelAdmin):
    list_display= ('title','content','interior','apartamento','foto','order','created','updated','recibida','fecha_respuesta')
    list_filter=('title','content','interior','apartamento','recibida','fecha_respuesta')
    list_per_page = 15

class TipoPqrResource(resources.ModelResource):
    class Meta:
        model = TipoPqr
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','descripcion',)
        exclude = ('id')

@ admin.register (TipoPqr)
class TipoPqr(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15    

class NormatividadResource(resources.ModelResource):
    class Meta:
        model = Normatividad
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','title','order')
        exclude = ('id')

@ admin.register (Normatividad)
class Normatividad(ImportExportModelAdmin):
    list_display= ('id','title','order')
    list_filter=('title',)
    list_per_page = 15  

    