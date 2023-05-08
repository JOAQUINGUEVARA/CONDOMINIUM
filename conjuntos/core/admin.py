from django.contrib import admin
from .models import Apartamento,Interior,Parqueadero,Deposito,Inmobiliaria,Residente,TipoIngreso,Autorizado,IngresoPeatonal,TipoActivo,ActivoFijo,Proyecto,ProponenteProyecto
from .models import IngresoVehiculo,Vehiculo,Vigilante,Visitante,Mascota,Correspondencia,Conjunto,ZonaComun,UserPerfil,TipoIdentificacion,Proveedor,ServicioProveedor,MiembroConsejo
from .models import Contrato,Mantenimiento,TipoContrato,Parqueadero,Vehiculo,VisitanteVehiculo,AutorizacionVehiculo,PrestamoActivoFijo,Proponente,Contrato,Reparacion,TipoProyecto
from .models import TipoAutoriza,TipoPlataformaWeb,PlataformaWebVehiculo,PlataformaWebPeatonal,AvanceObra,ReunionConsejo,CompromisoConsejo,DecisionConsejo,MiembroStaff,InformeRevisor
from .models import MiembroComiteConvivencia,RecomendacionRevisor,TipoProceso,ProcesoJuridico,GestionProcesoJuridico,TipoAsamblea,Asamblea,DecisionAsamblea

from .models import ProponenteProyecto,Obra
from pages.models import Clasificado,Pqr,TipoPqr
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources

from django.conf.locale.es import formats as es_formats
es_formats.DATE_FORMAT = 'd-m-y'

# Register your models here.

class ConjuntoAdmin(admin.ModelAdmin):
    list_display= ('id','razon_social','direccion','telefono','nombre_administrador','numero_unidades','estrato','email','pagina_web','foto')

admin.site.register(Conjunto,ConjuntoAdmin)


class ApartamentoResource(resources.ModelResource):
    class Meta:
        model = Apartamento
        skip_unchanged = True
        report_skipped = True
        fields = ('id','interior','apartamento','numero','coeficiente')
        exclude = ('id')

@ admin.register (Apartamento)
class Apartamento(ImportExportModelAdmin):
    list_display= ('id','interior','apartamento','numero','coeficiente')
    search_fields = ['numero']
    list_per_page = 15

class InteriorResource(resources.ModelResource):
    class Meta:
        model = Interior
        skip_unchanged = True
        report_skipped = True
        fields = ('id','numero')
        exclude = ('id')

@ admin.register (Interior)
class Interior(ImportExportModelAdmin):
    list_display= ('id','numero')
    search_fields = ['numero']
    list_per_page = 15


class ParqueaderoResource(resources.ModelResource):
    class Meta:
        model = Parqueadero
        skip_unchanged = True
        report_skipped = True
        fields = ('id','numero','interior','apartamento')
        exclude = ('id')

@ admin.register (Parqueadero)
class Ciudad(ImportExportModelAdmin):
    list_display= ('id','numero','interior','apartamento')
    search_fields = ['numero']
    list_per_page = 15

class DepositoResource(resources.ModelResource):
    class Meta:
        model = Deposito
        skip_unchanged = True
        report_skipped = True
        fields = ('id','numero','valor_arriendo','interior','apartamento')
        exclude = ('id')

@ admin.register (Deposito)
class Deposito(ImportExportModelAdmin):
    list_display= ('id','numero','valor_arriendo','interior','apartamento')
    search_fields = ['numero']
    list_per_page = 15

class InmobiliariaAdmin(admin.ModelAdmin):
    list_display= ('id','nit','razon_social','nombre_contacto','email','pagina_web','interior','apartamento',)
    list_filter=('razon_social','interior','apartamento',)

admin.site.register(Inmobiliaria, InmobiliariaAdmin)

class ResidenteResource(resources.ModelResource):
    class Meta:
        model = Residente
        skip_unchanged = True
        report_skipped = True
        fields = ('id','identificacion','nombre','tipo_residente','telefono','celular','email','edad','persona_discapacitada','genero','interior','apartamento',)
        exclude = ('id')

@ admin.register (Residente)
class Residente(ImportExportModelAdmin):
    list_display= ('id','identificacion','nombre','tipo_residente','telefono','celular','email','edad','persona_discapacitada','genero','interior','apartamento',)
    search_fields = ['identificacion','nombre']
    list_per_page = 15


class TipoIngresoAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoIngreso, TipoIngresoAdmin)

class AutorizadoAdmin(admin.ModelAdmin):
    list_display= ('id','identificacion','nombre','tipo_autoriza','foto','interior','apartamento',)
    list_filter=('identificacion','nombre','tipo_autoriza','interior','apartamento',)

admin.site.register(Autorizado, AutorizadoAdmin)

class IngresoPeatonalAdmin(admin.ModelAdmin):
    list_display= ('id','identificacion','tipoingreso','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_filter=('identificacion','tipoingreso','vigilante','hora_ingreso','hora_salida','interior','apartamento',)

admin.site.register(IngresoPeatonal, IngresoPeatonalAdmin)

class VigilanteAdmin(admin.ModelAdmin):
    list_display= ('id','nombre',)
    list_filter=('nombre',)

admin.site.register(Vigilante, VigilanteAdmin)

class VisitanteAdmin(admin.ModelAdmin):
    list_display= ('id','identificacion','nombre','foto',)
    list_filter=('identificacion','nombre',)

admin.site.register(Visitante, VisitanteAdmin)

class IngresoVehiculoAdmin(admin.ModelAdmin):
    list_display= ('id','placa','tipo_autoriza','foto','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_filter=('placa','tipo_autoriza','foto','vigilante','hora_ingreso','hora_salida','interior','apartamento',)

admin.site.register(IngresoVehiculo, IngresoVehiculoAdmin)


class VehiculoResource(resources.ModelResource):
    class Meta:
        model = Vehiculo
        skip_unchanged = True
        report_skipped = True
        fields = ('id','placa','tipo_vehiculo','uso','marca','modelo','color','interior','apartamento','parqueadero')
        exclude = ('id')

@ admin.register (Vehiculo)
class Vehiculo(ImportExportModelAdmin):
    list_display= ('placa','tipo_vehiculo','interior','apartamento','parqueadero')
    search_fields = ['placa','tipo_vehiculo','interior','apartamento','parqueadero']
    list_per_page = 15

class MascotaResource(resources.ModelResource):
    class Meta:
        model = Mascota
        skip_unchanged = True
        report_skipped = True
        fields = ('id','nombre','tipo_mascota','raza','edad','interior','apartamento','parqueadero')
        exclude = ('id')

@ admin.register (Mascota)
class Mascota(ImportExportModelAdmin):
    list_display= ('id','nombre','tipo_mascota','raza','edad','interior','apartamento')
    search_fields = ['tipo_mascota','raza','edad','interior','apartamento']
    list_per_page = 15


class CorrespondenciaAdmin(admin.ModelAdmin):
    list_display= ('id','remitente','destinatario','clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento',)
    list_filter=('remitente','destinatario','clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento',)

admin.site.register(Correspondencia, CorrespondenciaAdmin)


class ZonaComunAdmin(admin.ModelAdmin):
    list_display= ('id','foto','descripcion','observaciones')
    list_filter=('descripcion',)

admin.site.register(ZonaComun, ZonaComunAdmin)

class ClasificadoAdmin(admin.ModelAdmin):
    list_display= ('id','foto','title','content','user','created','updated')
    list_filter=('user','created','updated')

admin.site.register(Clasificado, ClasificadoAdmin)

class UserPerfilAdmin(admin.ModelAdmin):
    list_display= ('id','interior','apartamento')
    list_filter=('interior','apartamento')

admin.site.register(UserPerfil, UserPerfilAdmin)

class TipoAutorizaAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoAutoriza, TipoAutorizaAdmin)

class PlataformaWebPeatonalAdmin(admin.ModelAdmin):
    list_display= ('id','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')
    list_filter=('identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')

admin.site.register(PlataformaWebPeatonal, PlataformaWebPeatonalAdmin)

class PlataformaWebVehiculoAdmin(admin.ModelAdmin):
    list_display= ('id','placa','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')
    list_filter=('placa','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')

admin.site.register(PlataformaWebVehiculo, PlataformaWebVehiculoAdmin)

class TipoIdentificacionAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoIdentificacion,TipoIdentificacionAdmin)

class TipoActivoAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoActivo,TipoActivoAdmin)

