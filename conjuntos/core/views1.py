from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.base import TemplateView
from .models import IngresoPeatonal,Visitante,Correspondencia,Parametros,ZonaComun,ReservaZonasComunes
from pages.models import Panel
from .forms import VisitanteForm,DatosCorrespondenciaForm,DatosIngresoPeatonalForm,DatosReservaZonasComunesForm,FechaReservaZonasComunesForm
from .tables import CorrespondenciaTable,ZonasComunesTable,ReservaZonasComunesTable
from django.urls import reverse, reverse_lazy
from django.db.models import Q
from django.http import HttpResponseBadRequest,HttpResponse, HttpRequest, JsonResponse,HttpResponseRedirect
from django.shortcuts import redirect, get_object_or_404
from .filters import CorrespondenciaFilter
import django_filters
from django.contrib.auth import authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as do_login
from django.contrib.auth import logout as do_logout
from django.contrib.auth.forms import UserCreationForm

from django.template.loader import render_to_string
from django.core.paginator import Paginator
import datetime 
from datetime import datetime, timedelta
from django.views.decorators.csrf import csrf_exempt
from django.db.models import Subquery
from django.db.models import F, Count, Value
from datetime import date
from bootstrap_modal_forms.generic import BSModalCreateView
#from material import LayoutMixin, Layout, Fieldset, Row, Span2, Span5, Span7
#from vanilla import CreateView, DeleteView, ListView, UpdateView


class HomePageView(TemplateView):
    template_name = "core/home.html"

def register(request):
    # Creamos el formulario de autenticación vacío
    form = UserCreationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = UserCreationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():

            # Creamos la nueva cuenta de usuario
            user = form.save()

            # Si el usuario se crea correctamente 
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('main')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/register.html", {'form': form})

def login(request):
    # Creamos el formulario de autenticación vacío
    form = AuthenticationForm()
    if request.method == "POST":
        # Añadimos los datos recibidos al formulario
        form = AuthenticationForm(data=request.POST)
        # Si el formulario es válido...
        if form.is_valid():
            # Recuperamos las credenciales validadas
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Verificamos las credenciales del usuario
            user = authenticate(username=username, password=password)

            # Si existe un usuario con ese nombre y contraseña
            if user is not None:
                # Hacemos el login manualmente
                do_login(request, user)
                # Y le redireccionamos a la portada
                return redirect('main')

    # Si llegamos al final renderizamos el formulario
    return render(request, "users/login.html", {'form': form})

def logout(request):
    # Finalizamos la sesión
    do_logout(request)
    # Redireccionamos a la portada
    return redirect('home')

""" def CrearVisitanteView(request,cc):
    if request.method == "POST":  
        form = VisitanteForm(request.POST or None)
        if form.is_valid():
            try:
                object = form.save(commit=False)
                object.identificacion = cc
                object.save()
                print(cc)
                return HttpResponseRedirect(reverse('ingreso_peatonal_acceso',cc))
                #return render(request, 'core/crear_visitante.html',{'form':form})       
            except:
                pass
        else:
            form = VisitanteForm()
        return render(request, 'core/crear_visitante.html',{'form':form}) """

def CogeVarIdView(request):
    id = request.GET.get('id', None)
    parametros = Parametros()
    parametros.valor_parametro_uno = id
    parametros.user = request.user.id
    parametros.save()
    data = {'estado':True}    
    return JsonResponse(data)

def DatosVisitanteView(request):
    form =  VisitanteForm()
    context = {'form': form}
    print(context)
    html_form = render_to_string('core/crear_visitante.html',
    context,
    request=request,
    )
    return JsonResponse({'html_form': html_form})

@csrf_exempt
def GuardaDatosVisitanteView(request):
    id = request.GET.get('id', None)
    nombre = request.GET.get('nombre', None)
    visitante = Visitante()
    visitante.nombre = nombre
    visitante.identificacion = id
    visitante.save()
    data = {'id':id}
    return JsonResponse(data) 

class CrearVisitanteView(CreateView):
    model = Visitante
    template_name = 'core/crear_visitante.html'
    form_class = VisitanteForm
        
    def form_valid(self, form):
        if Parametros.objects.filter(user=self.request.user.id).exists():
            parametros = Parametros.objects.filter(user=self.request.user.id).latest('id')
            cc = parametros.valor_parametro_uno
            self.object = form.save(commit=False)
            cc = self.kwargs.get('cc')
            self.object.identificacion = cc
            self.object.save()
            Parametros.objects.filter(user=self.request.user.id).delete()
            return HttpResponseRedirect(reverse('ingreso_peatonal_acceso',cc))

