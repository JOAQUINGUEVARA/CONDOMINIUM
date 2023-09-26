from django.contrib import admin
from .models import Apartamento,Interior,Parqueadero,Deposito,Inmobiliaria,Residente,TipoIngreso,Autorizado,IngresoPeatonal,TipoActivo,ActivoFijo,Proyecto,ProponenteProyecto
from .models import IngresoVehiculo,Vehiculo,Vigilante,Visitante,Mascota,Correspondencia,Conjunto,ZonaComun,UserPerfil,TipoIdentificacion,Proveedor,ServicioProveedor,MiembroConsejo
from .models import Contrato,Mantenimiento,TipoContrato,Parqueadero,Vehiculo,VisitanteVehiculo,AutorizacionVehiculo,PrestamoActivoFijo,Proponente,Contrato,Reparacion,TipoProyecto
from .models import TipoAutoriza,TipoPlataformaWeb,PlataformaWebVehiculo,PlataformaWebPeatonal,AvanceObra,ReunionConsejo,CompromisoConsejo,DecisionConsejo,MiembroStaff,InformeRevisor
from .models import MiembroComiteConvivencia,RecomendacionRevisor,TipoProceso,ProcesoJuridico,GestionProcesoJuridico,TipoAsamblea,Asamblea,DecisionAsamblea,Reservas
from .models import ProponenteProyecto,Obra
from import_export.admin import ImportExportModelAdmin
from import_export import fields,resources
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from django.conf.locale.es import formats as es_formats
es_formats.DATE_FORMAT = 'd-m-y'

# Register your models here.

class ConjuntoAdmin(admin.ModelAdmin):
    list_display= ('id','nombre','razon_social','direccion','telefono','nombre_administrador','numero_unidades','estrato','email','pagina_web','foto')

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


class TipoIngresoResource(resources.ModelResource):
    class Meta:
        model = TipoIngreso
        skip_unchanged = True
        report_skipped = True
        fields = ('id','descripcion')
        exclude = ('id')

