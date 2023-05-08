from django.contrib import admin
from pages.models import Page,Panel,Legislacion,Comunicado
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

class LegislacionAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display= ('id','title','content','order','created','updated',)
    list_filter=('id','title','content','order','created','updated',)

admin.site.register(Legislacion, LegislacionAdmin)

class ComunicadoAdmin(admin.ModelAdmin):
    readonly_fields = ('created','updated')
    list_display= ('title','content','order','created','updated',)
    list_filter=('title','content','order','created','updated',)

admin.site.register(Comunicado, ComunicadoAdmin)