def upload_image(request):
   if request.method == 'GET':
      return render(request, 'core/ingreso_peatonal.html')

class AccesosView(TemplateView):
    template_name = 'core\pagina_accesos.html'

class AccesoPeatonalView(TemplateView):
    template_name = 'core\ingreso_peatonal.html'

class AccesoVehicularView(TemplateView):
    template_name = 'core\ingreso_vehicular.html'

class ContratosView(TemplateView):
    template_name = 'core\pagina_contratos.html'

class ZonasComunesView(TemplateView):
    template_name = 'core\pagina_zonas_comunes.html'

class ProveedoresView(TemplateView):
    template_name = 'core\pagina_proveedores.html'

class InformacionGeneralView(TemplateView):
    template_name = 'core\pagina_informacion_general.html'

class MantenimientoView(TemplateView):
    template_name = 'core\pagina_mantenimiento.html'

class AsambleaView(TemplateView):
    template_name = 'core\pagina_asamblea.html'

class PqrView(TemplateView):
    template_name = 'core\pagina_pqr.html'

class JuridicoView(TemplateView):
    template_name = 'core\juridico.html'

def MainView(request):
    request.session['idzona'] = ''
    request.session['fecha'] = ''
    model = Noticias
    noticias = Noticias.objects.all()
    return render(request, "core/main.html", {'noticias':noticias})

class LegislacionView(TemplateView):
    template_name = 'core\legislacion.html'        

class AboutView(TemplateView):
    template_name = 'core\empresa.html'

class AdministradorView(TemplateView):
    template_name = 'core\pagina_administrador.html'

class VigilanciaView(TemplateView):
    template_name = 'core\pagina_vigilancia.html'

class AlertasView(TemplateView):
    template_name = 'core\pagina_alertas.html'

class VigilanteView(TemplateView):
    template_name = 'core\pagina_vigilante.html'

class PaginaCorrespondenciaView(TemplateView):
    template_name = 'core\pagina_correspondencia.html'

class IngresoCorrespondenciaView(TemplateView):
    template_name = 'core\ingreso_correspondencia.html' 

class MensajeCorrespondenciaView(TemplateView):
    template_name = 'core\mensaje_correspondencia.html'    

class CalendarioView(TemplateView):
    template_name = 'core\calendario.html'    

""" class CorrespondenciaIngresoView(CreateView):
    model = Correspondencia
    template_name = 'core/ingreso_correspondencia.html'
    form_class = IngresoCorrespondenciaForm
    success_url=reverse_lazy('ingreso_correspondencia') """


def CorrespondenciaListView(request,id):
    if id == 0:
        correspondencia = CorrespondenciaTable(Correspondencia.objects.all().order_by('-id'))
    elif id == 1:    
        correspondencia = CorrespondenciaTable(Correspondencia.objects.all().filter(entregado=False).order_by('-id'))
    elif id == 2:
        correspondencia = CorrespondenciaTable(Correspondencia.objects.all().filter(entregado=True).order_by('-id'))
    correspondencia.paginate(page=request.GET.get("page", 1), per_page=15)
    return render(request, "core/correspondencia_lista.html", {"correspondencia":correspondencia})

from .forms import CorrespondenciaListFormHelper
import django_tables2
from django_tables2.config import RequestConfig
from django_tables2 import SingleTableMixin
from django_filters.views import FilterView

""" class CorrespondenciaListView(TemplateView):
    template_name = 'core/correspondencia_lista.html'

    def get_queryset(self, **kwargs):
        return Correspondencia.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CorrespondenciaListView, self).get_context_data(**kwargs)
        filter = CorrespondenciaFilter(self.request.GET, queryset=self.get_queryset(**kwargs))
        filter.form.helper = CorrespondenciaListFormHelper()
        table = CorrespondenciaTable(filter.qs)
        RequestConfig(self.request).configure(table)
        context['filter'] = filter
        context['table'] = table
        return context """


from django_tables2 import SingleTableView