@ admin.register (TipoIngreso)
class TipoIngreso(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15


class AutorizadoResource(resources.ModelResource):
    class Meta:
        model = Autorizado
        skip_unchanged = True
        report_skipped = True
        fields = ('id','identificacion','nombre','tipo_autoriza','foto','interior','apartamento',)
        exclude = ('id')

@ admin.register (Autorizado)
class Autorizado(ImportExportModelAdmin):
    list_display= ('id','identificacion','nombre','tipo_autoriza','foto','interior','apartamento',)
    list_filter=('identificacion','nombre','tipo_autoriza','interior','apartamento',)
    list_per_page = 15

class IngresoPeatonalResource(resources.ModelResource):
    class Meta:
        model = IngresoPeatonal
        skip_unchanged = True
        report_skipped = True
        fields = ('id','identificacion','tipoingreso','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
        exclude = ('id')

@ admin.register (IngresoPeatonal)
class IngresoPeatonal(ImportExportModelAdmin):
    list_display= ('id','identificacion','tipoingreso','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_filter=('identificacion','tipoingreso','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_per_page = 15


class VigilanteResource(resources.ModelResource):
    class Meta:
        model = Vigilante
        skip_unchanged = True
        report_skipped = True
        fields = ('id','nombre')
        exclude = ('id')

@ admin.register (Vigilante)
class Vigilante(ImportExportModelAdmin):
    list_display= ('id','nombre',)
    list_filter=('nombre',)
    list_per_page = 15

class VisitanteResource(resources.ModelResource):
    class Meta:
        model = Visitante
        skip_unchanged = True
        report_skipped = True
        fields = ('id','identificacion','nombre','foto',)
        exclude = ('id')

@ admin.register (Visitante)
class Visitante(ImportExportModelAdmin):
    list_display= ('id','identificacion','nombre','foto',)
    list_filter=('identificacion','nombre',)
    list_per_page = 15


class IngresoVehiculoResource(resources.ModelResource):
    class Meta:
        model = IngresoVehiculo
        skip_unchanged = True
        report_skipped = True
        fields = ('id','placa','tipo_autoriza','foto','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
        exclude = ('id')

@ admin.register (IngresoVehiculo)
class IngresoVehiculo(ImportExportModelAdmin):
    list_display= ('id','placa','tipo_autoriza','foto','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_filter=('placa','tipo_autoriza','foto','vigilante','hora_ingreso','hora_salida','interior','apartamento',)
    list_per_page = 15

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

class CorrespondenciaResource(resources.ModelResource):
    class Meta:
        model = Correspondencia
        skip_unchanged = True
        report_skipped = True
        fields = ('id','remitente','destinatario','clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento',)
        exclude = ('id')

@ admin.register (Correspondencia)
class Correspondencia(ImportExportModelAdmin):
    list_display= ('id','remitente','destinatario','clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento',)
    list_filter=('remitente','destinatario','clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento',)
    list_per_page = 15

class ZonaComunResource(resources.ModelResource):
    class Meta:
        model = ZonaComun
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','foto','descripcion','observaciones')
        exclude = ('id')

@ admin.register (ZonaComun)
class ZonaComun(ImportExportModelAdmin):
    list_display= ('id','foto','descripcion','observaciones')
    list_filter=('descripcion',)
    list_per_page = 15


""" class UserPerfilAdmin(admin.ModelAdmin):
    list_display= ('id','interior','apartamento')
    list_filter=('interior','apartamento')

admin.site.register(UserPerfil, UserPerfilAdmin) """

class TipoAutorizaResource(resources.ModelResource):
    class Meta:
        model = TipoAutoriza
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','descripcion',)
        exclude = ('id')

@ admin.register (TipoAutoriza)
class TipoAutoriza(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15

""" class PlataformaWebPeatonalAdmin(admin.ModelAdmin):
    list_display= ('id','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')
    list_filter=('identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')

admin.site.register(PlataformaWebPeatonal, PlataformaWebPeatonalAdmin)

class PlataformaWebVehiculoAdmin(admin.ModelAdmin):
    list_display= ('id','placa','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')
    list_filter=('placa','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_plataforma')

admin.site.register(PlataformaWebVehiculo, PlataformaWebVehiculoAdmin) """

class TipoIdentificacionResource(resources.ModelResource):
    class Meta:
        model = TipoIdentificacion
        skip_unchanged = True
        report_skipped = True
        fields = ('id','descripcion')
        exclude = ('id')

@ admin.register (TipoIdentificacion)
class TipoIdentificacion(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15

class TipoActivoResource(resources.ModelResource):
    class Meta:
        model = TipoActivo
        skip_unchanged = True
        report_skipped = True
        fields = ('id','descripcion')
        exclude = ('id')

@ admin.register (TipoActivo)
class TipoActivo(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15


class ActivoFijoResource(resources.ModelResource):
    class Meta:
        model = ActivoFijo
        skip_unchanged = True
        report_skipped = True
        fields = ('id','nombre','tipo_activo','descripcion','marca','serial','foto','valor_libros','cantidad','mantenimiento','frecuencia_mantenimiento','ultimo_mantenimiento','placa_numero')
        exclude = ('id')

@ admin.register (ActivoFijo)
class ActivoFijo(ImportExportModelAdmin):
    list_display= ('id','nombre','tipo_activo','descripcion','marca','serial','foto','valor_libros','cantidad','mantenimiento','frecuencia_mantenimiento','ultimo_mantenimiento','placa_numero')
    list_filter=('nombre','tipo_activo','marca','serial','mantenimiento','ultimo_mantenimiento','placa_numero')
    list_per_page = 15


class ProveedorResource(resources.ModelResource):
    class Meta:
        model = Proveedor
        skip_unchanged = True
        report_skipped = True
        fields = ('id','cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto')
        exclude = ('id')

@ admin.register (Proveedor)
class Proveedor(ImportExportModelAdmin):
    list_display= ('id','cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto')
    list_filter=('nombre','servicio_provee')
    list_per_page = 15

class ServicioProveedorResource(resources.ModelResource):
    class Meta:
        model = ServicioProveedor
        skip_unchanged = True
        report_skipped = True
        fields = ('id','descripcion')
        exclude = ('id')

@ admin.register (ServicioProveedor)
class ServicioProveedor(ImportExportModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15

class MantenimientoResource(resources.ModelResource):
    class Meta:
        model = Mantenimiento
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado')
        exclude = ('id')

@ admin.register (Mantenimiento)
class Mantenimiento(ImportExportModelAdmin):
    list_display= ('id','fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado')
    list_filter=('fecha','activo_fijo','proveedor','descripcion','contrato','calificacion','terminado')
    list_per_page = 15


class ContratoResource(resources.ModelResource):
    class Meta:
        model = Contrato
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','proveedor','objeto','fecha_contrato','valor','descripcion','vigencia','activo')
        exclude = ('id')

@ admin.register (Contrato)
class Contrato(ImportExportModelAdmin):
    list_display= ('id','proveedor','objeto','fecha_contrato','valor','descripcion','vigencia','activo')
    list_filter=('proveedor','objeto','fecha_contrato','valor','descripcion','vigencia','activo')
    list_per_page = 15

class MiembroConsejoResource(resources.ModelResource):
    class Meta:
        model = MiembroConsejo
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','interior','apartamento','nombre','cargo','email','envio','activo','contenido','orden')
        exclude = ('id')

@ admin.register (MiembroConsejo)
class MiembroConsejo(ImportExportModelAdmin):
    list_display= ('id','interior','apartamento','nombre','cargo','email','envio','activo','contenido','orden')
    list_filter=('nombre',)
    list_per_page = 15


class TipoContratoResource(resources.ModelResource):
    class Meta:
        model = TipoContrato
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','descripcion',)
        exclude = ('id')

@ admin.register (TipoContrato)
class TipoContrato(ImportExportModelAdmin):
    list_display= ('descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15


class TipoPlataformaWebAdmin(admin.ModelAdmin):
    list_display= ('id','descripcion',)
    list_filter=('descripcion',)

admin.site.register(TipoPlataformaWeb,TipoPlataformaWebAdmin)

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

class VisitanteVehiculoResource(resources.ModelResource):
    class Meta:
        model = VisitanteVehiculo
        skip_unchanged = True
        report_skipped = True
        list_display= ('placa','identificacion','nombre')
        exclude = ('id')

@ admin.register (VisitanteVehiculo)
class VisitanteVehiculo(ImportExportModelAdmin):
    list_display= ('placa','identificacion','nombre')
    list_filter=('placa','identificacion')
    list_per_page = 15

class AutorizacionVehiculoResource(resources.ModelResource):
    class Meta:
        model = AutorizacionVehiculo
        skip_unchanged = True
        report_skipped = True
        list_display= ('placa','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_autoriza')
        exclude = ('id')

@ admin.register (AutorizacionVehiculo)
class AutorizacionVehiculo(ImportExportModelAdmin):
    list_display= ('placa','identificacion','nombre','fecha_inicial','fecha_final','interior','apartamento','tipo_autoriza')
    list_filter=('placa','identificacion','fecha_inicial','fecha_final','interior','apartamento',)
    list_per_page = 15

class ProponenteResource(resources.ModelResource):
    class Meta:
        model = Proponente
        skip_unchanged = True
        report_skipped = True
        list_display= ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
        exclude = ('id')

@ admin.register (Proponente)
class Proponente(ImportExportModelAdmin):
    list_display= ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
    list_filter=('cc_nit','tipo_identificacion','servicio_provee','nombre','persona_contacto','calificacion')
    list_per_page = 15

class ReparacionResource(resources.ModelResource):
    class Meta:
        model = Reparacion
        skip_unchanged = True
        report_skipped = True
        list_display= ('descripcion','valor','valor_anticipo','observacion','calificacion','fecha_terminacion','terminado')
        exclude = ('id')

@ admin.register (Reparacion)
class Reparacion(ImportExportModelAdmin):
    list_display= ('descripcion','valor','valor_anticipo','observacion','calificacion','fecha_terminacion','terminado')
    list_filter=('fecha','proveedor','descripcion','observacion','calificacion','fecha_terminacion','terminado')
    list_per_page = 15

class TipoProyectoResource(resources.ModelResource):
    class Meta:
        model = TipoProyecto
        skip_unchanged = True
        report_skipped = True
        list_display= ('descripcion',)
        exclude = ('id')

@ admin.register (TipoProyecto)
class TipoProyecto(ImportExportModelAdmin):
    list_display= ('descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15

class ProyectoResource(resources.ModelResource):
    class Meta:
        model = Proyecto
        skip_unchanged = True
        report_skipped = True
        list_display= ('fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto')
        exclude = ('id')

@ admin.register (Proyecto)
class Proyecto(ImportExportModelAdmin):
    list_display= ('fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto')
    list_filter=('fecha','tipo_proyecto','descripcion','aprobado',)
    list_per_page = 15

class ProponenteProyectoResource(resources.ModelResource):
    class Meta:
        model = ProponenteProyecto
        skip_unchanged = True
        report_skipped = True
        ist_display= ('proyecto','proponente','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra')
        exclude = ('id')

@ admin.register (ProponenteProyecto)
class ProponenteProyecto(ImportExportModelAdmin):
    list_display= ('proyecto','proponente','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra')
    list_filter=('proyecto','proponente','fecha','descripcion','seleccionado','fecha_seleccion','votos_favor','votos_contra',)
    list_per_page = 15

class ObraResource(resources.ModelResource):
    class Meta:
        model = Obra
        skip_unchanged = True
        report_skipped = True
        list_display= ('fecha','proveedor','interventor','descripcion','contrato','valor','valor_anticipo','valor_pagado','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada')
        exclude = ('id')

@ admin.register (Obra)
class Obra(ImportExportModelAdmin):
    list_display= ('fecha','proveedor','interventor','descripcion','contrato','valor','valor_anticipo','valor_pagado','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada')
    list_filter=('fecha','proveedor','interventor','descripcion','contrato','saldo_pagar','avance_obra','fecha_terminacion','calificacion','terminada',)
    list_per_page = 15

class AvanceObraResource(resources.ModelResource):
    class Meta:
        model = AvanceObra
        skip_unchanged = True
        report_skipped = True
        list_display= ('obra','fecha','descripcion','valor','porcentaje_avance')
        exclude = ('id')

@ admin.register (AvanceObra)
class AvanceObra(ImportExportModelAdmin):
    list_display= ('obra','fecha','descripcion','valor','porcentaje_avance')
    list_filter=('obra','fecha','descripcion','valor','porcentaje_avance',)
    list_per_page = 15

class ReunionConsejoResource(resources.ModelResource):
    class Meta:
        model = ReunionConsejo
        skip_unchanged = True
        report_skipped = True
        list_display= ('fecha','contenido','numero_acta','hora_inicio','hora_final')
        exclude = ('id')

@ admin.register (ReunionConsejo)
class ReunionConsejo(ImportExportModelAdmin):
    list_display= ('fecha','contenido','numero_acta','hora_inicio','hora_final')
    list_filter=('fecha','contenido','numero_acta',)
    list_per_page = 15


class CompromisoConsejoResource(resources.ModelResource):
    class Meta:
        model = CompromisoConsejo
        skip_unchanged = True
        report_skipped = True
        list_display= ('reunion_consejo','compromiso','cumplido','fecha_cumplido')
        exclude = ('id')

@ admin.register (CompromisoConsejo)
class CompromisoConsejo(ImportExportModelAdmin):
    list_display= ('reunion_consejo','compromiso','cumplido','fecha_cumplido')
    list_filter=('reunion_consejo','compromiso','cumplido','fecha_cumplido',)
    list_per_page = 15

class DecisionConsejoResource(resources.ModelResource):
    class Meta:
        model = DecisionConsejo
        skip_unchanged = True
        report_skipped = True
        list_display= ('reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion')
        exclude = ('id')

@ admin.register (DecisionConsejo)
class DecisionConsejo(ImportExportModelAdmin):
    list_display= ('reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion')
    list_filter=('reunion_consejo','decision','numero_votos_favor','numero_votos_contra','numero_votos_abstencion',)
    list_per_page = 15


class MiembroComiteConvivenciaResource(resources.ModelResource):
    class Meta:
        model = MiembroComiteConvivencia
        skip_unchanged = True
        report_skipped = True
        list_display= ('id','nombre','email','envio','publicar','comunidad')
        exclude = ('id')

@ admin.register (MiembroComiteConvivencia)
class MienbroComiteConvivencia(ImportExportModelAdmin):
    list_display= ('id','nombre','email','envio','publicar','comunidad')
    list_filter=('nombre','email',)
    list_per_page = 15

class MiembroStaffResource(resources.ModelResource):
    class Meta:
        model = MiembroStaff
        skip_unchanged = True
        report_skipped = True
        list_display= ('nombre','email','envio','publicar','comunidad','foto','orden')
        exclude = ('id')

@ admin.register (MiembroStaff)
class MienbroStaff(ImportExportModelAdmin):
    list_display= ('id','nombre','email','envio','publicar','comunidad')
    list_filter=('nombre','orden',)
    list_per_page = 15

class InformeRevisorResource(resources.ModelResource):
    class Meta:
        model = InformeRevisor
        skip_unchanged = True
        report_skipped = True
        list_display= ('fecha','contenido')
        exclude = ('id')

@ admin.register (InformeRevisor)
class InformeRevisor(ImportExportModelAdmin):
    list_display= ('fecha','contenido')
    list_filter=('fecha','contenido',)
    list_per_page = 15
    
class RecomendacionRevisorResource(resources.ModelResource):
    class Meta:
        model = RecomendacionRevisor
        skip_unchanged = True
        report_skipped = True
        list_display= ('informe_revisor','recomendacion','cumplido','fecha_cumplido')
        exclude = ('id')

@ admin.register (RecomendacionRevisor)
class RecomendacionRevisor(ImportExportModelAdmin):
    list_display= ('informe_revisor','recomendacion','cumplido','fecha_cumplido')
    list_filter=('informe_revisor','cumplido','fecha_cumplido')
    list_per_page = 15

class TipoProcesoResource(resources.ModelResource):
    class Meta:
        model = TipoProceso
        skip_unchanged = True
        report_skipped = True
        list_display= ('descripcion',)
        exclude = ('id')

@ admin.register (TipoProceso)
class TipoProceso(ImportExportModelAdmin):
    list_display= ('descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15

class ProcesoJuridicoResource(resources.ModelResource):
    class Meta:
        model = ProcesoJuridico
        skip_unchanged = True
        report_skipped = True
        list_display= ('proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo')
        exclude = ('id')

@ admin.register (ProcesoJuridico)
class ProcesoJuridico(ImportExportModelAdmin):
    list_display= ('proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo')
    list_filter=('proceso_numero','tipo_proceso','fecha_inicial','demandado')
    list_per_page = 15

class GestionProcesoJuridicoResource(resources.ModelResource):
    class Meta:
        model = GestionProcesoJuridico
        skip_unchanged = True
        report_skipped = True
        list_display=('fecha','titulo','proceso_juridico','gestion')
        exclude = ('id')

@ admin.register (GestionProcesoJuridico)
class GestionProcesoJuridico(ImportExportModelAdmin):
    list_display=('fecha','titulo','proceso_juridico','gestion')
    list_filter=('proceso_juridico','fecha','titulo')
    list_per_page = 15


class TipoAsambleaResource(resources.ModelResource):
    class Meta:
        model = TipoAsamblea
        skip_unchanged = True
        report_skipped = True
        list_display=('descripcion',)
        exclude = ('id')

@ admin.register (TipoAsamblea)
class TipoAsamblea(ImportExportModelAdmin):
    list_display=('descripcion',)
    list_filter=('descripcion',)
    list_per_page = 15


class AsambleaResource(resources.ModelResource):
    class Meta:
        model = Asamblea
        skip_unchanged = True
        report_skipped = True
        list_display=('fecha','tipo_asamblea','contenido','hora_inicio','hora_final','numero_acta')
        exclude = ('id')

@ admin.register (Asamblea)
class Asamblea(ImportExportModelAdmin):
    list_display=('fecha','tipo_asamblea','contenido','hora_inicio','hora_final','numero_acta')
    list_filter=('fecha','tipo_asamblea','numero_acta')
    list_per_page = 15

class DecisionAsambleaResource(resources.ModelResource):
    class Meta:
        model = DecisionAsamblea
        skip_unchanged = True
        report_skipped = True
        list_display=('asamblea','decision','numero_votos_favor','numero_votos_contra')
        exclude = ('id')

@ admin.register (DecisionAsamblea)
class DecisionAsamblea(ImportExportModelAdmin):
    list_display=('asamblea','decision','numero_votos_favor','numero_votos_contra')
    list_filter=('asamblea','decision')
    list_per_page = 15

class ReservasResource(resources.ModelResource):
    class Meta:
        model = Reservas
        skip_unchanged = True
        report_skipped = True
        list_display=('fecha','zona_comun','hora_inicio','hora_final','estado','anexo_pago','confirmada')
        exclude = ('id')

@ admin.register (Reservas)
class Reservas(ImportExportModelAdmin):
    list_display=('fecha','zona_comun','hora_inicio','hora_final','estado','anexo_pago','confirmada')
    list_filter=('fecha','zona_comun','estado','anexo_pago','confirmada')
    list_per_page = 15



 