class ActivoFijoAdmin(admin.ModelAdmin):
    list_display= ('id','nombre','tipo_activo','descripcion','marca','serial','foto','valor_libros','cantidad','mantenimiento','frecuencia_mantenimiento','ultimo_mantenimiento','placa_numero')
    list_filter=('nombre','tipo_activo','marca','serial','mantenimiento','ultimo_mantenimiento','placa_numero')

admin.site.register(ActivoFijo,ActivoFijoAdmin)

class ProveedorAdmin(admin.ModelAdmin):
    list_display= ('id','cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto')
    list_filter=('nombre','servicio_provee')

admin.site.register(Proveedor,ProveedorAdmin)

class ServicioProveedorAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(ServicioProveedor,ServicioProveedorAdmin)

class MantenimientoAdmin(admin.ModelAdmin):
    list_display= ('id','fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado')
    list_filter=('fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado')

admin.site.register(Mantenimiento,MantenimientoAdmin)

class ContratoAdmin(admin.ModelAdmin):
    list_display= ('id','proveedor','objeto','fecha_contrato','valor','descripcion','vigencia','activo')
    list_filter=('proveedor','objeto','fecha_contrato','valor','descripcion','vigencia','activo')

admin.site.register(Contrato,ContratoAdmin)

class MiembroConsejoAdmin(admin.ModelAdmin):
    list_display= ('id','interior','apartamento','nombre','cargo','email','envio','activo','contenido','orden')
    list_filter=('nombre',)

admin.site.register(MiembroConsejo, MiembroConsejoAdmin)

class TipoContratoAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoContrato,TipoContratoAdmin)

class TipoPlataformaWebAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoPlataformaWeb,TipoPlataformaWebAdmin)


from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User


""" class PerfilInline(admin.StackedInline):
    model = UserPerfil
    can_delete = False
    verbose_name_plural = 'Perfil Usuario'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

admin.site.unregister(User)
admin.site.register(User, UserAdmin) """

#class SolicitudAdmin(admin.ModelAdmin):
#    #readonly_fields = ('created','updated')
#    list_display=('numero','fecha','solicitante','paciente','direccion_envio','telefono_envio','total')
#    list_filter= ('numero','fecha','solicitante','paciente',)

 
    # Para campos de seleccion multiple
    #filter_horizontal=('solicitante',)
    #raw_id_fields=('solicitud',)

class PqrAdmin(admin.ModelAdmin):
    list_display= ('title','content','interior','apartamento','foto','order','created','updated','recibida','fecha_respuesta')
    list_filter=('title','content','interior','apartamento','recibida','fecha_respuesta')

admin.site.register(Pqr, PqrAdmin)

class TipoPqrAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoPqr, TipoPqrAdmin)

class VisitanteVehiculoAdmin(admin.ModelAdmin):
    list_display= ('placa','identificacion','nombre')
    list_filter=('placa','identificacion')

admin.site.register(VisitanteVehiculo,VisitanteVehiculoAdmin)

class AutorizacionVehiculoAdmin(admin.ModelAdmin):
    list_display= ('placa','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_autoriza')
    list_filter=('placa','identificacion','fecha_inicial','fecha_final','interior','apartamento',)

admin.site.register(AutorizacionVehiculo,AutorizacionVehiculoAdmin)

class ProponenteAdmin(admin.ModelAdmin):
    list_display= ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
    list_filter=('cc_nit','tipo_identificacion','servicio_provee','nombre','persona_contacto','calificacion')

admin.site.register(Proponente,ProponenteAdmin)

class ReparacionAdmin(admin.ModelAdmin):
    list_display= ('descripcion','valor','valor_anticipo','observacion','calificacion','fecha_terminacion','terminado')
    list_filter=('fecha','proveedor','descripcion','observacion','calificacion','fecha_terminacion','terminado')

admin.site.register(Reparacion,ReparacionAdmin)