class  PagedFilteredTableView(SingleTableView):
    filter_class = None
    formhelper_class = None
    context_filter_name = 'filter'

    def get_queryset(self, **kwargs):
        qs = super( PagedFilteredTableView, self).get_queryset()
        self.filter = self.filter_class(self.request.GET, queryset=qs)
        self.filter.form.helper = self.formhelper_class()
        return self.filter.qs

    def get_table(self, **kwargs):
        table = super( PagedFilteredTableView, self).get_table()
        #RequestConfig(self.request, paginate={'page': self.kwargs['page'],
        #                    "per_page": self.paginate_by}).configure(table)
        return RequestConfig(self.request, paginate={'per_page':self.paginate_by}).configure(
            table
        )
        #return table 

    def get_context_data(self, **kwargs):
        context = super( PagedFilteredTableView, self).get_context_data()
        context[self.context_filter_name] = self.filter
        return context

class CorrespondenciaListFilterView(PagedFilteredTableView):
    model = Correspondencia
    table_class = CorrespondenciaTable
    template_name = 'core/correspondencia_lista.html'
    paginate_by = 50
    filter_class = CorrespondenciaFilter
    formhelper_class = CorrespondenciaListFormHelper

def DatosCorrespondenciaView(request):
    data = dict()
    form = DatosCorrespondenciaForm()
    context = {'form': form}
    data['html_form'] = render_to_string('core/datos_correspondencia.html',
        context,
        request=request
    )
    return JsonResponse(data)

def EntregasCorrespondenciaView(request):
    id = request.GET.get('id', None)
    id=int(id)
    data= dict()
    Correspondencia.objects.filter(id=id).update(entregado=True)
    data = {'id':id,'entregado':True}
    return JsonResponse(data)

@csrf_exempt
def GuardaDatosCorrespondenciaView(request):
    data = dict()
    clase_correspondencia = request.GET.get('clase_correspondencia', None)
    tipo_correspondencia = request.GET.get('tipo_correspondencia', None)
    interior = request.GET.get('interior', None)
    apartamento = request.GET.get('apartamento', None)
    correspondencia = Correspondencia()
    correspondencia.clase_correspondencia = clase_correspondencia
    correspondencia.tipo_correspondencia = tipo_correspondencia
    correspondencia.apartamento_id = apartamento
    correspondencia.interior_id = interior 
    correspondencia.detalle = ''
    correspondencia.destinatario =''
    correspondencia.remitente = ''
    correspondencia.entregado = False
    correspondencia.vigilante_id=request.user.id
    correspondencia.save()
    data = {'estado':True} 
    return JsonResponse(data)

def CorrespondenciaConsultaView(request):
    f = CorrespondenciaFilter(request.GET, queryset=Correspondencia.objects.all())
    return render(request, 'core/consulta_correspondencia.html', {'filter': f})    

def ReservaZonasComunesView(request):
    if request.session['idzona'] == '':
        request.session['idzona'] = 1
            
    if request.session['fecha'] == '':
        id = request.session['idzona']
        q1 = ReservaZonasComunes.objects.filter(zona_comun=id)
        #q2 = ReservaZonasComunes.objects.filter(fecha_inicial >= now)
        reserva_zonas_comunes = ReservaZonasComunesTable(ReservaZonasComunes.objects.filter(zona_comun=id).order_by('zona_comun','-fecha_inicial','horario','hora_inicial'))
        zonas_comunes = ZonasComunesTable(ZonaComun.objects.all())
        id = request.session['idzona']
        zona = ZonaComun.objects.get(id=id)
        nombreZona = zona.descripcion
        observaciones = zona.observaciones
        foto = zona.foto
        #request.session['idzona'] = ''
    else:
        fecha = request.session['fecha']
        reserva_zonas_comunes = ReservaZonasComunesTable(ReservaZonasComunes.objects.filter(fecha_inicial=fecha).order_by('zona_comun','-fecha_inicial','horario','hora_inicial'))
        zonas_comunes = ZonasComunesTable(ZonaComun.objects.all())
        id = request.session['idzona']
        zona = ZonaComun.objects.get(id=id)
        nombreZona = zona.descripcion
        observaciones = zona.observaciones
        foto = zona.foto
    request.session['fecha'] = ''        
    return render(request, "core/reserva_zonas_comunes.html", {"nombreZona":nombreZona,"zonas_comunes":zonas_comunes,"reserva_zonas_comunes":reserva_zonas_comunes,"foto":foto,'observaciones':observaciones})

def FiltroZonasComunesView(request,id):
    request.session['idzona'] = id
    return HttpResponseRedirect(reverse('reserva_zonas_comunes'))

