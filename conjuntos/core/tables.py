
from core.models import  PlataformaWebPeatonal,PlataformaWebVehiculo,Correspondencia, InformeRevisor, UserPerfil,ZonaComun,Residente,Autorizado,Mantenimiento,ActivoFijo,Proveedor,Contrato,Obra,Reparacion
from core.models import MiembroConsejo,MiembroStaff,ReunionConsejo,ProcesoJuridico,Apartamento,ResidenteTemp,Reservas,Proponente,Proyecto,ProponenteProyecto,AutorizacionVehiculo
from core.models import IngresoPeatonal,IngresoVehiculo,PrestamoActivoFijo,MiembroComiteConvivencia,BajaActivoFijo
import django_tables2 as tables
from django.utils.safestring import mark_safe
from django_tables2 import TemplateColumn,BooleanColumn
from datetime import datetime
import django_tables2
from django.contrib.humanize.templatetags.humanize import intcomma


class ColumnWithThousandsSeparator(django_tables2.Column):
    def render(self,value):
        return intcomma(value)

def highlight(self, text):
        self.text_block = strip_tags(text)
        return(text)

class CorrespondenciaTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    entregado = tables.Column(
        attrs={"td": {"id": "entregado"}})
    tipo_correspondencia = tables.Column(
        attrs={"td": {"id": "tipo_correspondencia"}})
    fechahora_entrega = tables.Column(
        attrs={"td": {"id": "fechahora_entrega"}})            
    class Meta:
        model = Correspondencia
        fields = ('clase_correspondencia','tipo_correspondencia','vigilante','fechahora_recibo','fechahora_entrega','interior','apartamento','entregado')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap-responsive.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
        
    Entregas  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEntregas" class="btn-floating btn-short waves-effect waves-light brown" href='#' type="button" class="btn btn-primary" value="entregas" ><i class="material-icons">mail</i></a>'''
        
     )

class AutorizacionesPeatonalTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    activo = tables.Column(
        attrs={"td": {"id": "activo"}})
    permanente = tables.Column(
        attrs={"td": {"id": "permanente"}})    
    class Meta:
        model = Autorizado
        fields = ('identificacion','nombre','permanente','fecha_inicial','fecha_final','apartamento','tipo_autoriza','activo')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
        
    Editar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEditar" type="submit" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "editar_autorizado_peatonal" pk=record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''
        
     )
     
    Borrar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnBorrar" type="submit" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borrar_autorizado_peatonal" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
        
     ) 


class AutorizacionVehiculoTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = AutorizacionVehiculo
        fields = ('placa','identificacion','nombre','fecha_inicial','fecha_final','apartamento','tipo_autoriza')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
        
    Editar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEditar" type="submit" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "editar_autorizado_vehicular" pk=record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''
        
     )
     
    Borrar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnBorrar" type="submit" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borrar_autorizado_vehicular" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
        
     ) 

class IngresoPeatonalTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = IngresoPeatonal
        fields = ('identificacion','nombre','tipoingreso','tipo_autoriza','hora_ingreso','hora_salida','apartamento','vigilante')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

class IngresoVehicularTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = IngresoVehiculo
        fields = ('placa','tipo_autoriza','hora_ingreso','hora_salida','apartamento','vigilante')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

class AutorizacionesPlataformaWebPeatonalTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = PlataformaWebPeatonal
        fields = ('identificacion','nombre','fecha_inicial','fecha_final','apartamento','interior')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
        
    Editar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEditar"type="submit" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "editar_autorizado_plataforma_web_peatonal" pk=record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''
        
     ) 
    Borrar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<button id = "btnBorrar"type="submit" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borrar_autorizado_plataforma_web_peatonal" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
        
     ) 

class AutorizacionesPlataformaWebVehiculoTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = PlataformaWebVehiculo
        fields = ('identificacion','nombre','fecha_inicial','fecha_final','apartamento','interior','tipo_plataforma')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
        
    Editar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEditar"type="submit" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "editar_autorizado_plataforma_web_vehiculo" pk=record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''
        
     ) 
    Borrar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<button id = "btnBorrar"type="submit" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borrar_autorizado_plataforma_web_vehiculo" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
        
     ) 

class ApartamentosTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    class Meta:
        model = Apartamento
        fields = ('id','numero')
        template_name = 'django_tables2/bootstrap-responsive.html'
        attrs = {"class": "table table-hover table-sm"}

    Seleccionar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnSelApartamento" class="close" data-dismiss="modal" aria-hidden="true" type="button" class="btn btn-primary" value="seleccionar" >✔</a>'''
    )

class ReservaZonasComunesTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
       
    class Meta:
        model = Reservas
        fields = ('zona_comun','hora_inicio','hora_final','user')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

    Pago  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnEntregas" class="close" data-dismiss="modal" aria-hidden="true" type="button" class="btn btn-primary" value="entregas" ><span class="mdi mdi-plus-circle"></span></a>'''
        
     )


""" class ReservaZonasComunesTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
       
    class Meta:
        model = ReservaZonasComunes
        fields = ('fecha','hora_inicial','minuto_inicial','hora_final','minuto_final')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Borrar  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnborrar"  data-dismiss="modal" aria-hidden="true" type="button" class="btn btn-danger" value="entregas" href="{% url 'borrar_reserva_zonas_comunes' record.id %}" ><span class="mdi mdi-delete"></span></a>''' 
    )
    Pago  = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id = "btnpago" class="close" data-dismiss="modal" aria-hidden="true" type="button" class="btn btn-success" value="entregas" ><span class="mdi mdi-plus-circle"></span></a>'''
    ) """
        
class ZonasComunesTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    reserva = tables.Column(
        attrs={"td": {"id": "arrienda"}})

    tarifa = ColumnWithThousandsSeparator()
    class Meta:
        model = ZonaComun
        fields = ('descripcion','observaciones','tarifa','arrienda','orden')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id= "BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url 'editar_zona_comun' record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''

    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrarActivo" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borrar_zona_comun" pk=record.id %}" value="editar"><i class="material-icons">delete</i><</a>'''
    )
    """ Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_zonas_comunes" record.id %}" value="upload" style="color:red"><i class="material-icons">portrait</i></a>'''
    ) """

class ResidenteTable(tables.Table):
          
    class Meta:
        model = Residente
        fields = ('interior','apartamento','identificacion','nombre','tipo_residente','telefono','celular','email')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }
     
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id= "BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url 'editar_residente' record.id %}" value="editar" ><i class="material-icons">edit</i></a>'''
    )
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "informacion_residente_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )
    Email = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEmail" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "seleccion_email_anexo" id=record.id tipomail=1 %}" value="detalle" ><i class="material-icons">email</i></a>'''
    )

class CorreosResidentesTable(tables.Table):

    envio_email = tables.Column(
        attrs={"td": {"id": "envio_email"}})
          
    class Meta:
        model = Residente
        fields = ('interior','apartamento','identificacion','nombre','email','envio_email')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }

class TokensResidentesTable(tables.Table):

    envio_token = tables.Column(
        attrs={"td": {"id": "envio_token"}})
          
    class Meta:
        model = Residente
        fields = ('interior','apartamento','identificacion','nombre','token','envio_token')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }     
    
class ResidenteTempTable(tables.Table):
          
    class Meta:
        model = ResidenteTemp
        fields = ('interior','apartamento','identificacion','nombre','tipo_residente','telefono','celular','email')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }
     
    Adicionar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "adicionar_residente_desde_temp" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )


class ResidenteTable1(tables.Table):
          
    class Meta:
        model = Residente
        fields = ('interior','apartamento','identificacion','nombre','tipo_residente','telefono','celular','email')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
    
    """ Otros_Residentes = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="otro_residente" type="button" class="btn-floating btn-short waves-effect waves-light brown" style="background-color:red;" type="submit" data-tooltip="Ingresar Otros Residentes" href="{% url "otro_residente" %}" value="editar" ><i class="material-icons">person</i></a>'''
    ) """
    Paqueaderos = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="parqueadero" type="button" style="background-color:red;" type="submit" class="btn-floating btn-short waves-effect waves-light brown" data-tooltip="Ingresar parqueaderos" href="{% url "parqueadero_residente" %}" value="editar" ><i class="material-icons">local_parking</i></a>'''
    )
    Vehículos = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="vehiculo" type="button" style="background-color:red;" type="submit" class="btn-floating btn-short waves-effect waves-light red"  data-tooltip="Ingresar Vehìculos" href="{% url "vehiculo_residente" %}" value="editar" ><i class="material-icons">directions_car</i></a>'''
    )
    Depósitos = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="parqueadero" type="button" style="background-color:red;" type="submit" class="btn-floating btn-short waves-effect waves-light orange" data-tooltip="Ingresar Parqueaderos" href="{% url "deposito_residente" %}" value="editar" style="color:red" ><i class="material-icons">storage</i></a>'''
    )
    Mascotas = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="mascota" type="button" style="background-color:red;" class="btn-floating btn-short waves-effect waves-light green" data-tooltip="Ingresar Mascotas" type="submit" href="{% url "mascota_residente" %}" value="editar" ><i class="material-icons">pets</i></a>'''
    ) 