class TipoProyectoAdmin(admin.ModelAdmin):
    list_display= ('descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoProyecto,TipoProyectoAdmin)

class ProyectoAdmin(admin.ModelAdmin):
    list_display= ('fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto')
    list_filter=('fecha','tipo_proyecto','descripcion','aprobado',)

admin.site.register(Proyecto,ProyectoAdmin)

class ProponenteProyectoAdmin(admin.ModelAdmin):
    list_display= ('proyecto','proponente','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra')
    list_filter=('proyecto','proponente','fecha','descripcion','seleccionado','fecha_seleccion','votos_favor','votos_contra',)

admin.site.register(ProponenteProyecto,ProponenteProyectoAdmin)

class ObraAdmin(admin.ModelAdmin):
    list_display= ('fecha','proveedor','interventor','descripcion','contrato','valor','valor_anticipo','valor_pagado','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada')
    list_filter=('fecha','proveedor','interventor','descripcion','contrato','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada',)

admin.site.register(Obra,ObraAdmin)

class AvanceObraAdmin(admin.ModelAdmin):
    list_display= ('obra','fecha','descripcion','valor','porcentaje_avance')
    list_filter=('obra','fecha','descripcion','valor','porcentaje_avance',)

admin.site.register(AvanceObra,AvanceObraAdmin)

class ReunionConsejoAdmin(admin.ModelAdmin):
    list_display= ('fecha','contenido','numero_acta','hora_inicio','hora_final')
    list_filter=('fecha','contenido','numero_acta',)

admin.site.register(ReunionConsejo,ReunionConsejoAdmin)

class CompromisoConsejoAdmin(admin.ModelAdmin):
    list_display= ('reunion_consejo','compromiso','cumplido','fecha_cumplido')
    list_filter=('reunion_consejo','compromiso','cumplido','fecha_cumplido',)

admin.site.register(CompromisoConsejo,CompromisoConsejoAdmin)

class DecisionConsejoAdmin(admin.ModelAdmin):
    list_display= ('reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion')
    list_filter=('reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion',)

admin.site.register(DecisionConsejo,DecisionConsejoAdmin)

class ComiteConvivenciaAdmin(admin.ModelAdmin):
    list_display= ('id','nombre','email','envio','publicar','comunidad')
    list_filter=('nombre','email',)

admin.site.register(MiembroComiteConvivencia,ComiteConvivenciaAdmin)

class MiembroStaffAdmin(admin.ModelAdmin):
    list_display= ('nombre','email','envio','publicar','comunidad','foto','orden')
    list_filter=('nombre','orden',)

admin.site.register(MiembroStaff,MiembroStaffAdmin)

class InformeRevisorAdmin(admin.ModelAdmin):
    list_display= ('fecha','contenido')
    list_filter=('fecha','contenido',)

admin.site.register(InformeRevisor,InformeRevisorAdmin)

class RecomendacionRevisorAdmin(admin.ModelAdmin):
    list_display= ('informe_revisor','recomendacion','cumplido','fecha_cumplido')
    list_filter=('informe_revisor','cumplido','fecha_cumplido')

admin.site.register(RecomendacionRevisor,RecomendacionRevisorAdmin)


class TipoProcesoAdmin(admin.ModelAdmin):
    list_display= ('descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoProceso,TipoProcesoAdmin)

fields = ['proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo']

class ProcesoJuridicoAdmin(admin.ModelAdmin):
    list_display= ('proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo')
    list_filter=('proceso_numero','tipo_proceso','fecha_inicial','demandado')

admin.site.register(ProcesoJuridico,ProcesoJuridicoAdmin)

class GestionProcesoJuridicoAmin(admin.ModelAdmin):
    list_display=('fecha','titulo','proceso_juridico','gestion')
    list_filter=('proceso_juridico','fecha','titulo')

admin.site.register(GestionProcesoJuridico,GestionProcesoJuridicoAmin)   

class TipoAsambleaAdmin(admin.ModelAdmin):
    list_display=('descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoAsamblea,TipoAsambleaAdmin)

class AsambleaAdmin(admin.ModelAdmin):
    list_display=('fecha','tipo_asamblea','contenido','hora_inicio','hora_final','numero_acta')
    list_filter=('fecha','tipo_asamblea','numero_acta')

admin.site.register(Asamblea,AsambleaAdmin)

class DecisionAsambleaAdmin(admin.ModelAdmin):
    list_display=('asamblea','decision','numero_votos_favor','numero_votos_contra')
    list_filter=('asamblea','decision')
admin.site.register(DecisionAsamblea,DecisionAsambleaAdmin)    