def FiltrarFechaReservaZonasComunes(request):
    fecha = request.GET.get('fecha', None)
    request.session['fecha'] = fecha
    data= dict()
    numres =  ReservaZonasComunes.objects.filter(fecha_inicial=fecha).count()
    data = {'estado':numres}
    return JsonResponse(data)

""" def FechaReservaZonasComunesView(request):
    data = dict()
    form = FechaReservaZonasComunesForm()
    context = {'form': form}
    data['html_form'] = render_to_string('core/filtro_fecha_reserva_zonas_comunes.html',
        context,
        request=request
    )
    return JsonResponse(data) """

class  CrearReservaZonasComunesView(BSModalCreateView):
    template_name = 'core/crea_reserva_zonas_comunes.html'
    form_class = DatosReservaZonasComunesForm
    success_message = 'Success: Reserva fué creada'
    #success_url = reverse_lazy('reserva_zonas_comunes')

    def form_valid(self, form):
        reserva = form.save(commit=False)
        hora_inicial = reserva.hora_inicial
        horas = reserva.horas
        if reserva.horario == 'PM':
            hora_inicial = hora_inicial+12    
        hora_final = hora_inicial+horas
        hora_inicial_cont = hora_inicial
        sw = 0
        while hora_inicial_cont <= hora_final:
            anio_actual = reserva.fecha_inicial.year
            mes_actual = reserva.fecha_inicial.month
            dia_actual = reserva.fecha_inicial.day
            fecha_hora_inicial_d = datetime(anio_actual, mes_actual, dia_actual, hora_inicial, 00, 00, 00000)
            fecha_hora_final_d = datetime(anio_actual, mes_actual, dia_actual, hora_final, 00, 00, 00000)
            reserva.fecha_hora_inicial=fecha_hora_inicial_d
            reserva.fecha_hora_final=fecha_hora_final_d
            reserva.residente_id=self.request.user.id
            nzona = reserva.zona_comun
            fecha_inicial = reserva.fecha_inicial
            zona = ZonaComun.objects.get(descripcion=nzona)
            #self.request.session['fecha'] = fecha_inicial
            if ReservaZonasComunes.objects.filter(zona_comun_id=zona.id).filter(fecha_inicial=fecha_inicial).exists():
                reservas =  ReservaZonasComunes.objects.filter(zona_comun_id=zona.id).filter(fecha_inicial=fecha_inicial)  
                if hora_inicial_cont in reservas.hora_inicial:
                   mensage='Hora ya asignada'
                   sw = 1
                   hora_inicial_cont = hora_final
                   return render(self.request, "core/mensaje_error_reserva.html", {'mensaje': mensage,'parametro':zona.id})
            hora_inicial_cont += 1              
        if sw == 0:
            reserva.save()
        self.request.session['idzona'] = zona.id
        return HttpResponseRedirect(reverse('reserva_zonas_comunes'))
        

    def get_success_url(self):
        idzona = self.request.session['idzona']
        return reverse_lazy('reserva_zonas_comunes')


def DatosReservaZonasComunesView(request):
    data = dict()
    form = DatosReservaZonasComunesForm()
    context = {'form': form}
    data['html_form'] = render_to_string('core/crea_reserva_zonas_comunes.html',
        context,
        request=request
    )
    return JsonResponse(data)

def GuardaDatosReservaZonasComunesView(request):
    data = dict()
    zona_comun = request.GET.get('zona_comun', None)
    fecha_inicial_str = request.GET.get('fecha_inicial', None)
    horas = request.GET.get('horas', None)
    interior = request.GET.get('interior', None)
    apartamento = request.GET.get('apartamento', None)
    hora_inicial = request.GET.get('hora_inicial', None)
    horario = request.GET.get('horario', None)
    reserva = ReservaZonasComunes()
    if horario == 'PM':
       hora_inicial = hora_inicial+12    
    hora_final = hora_inicial+horas    
    anio_actual = reserva.fecha_inicial.year
    mes_actual = reserva.fecha_inicial.month
    dia_actual = reserva.fecha_inicial.day
    fecha_inicial = datetime.datetime.strptime(fecha_inicial_str,"%m/%d/%Y").date()
    fecha_hora_inicial_d = datetime(anio_actual, mes_actual, dia_actual, hora_inicial, 00, 00, 00000)
    fecha_hora_final_d = datetime(anio_actual, mes_actual, dia_actual, hora_final, 00, 00, 00000)
    reserva.fecha_inicial = fecha_inicial
    reserva.fecha_hora_inicial = fecha_hora_inicial_d
    reserva.fecha_hora_final = fecha_hora_final_d
    reserva.residente_id = request.user.id
    reserva.zona_comun = zona_comun
    reserva.fecha_inicial = fecha_inicial
    reserva.horas =horas
    reserva.fecha_hora_inicial =fecha_hora_inicial_d
    reserva.fecha_hora_final = fecha_hora_final_d
    reserva.apartamento_id = apartamento
    reserva.interior_id = interior 
    reserva.residente_id=request.user.id
    if ReservaZonasComunes.objects.filter(zona_comun_id=zona.id).filter(fecha_inicial=fecha_inicial).exists():
        reservas =  ReservaZonasComunes.objects.filter(zona_comun_id=zona.id).filter(fecha_inicial=fecha_inicial)  
        for i in reservas:
            if hora_inicial >= int(i.fecha_hora_inicial.strftime("%X")[0:2]) and hora_inicial < int(i.fecha_hora_final.strftime("%X")[0:2]): 
                #mensage='Hora ya asignada'
                #return render(self.request, "core/mensaje_error_reserva.html", {'mensaje': mensage,'parametro':zona.id})
                data = {'estado':False} 
            else:
                reserva.save()
                data = {'estado':True} 
    else:
        reserva.save()
    data = {'estado':True} 
    return JsonResponse(data)

