from .models import Correspondencia,Proyecto,Proponente,Residente,Proveedor,Contrato,Mantenimiento,Obra,Reparacion,ActivoFijo,PrestamoActivoFijo,InformeRevisor
from .models import IngresoPeatonal,IngresoVehiculo,AutorizacionVehiculo,Autorizado,ProcesoJuridico,ReunionConsejo
from pages.models import Pqr
import django_filters
from django_filters import FilterSet,DateFromToRangeFilter,DateFilter,DateRangeFilter,DateTimeFromToRangeFilter
import crispy_forms
from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Fieldset, ButtonHolder, Submit
import django_filters

class CorrespondenciaFilter(django_filters.FilterSet):
    
    fechahora_recibo = DateRangeFilter()
    fechahora_entrega =DateRangeFilter()

    class Meta:
        model =Correspondencia
        fields = ['vigilante','clase_correspondencia','tipo_correspondencia','interior','apartamento','entregado','fechahora_recibo','fechahora_entrega']

class IngresoPeatonalFilter(django_filters.FilterSet):
    
    hora_ingreso = DateRangeFilter()
    hora_salida = DateRangeFilter()
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = IngresoPeatonal
        fields = ['nombre','hora_ingreso','hora_salida','tipoingreso','apartamento','vigilante']

class IngresoVehiculoFilter(django_filters.FilterSet):
    
    hora_ingreso = django_filters.DateRangeFilter()
    hora_salida = django_filters.DateRangeFilter()
    placa = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = IngresoVehiculo
        fields = ['placa','hora_ingreso','hora_salida','apartamento','vigilante']

class AutorizadoFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    fecha_inicial = django_filters.DateRangeFilter()
    fecha_final = django_filters.DateRangeFilter()
    
    class Meta:
        model = Autorizado
        fields = ['identificacion','nombre','permanente','fecha_inicial','fecha_final','apartamento','tipo_autoriza']

class AutorizacionVehiculoFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    fecha_inicial = django_filters.DateRangeFilter()
    fecha_final = django_filters.DateRangeFilter()
    
    class Meta:
        model = AutorizacionVehiculo
        fields = ['placa','identificacion','nombre','fecha_inicial','fecha_final','apartamento','tipo_autoriza']

  
class ProyectoFilter(django_filters.FilterSet):
    
    descripcion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model =Proyecto
        fields = ['tipo_proyecto','descripcion']

class ProponenteFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    calificacion__gt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gt')
    calificacion__lt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lt')

    class Meta:
        model =Proponente
        fields = ['servicio_provee','nombre']

class ResidentesFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    identificacion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Residente
        fields = ['identificacion','nombre','apartamento','envio_email']

class ResidentesTokenFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    identificacion = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Residente
        fields = ['identificacion','nombre','apartamento','envio_token']

class ProveedorFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
    identificacion = django_filters.CharFilter(lookup_expr='icontains')
    calificacion__gt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gt')
    calificacion__lt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lt')
       
    class Meta:
        model = Proveedor
        fields = ['identificacion','nombre','servicio_provee','calificacion']

class PqrFilter(django_filters.FilterSet):
    
    created = django_filters.DateRangeFilter()
    title = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = Pqr
        fields = ['tipo_pqr','title','pendiente','apartamento','created']


class ContratosFilter(django_filters.FilterSet):
    
    proveedor__nombre = django_filters.CharFilter(lookup_expr='icontains')
    objeto = django_filters.CharFilter(lookup_expr='icontains')
    fecha_vence = django_filters.DateRangeFilter()

    class Meta:
        model = Contrato
        fields = ['proveedor','objeto','activo','meses_vence','fecha_vence','dias_vence','tipo_contrato']

class ProcesosJuridicosFilter(django_filters.FilterSet):
    
    proceso_juridico = django_filters.CharFilter(lookup_expr='icontains')
    proceso_numero = django_filters.CharFilter(lookup_expr='icontains')
    fecha_inicial = django_filters.DateRangeFilter()
    fecha_final = django_filters.DateRangeFilter()

    class Meta:
        model = ProcesoJuridico
        fields = ['proceso_numero','tipo_proceso','fecha_inicial','abogado','demandante','demandado','juzgado','contenido','interior','apartamento','fecha_final','valor_demanda','activo']

class MantenimientosFilter(django_filters.FilterSet):
    
    proveedor__nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    calificacion__gt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gt')
    calificacion__lt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lt')
    
    class Meta:
        model = Mantenimiento
        fields = ['proveedor','activo_fijo','descripcion','terminado','calificacion']


class ObraFilter(django_filters.FilterSet):
    
    proveedor__nombre = django_filters.CharFilter(lookup_expr='icontains')
    proveedor__nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    calificacion__gt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gt')
    calificacion__lt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lt')
    
    class Meta:
        model = Obra
        fields = ['proveedor','interventor','descripcion','terminada','calificacion']  

class ReparacionesFilter(django_filters.FilterSet):
    
    proveedor__nombre = django_filters.CharFilter(lookup_expr='icontains')
    descripcion = django_filters.CharFilter(lookup_expr='icontains')
    calificacion__gt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='gt')
    calificacion__lt = django_filters.NumberFilter(field_name='calificacion', lookup_expr='lt')
    
    class Meta:
        model = Reparacion
        fields = ['proveedor','fecha','descripcion','descripcion','terminado','calificacion']        

class ActivosFijosFilter(django_filters.FilterSet):
    
    nombre = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = ActivoFijo
        fields = ['nombre','tipo_activo']    

class PrestamosActivosFijosFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateRangeFilter()
    responsable = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = PrestamoActivoFijo
        fields = ['fecha','responsable','devuelto']

class BajaActivosFijosFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateRangeFilter()
    responsable = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        #model = BajaActivoFijo
        fields = ['fecha','activo_fijo','causa_baja']

class InformesRevisorFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateRangeFilter()
    contenido = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = InformeRevisor
        fields = ['fecha','contenido']

class ReunionesConsejoFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateRangeFilter()
    contenido = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = ReunionConsejo
        fields = ['fecha','contenido','numero_acta']        

class AsambleaFilter(django_filters.FilterSet):
    
    fecha = django_filters.DateRangeFilter()
    contenido = django_filters.CharFilter(lookup_expr='icontains')
        
    class Meta:
        model = ReunionConsejo
        fields = ['fecha','contenido']        