class ResidenteOtroTable(tables.Table):
          
    class Meta:
        model = Residente
        fields = ('identificacion','nombre','tipo_residente','telefono','celular','email','edad','persona_discapacitada')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }

class UserPerfilTable(tables.Table):

    class Meta:
        model = UserPerfil
        fields = ('nombre','usuario','email','activa','clave','interior','apartamento')
        template_name = 'django_tables2/semantic.html'
        row_attrs = {
            "id": lambda record: record.pk
        }

class NumberColumn(tables.Column):
    def render(self, value):
        return '{:0.2f}'.format(value)

class ActivoFijoTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})

    prestado = tables.Column(
        attrs={"td": {"id": "prestado"}})
        
    valor_libros = ColumnWithThousandsSeparator()
    class Meta:
        model = ActivoFijo
        fields = ('nombre','tipo_activo','descripcion','marca','serial','placa_numero','valor_libros','cantidad','prestado','estado')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditarActivo" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_activo_fijo" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrarActivo" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_activo_fijo" pk=record.id %}" value="editar"><i class="material-icons">delete</i><</a>'''
    )
    Adic_Mant = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnCreaMantenimiento" type="button" class="btn-floating btn-short waves-effect waves-light blue" href="{% url 'crea_mantenimiento' %}" value="crear"><i class="material-icons">add</i></a>'''
    )
    Adic_Prestamo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnCreaPrestamo" type="button" class="btn-floating btn-short waves-effect waves-light purple" href="{% url 'crea_prestamo_activo' %}" value="crear"><i class="material-icons">add</i></a>'''
    )
    Adic_Baja = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnCreaPrestamo" type="button" class="btn-floating btn-short waves-effect waves-light cyan" href="{% url 'crea_baja_activo' %}" value="crear"><i class="material-icons">add</i></a>'''
    )
    Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_activo_fijo" record.id %}" value="borrar" style="color:red"><i class="material-icons">portrait</i></a>'''
    )

class ActivoFijo1Table(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})

    valor_libros = ColumnWithThousandsSeparator()
    class Meta:
        model = ActivoFijo
        fields = ('nombre','tipo_activo','descripcion','marca','serial','placa_numero','valor_libros','cantidad')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditarActivo" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_activo_fijo" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrarActivo" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_activo_fijo" pk=record.id %}" value="editar"><i class="material-icons">delete</i><</a>'''
    ) """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light blue" href="{% url "activos_fijos_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )
    Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_activo_fijo" record.id %}" value="borrar" style="color:red"><i class="material-icons">portrait</i></a>'''
    )
class ActivoFijo2Table(tables.Table):
          
    class Meta:
        model = ActivoFijo
        fields = ('frecuencia_mantenimiento','ultimo_mantenimiento','fecha_vence_mantenimiento','meses_sin_mantenimiento','dias_sin_mantenimiento')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

class PrestamosActivosFijosTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})      
    class Meta:
        model = PrestamoActivoFijo
        fields = ('fecha','activo_fijo','responsable','cantidad','devuelto')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrarActivo" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_prestamo_activo_fijo" pk=record.id %}" value="editar"><i class="material-icons">delete</i><</a>'''
    )
    PDF = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnReporteActivo" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "reporte_prestamos_activos_fijos_pdf" id=record.id tipo_rep=2 %}" value="editar"><i class="material-icons">print</i></a>'''
    )

class BajaActivosFijosTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})      
    class Meta:
        model = BajaActivoFijo
        fields = ('fecha','activo_fijo','detalle','cantidad','causa_baja')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrarBaja" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_baja_activo_fijo" pk=record.id %}" value="borrar"><i class="material-icons">delete</i><</a>'''
    )
    PDF = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnReporteBaja" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "reporte_bajas_activos_fijos_pdf" id=record.id tipo_rep=2 %}" value="editar"><i class="material-icons">print</i></a>'''
    )
    Adic_Anexo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnAnexos" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "upload:anexo_baja_activo_fijo" record.id %}" value="editar" style="color:red"><i class="material-icons">add_circle</i></a></td>'''
    )
class MantenimientosTable(tables.Table):
          
    class Meta:
        model = Mantenimiento
        fields = ('fecha','activo_fijo','proveedor','descripcion','contrato','calificacion')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Detalle = tables.TemplateColumn(
    '{% csrf_token %}'
    '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "mantenimientos_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )

class ProveedoresTable(tables.Table):
          
    class Meta:
        model = Proveedor
        fields = ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email','persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" type="edit" href="{% url "edita_proveedor" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_proveedor" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">delete</i></a>'''
    ) """
    """ Adic_Anexo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnAnexos" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "upload:anexo_proveedor" record.id %}" value="editar" style="color:red"><i class="material-icons">add_circle</i></a>'''
    )     """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnContratos" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "proveedor_detalle" record.id %}" value="editar" style="color:orange"><i class="material-icons">view_list</i></a>'''
    )

class ProponentesTable(tables.Table):

    id = tables.Column(
        attrs={"td": {"id": "id"}})

    class Meta:
        model = Proponente
        fields = ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" type="edit" href="{% url "edita_proponente" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    ) """
    """ Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_proponente" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">delete</i></a>'''
    )     """	
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "proponente_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )

class ProponentesTable1(tables.Table):
          
    class Meta:
        model = Proponente
        fields = ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

class ProponentesTable2(tables.Table):
          
    class Meta:
        model = Proponente
        fields = ('persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    
    Pasa_a_Proveedor = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnContratos" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "proponente_a_proveedor" record.id %}" value="editar" style="color:orange"><i class="material-icons">view_list</i></a>'''
    )

class ProponentesProyectoTable(tables.Table):

    id = tables.Column(
        attrs={"td": {"id": "id"}})
    seleccionado = tables.Column(
        attrs={"td": {"id": "seleccionado"}})  
    class Meta:
        model = ProponenteProyecto
        fields = ('proponente','fecha','descripcion','valor','seleccionado','fecha_seleccion','votos_favor','votos_contra')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" type="edit" href="{% url "edita_proponente_proyecto" record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_proponente_proyecto" record.id %}" value="editar" style="color:red"><i class="material-icons">delete</i></a>'''
    )    	
    Adic_Anexo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnAnexos" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "upload:anexo_proponente_proyecto" record.id %}" value="editar" style="color:red"><i class="material-icons">add_circle</i></a></td>'''
    )

class Proveedores1Table(tables.Table):
          
    class Meta:
        model = Proveedor
        fields = ('cc_nit','tipo_identificacion','servicio_provee','nombre','telefono','celular','direccion','email')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" type="edit" href="{% url "edita_proveedor" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_proveedor" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">delete</i></a>'''
    )
    Adic_Anexo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnAnexos" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "upload:anexo_proveedor" record.id %}" value="editar" style="color:red"><i class="material-icons">add_circle</i></a>'''
    )    
class Proveedores2Table(tables.Table):
          
    class Meta:
        model = Proveedor
        fields = ('persona_contacto','telefono_contacto','celular_contacto','email_contacto','calificacion')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
 
class ContratosTable(tables.Table):

    valor = ColumnWithThousandsSeparator()      
    class Meta:
        model = Contrato
        fields = ('numero','proveedor','tipo_contrato','objeto','fecha_contrato','valor')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "contratos_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )    	

class ProyectosTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    aprobado = tables.Column(
        attrs={"td": {"id": "aprobado"}})
    presupuesto = ColumnWithThousandsSeparator()      
    class Meta:
        model = Proyecto
        fields = ('fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange"  href="{% url "edita_proyecto" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_proyecto" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
    ) """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "proyecto_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )
    

class ProyectosDetalleTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    aprobado = tables.Column(
        attrs={"td": {"id": "aprobado"}})
    presupuesto = ColumnWithThousandsSeparator()      
    class Meta:
        model = Proyecto
        fields = ('fecha','tipo_proyecto','descripcion','aprobado','aprobado_por','fecha_aprobacion','presupuesto')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange"  href="{% url "edita_proyecto" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light red" href="{% url "borra_proyecto" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
    )
    Adic_Proponente = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnProponente" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "adiciona_proponente_proyecto" %}" value="detalle" ><i class="material-icons">person</i></a>'''
    )
    Adic_Anexo = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnAnexos" type="button" class="btn-floating btn-short waves-effect waves-light green" href="{% url "upload:anexo_proyecto" record.id %}" value="editar" style="color:red"><i class="material-icons">add_circle</i></a></td>'''
    )

class ObrasTable(tables.Table):

    valor = ColumnWithThousandsSeparator()      
    class Meta:
        model = Obra
        fields = ('fecha','proveedor','interventor','descripcion','contrato','valor','valor_anticipo','avance_obra','fecha_terminacion','calificacion','terminado')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange"  href="{% url "edita_obra" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    ) """
    """ Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_obra" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
    ) """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "obra_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )

class ReparacionesTable(tables.Table):
    terminado = tables.Column(
        attrs={"td": {"id": "terminado"}})
    valor = ColumnWithThousandsSeparator()
    valor_anticipo = ColumnWithThousandsSeparator()      
    class Meta:
        model = Reparacion
        fields = ('fecha','proveedor','descripcion','contrato','valor','valor_anticipo','observacion','calificacion','terminado')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" type="edit" href="{% url "edita_reparacion" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" type="delete" href="{% url "borra_reparacion" pk=record.id %}" value="borrar" ><i class="material-icons">delete</i></a>'''
    ) """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "reparaciones_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )

class MiembrosConsejoTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    envio = tables.Column(
        attrs={"td": {"id": "envio"}})
    activo = tables.Column(
        attrs={"td": {"id": "activo"}})
    publicar = tables.Column(
        attrs={"td": {"id": "publicar"}})
    comunidad = tables.Column(
        attrs={"td": {"id": "comunidad"}})    
    class Meta:
        model = MiembroConsejo
        fields = ('interior','apartamento','nombre','cargo','email','envio','publicar','comunidad','activo','orden')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_miembro_consejo" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_miembro_consejo" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )	 
    Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_miembro_consejo" record.id %}" value="borrar" style="color:red"><i class="material-icons">portrait</i></a>'''
    )

class ComiteConvivenciaTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    envio = tables.Column(
        attrs={"td": {"id": "envio"}})
    activo = tables.Column(
        attrs={"td": {"id": "activo"}})
    publicar = tables.Column(
        attrs={"td": {"id": "publicar"}})
    comunidad = tables.Column(
        attrs={"td": {"id": "comunidad"}})    
    class Meta:
        model = MiembroComiteConvivencia
        fields = ('interior','apartamento','nombre','email','envio','publicar','comunidad','activo','orden')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_comite_convivencia" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_comite_convivencia" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )	 
    Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_comite_convivencia" record.id %}" value="borrar" style="color:red"><i class="material-icons">portrait</i></a>'''
    )

class MiembrosStaffTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    envio = tables.Column(
        attrs={"td": {"id": "envio"}})
    publicar = tables.Column(
        attrs={"td": {"id": "publicar"}})
    comunidad = tables.Column(
        attrs={"td": {"id": "comunidad"}})        
    class Meta:
        model = MiembroStaff
        fields = ('nombre','cargo','email','envio','publicar','comunidad','orden')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_miembro_staff" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_miembro_staff" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )
    """ Foto = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnUpload" type="button" class="btn-floating btn-short waves-effect waves-light Red" href="{% url "carga_foto_miembro_staff" record.id %}" value="borrar" style="color:red"><i class="material-icons">portrait</i></a>'''
    ) """

class VigilantesTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})
    envio = tables.Column(
        attrs={"td": {"id": "envio"}})
    publicar = tables.Column(
        attrs={"td": {"id": "publicar"}})
    comunidad = tables.Column(
        attrs={"td": {"id": "comunidad"}})        
    class Meta:
        model = MiembroStaff
        fields = ('nombre','email','publicar','comunidad','orden')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }	
    Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_vigilante" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_vigilante" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )
    
class ReunionConsejoTable(tables.Table):

    class Meta:
        model = ReunionConsejo
        fields = ('fecha','numero_acta','hora_inicio','hora_final')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "detalle_reunion_consejo" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )    	    	 

class InformeRevisorTable(tables.Table):
    class Meta:
        model = InformeRevisor
        fields = ('fecha','contenido')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_informe_revisor" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_informe_revisor" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )    """ 
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "informe_revisor_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )    	

class ProcesosJuridicosTable(tables.Table):

    def render_text(self, contenido):
        return str(contenido[:30] + "...")
            
    class Meta:
        model = ProcesoJuridico
        fields = ('proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo')
        template_name = 'django_tables2/semantic.html'
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }
    """ Editar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnEditar" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "edita_proceso_juridico" pk=record.id %}" value="editar" style="color:red"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnBorrar" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borra_proceso_juridico" pk=record.id %}" value="borrar" style="color:red"><i class="material-icons">delete</i></a>'''
    )     """
    Detalle = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a id="BtnDetalle" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "proceso_juridico_detalle" record.id %}" value="detalle" ><i class="material-icons">view_headline</i></a>'''
    )    	