def IngresoPeatonalBusquedaView(request):
    if request.method == 'GET':
        #form_class = IngresoPeatonalForm
        query= request.GET.get('q')
        submitbutton= request.GET.get('submit')
        #if query is not None:
        lookups= Q(identificacion__icontains=query)
        results= Visitante.objects.filter(lookups).distinct()
        context={'results': results,'submitbutton': submitbutton}
        context['ingresos'] = IngresoPeatonal.objects.filter(identificacion=query).order_by('-id')[:5]
        return render(request,'core/ingreso_peatonal.html', context)
    else:
        return render(request, 'core/ingreso_peatonal.html')

def DatosIngresoPeatonalView(request):
    data = dict()
    form = DatosIngresoPeatonalForm()
    context = {'form': form}
    data['html_form'] = render_to_string('core/datos_ingreso_peatonal.html',
        context,
        request=request
    )
    return JsonResponse(data)

@csrf_exempt
def GuardaDatosIngresoPeatonalView(request):
    id = request.GET.get('id', None)
    tipoingreso = request.GET.get('tipoingreso', None)
    interior = request.GET.get('interior', None)
    apartamento = request.GET.get('apartamento', None)
    ingreso_peatonal = IngresoPeatonal()
    ingreso_peatonal.identificacion_id = id
    ingreso_peatonal.tipoingreso_id = tipoingreso
    ingreso_peatonal.interior_id = interior
    ingreso_peatonal.apartamento_id = apartamento
    ingreso_peatonal.vigilante_id=request.user.id
    ingreso_peatonal.save()
    data = {'id':id}
    return JsonResponse(data) 

""" def IngresoPeatonalViewP(request,cc):
    if request.method == "POST":  
        form = IngresoPeatonalFormP(request.POST or None)
        if form.is_valid():
            try:
                object = form.save(commit=False)
                object.identificacion_id = cc
                object.vigilante_id=request.user.id
                object.save()
                return HttpResponseRedirect('acceso_peatonal',cc)
            except:
                pass
        else:
            form = VisitanteForm()
        return render(request, 'core/ingreso_peatonal_p.html',{'form':form}) """

""" class IngresoPeatonalViewP(CreateView):
    model = IngresoPeatonal
    template_name = 'core/ingreso_peatonal_p.html'
    form_class = IngresoPeatonalFormP
    #success_url=reverse_lazy('acceso_peatonal')
    
    def form_valid(self, form):
        if form.is_valid():
            object = form.save(commit=False)
            cc = self.kwargs.get("cc")
            object.identificacion_id = cc
            object.vigilante_id=self.request.user.id
            object.save()
            return HttpResponseRedirect(reverse_lazy('acceso_peatonal'))
        else:
            messageform='Información Inválida'
            return render(self.request, "core/mensaje_error.html", {'form': messageform})
        return HttpResponseRedirect('acceso_peatonal')
 """
class SuccessView(TemplateView):
    template_name = 'core\success.html'

class ResidenteView(TemplateView):
    template_name = 'core\pagina_residente.html'

class BlogView(TemplateView):
    template_name = 'core\blog.html'

class ConsejeroView(TemplateView):
    template_name = 'core\pagina_consejero.html'