from django.shortcuts import render
from django.template import RequestContext
from django.shortcuts import render, get_object_or_404,redirect
from .models import Page,Panel,Legislacion,Pqr,Clasificado, RespuestaPqr,Comunicado,Normatividad
from core.models import Autorizado,PlataformaWebVehiculo,PlataformaWebPeatonal,Conjunto,Apartamento,Residente
from django.views.generic.list import ListView
from django.views.generic.edit import CreateView,UpdateView,DeleteView
from django.core.paginator import Paginator,EmptyPage, PageNotAnInteger
from .forms import PQRForm,RespuestaPQRForm,ClasificadosForm,AnexoFotoClasificadoForm,RespuestaPQRForm,LegislacionForm,ComunicadoForm,ClasificadosForm,NormatividadForm
from django.urls import reverse,reverse_lazy
from django.http import HttpResponseRedirect,JsonResponse
from .tables import PqrTable,LegislacionTable,ComunicadosTable
from django.views.generic.base import TemplateView
from datetime import datetime,timedelta
from upload.models import AnexoLegislacion,AnexoNormatividad,AnexoComunicado
from django.template.loader import render_to_string
from core.filters import PqrFilter
from django.contrib import messages
from django.conf import settings
from django.core.mail import EmailMessage,send_mass_mail,BadHeaderError,send_mail
from django_tables2.config import RequestConfig


def page(request, page_id, page_slug):
    page = get_object_or_404(Page, id=page_id)
    return render(request,'pages/pages_listado.html', {'page':page})

class PageListView(ListView):
    model = Page

def panel(request, page_id, page_slug):
    panel = get_object_or_404(Panel, id=page_id)
    return render(request,'pages/panel_listado.html', {'panel':panel})

class PanelistView(ListView):
    model = Panel    

def LegislacionListView(request):
    legislacion = Legislacion.objects.all()
    return render(request, "core/pagina_legislacion.html", {'legislacion':legislacion})

def LegislacionPaginasView(request, legislacion_id, legislacion_slug ):
    #legislacion= get_object_or_404(Legislacion, id=legislacion_id)
    legislacion=Legislacion.objects.filter(id=legislacion_id)
    paginator = Paginator(legislacion,1)
    page = request.GET.get(1)
    try:
        legislacion = paginator.page(page)
    except PageNotAnInteger:
        # If page is not an integer, deliver first page.
        legislacion = paginator.page(1)
    except EmptyPage:
        # If page is out of range (e.g. 9999), deliver last page of results.
        legislacion = paginator.page(paginator.num_pages)

    return render(request,'pages/lista_legislacion.html', {"legislacion": legislacion})
    

""" def PqrResidenteListView(request,id):
    pqr =PqrTable(Pqr.objects.filter(residente_id=id).order_by('-created'))
    return render(request, "pages/Reservas.html", {"pqr":pqr}) """

def PqrDetalleView(request,id):
    pqr =Pqr.objects.filter(id=id)
    return render(request, "pages/pqr_detalle.html", {"pqr":pqr})

def PqrListaView(request):
    queryset = Pqr.objects.select_related().all()
    f = PqrFilter(request.GET, queryset=queryset)
    pqr =PqrTable(f.qs)
    return render(request, "pages/pqr_lista.html", {"pqr":pqr,'filter':f})

    
class CreaPQRView(CreateView):
    model = Pqr
    template_name = 'pages/pqr_form.html'
    form_class = PQRForm
    
    def form_valid(self, form):
        pqr = form.save(commit=False)
        pqr.user_id = self.request.user.id
        pqr.save()
        pqr = Pqr.objects.latest('id')
        conjunto = Conjunto.objects.latest('id')
        email_sol = conjunto.email
        apartamento = Apartamento.objects.get(id=pqr.apartamento_id)
        message ="Sr. Administrador, le ha sido enviada una PQR del Apartamento :"+apartamento.numero
        subject = "PQR "+pqr.title
        from_email = settings.EMAIL_HOST_USER
        mail = EmailMessage(
        subject,
        message,
        from_email,
        to=[email_sol],
        bcc=None,
        )
        mail.send()
        tipo_usuario = self.request.session['tipo_usuario']
        return redirect('user_home',tipo_usuario)

def VerDetallePqrView(request,id):
    pqr = Pqr.objects.filter(id=id)
    return render(request, "pages/pqr_detalle.html", {"pqr":pqr})

def VerRespuestaPqrView(request,id):
    pqr_id = Pqr.objects.get(id=id)
    pqr = Pqr.objects.filter(id=id)
    if RespuestaPqr.objects.filter(pqr_id=pqr_id).exists():
        respuesta_pqr = RespuestaPqr.objects.filter(pqr_id=pqr_id)
        context = {'pqr':pqr,'respuesta_pqr':respuesta_pqr}
        return render(request, "pages/pqr_lista_respuesta.html", context)
    else:
        respuesta_pqr = 'No se ha respondido la PQR'
        context = {'respuesta':respuesta_pqr}
        return render(request, "pages/pqr_lista_respuesta.html", context)


""" def VerRespuestaPqrUsuarioView(request,id):
    pqr = Pqr.objects.get(id=id)
    respuesta_pqr = RespuestaPqr.objects.get(pqr_id=id)
    return render(request, "pages/pqr_respuesta_usuario.html", {'pqr':pqr,'respuesta_pqr':respuesta_pqr}) """
            
def BuscarRespuestaPqrView(request,id):
    if RespuestaPqr.objects.filter(pqr_id=id).exists():
        respuesta_pqr = RespuestaPqr.objects.filter(pqr_id=id)
        pqr = Pqr.objects.filter(id=id)
        context = {'pqr':pqr,'respuesta_pqr':respuesta_pqr}
        return render(request, "pages/pqr_lista_respuesta.html", context)
    else:
        return redirect('dar_respuesta_pqr',id)        

def BorraRespuestaPQRView(request,id):
    RespuestaPqr.filter(id=id).delete()
    return redirect('ver_respuesta_pqr',id)

class EditaRespuestaPQRView(UpdateView):
    model = RespuestaPqr
    fields = ['content']
    #form = RespuestaPQRForm
    template_name = "pages/respuesta_pqr_form.html"
    #success_url = reverse_lazy('ver_respuesta_pqr')   

    def get_success_url(self):
        pk = self.kwargs.get("pk")
        respuesta_pqr = RespuestaPqr.objects.get(id=pk)
        idpqr = respuesta_pqr.pqr_id
        return reverse_lazy('ver_respuesta_pqr', kwargs={'id':idpqr})
        
   
class DarRespuestaPqrView(CreateView):
    model = RespuestaPqr
    template_name = 'pages/respuesta_pqr_form.html'
    form_class = RespuestaPQRForm

    def form_valid(self, form):
        pk=self.kwargs['pk']
        respuesta_pqr = form.save(commit=False)
        respuesta_pqr.pqr_id = pk
        respuesta_pqr.save()
        id = pk
        Pqr.objects.filter(pk=pk).update(fecha_respuesta=datetime.now(),pendiente=False)
        pqr = Pqr.objects.get(id=id)
        apartamento = Apartamento.objects.get(id=pqr.apartamento_id)
        mensaje=" Su "+pqr.tipo_pqr.descripcion+" <"+pqr.title+"> ya ha sido respondido por la Administración"
        asunto = "Respuesta "+pqr.tipo_pqr.descripcion
        EnvioMailResidente(apartamento.id,mensaje,asunto)
        redirect_url = reverse('lista_pqr') 
        return HttpResponseRedirect(redirect_url)       

def DireccionaListaPqrView(request):
    tipo_usuario = request.session['tipo_usuario']
    if tipo_usuario == 1:
        return redirect('lista_pqr')
    else:
        if tipo_usuario == 2 or tipo_usuario == 5:
            return redirect('user_home',tipo_usuario)
        
class ClasificadosListView(TemplateView):
    template_name = 'pages\clasificados.html'

def ListaClasificadoView(request):
    clasificados = Clasificado.objects.all().order_by('-id')
    return render(request, "pages/clasificados_lista.html", {"clasificados":clasificados})

def ClasificadosDetalleView(request,id):
    clasificado = Clasificado.objects.filter(id=id).order_by('-id')
    return render(request, "pages/clasificados_detalle.html", {"clasificado":clasificado})

class CrearClasificadoView(CreateView):
    model = Clasificado
    template_name = 'pages/clasificado_form.html'
    form_class = ClasificadosForm
        
    def form_valid(self, form):
        tipo_usuario =self.request.session['tipo_usuario']
        clasificado = form.save(commit=False)
        clasificado.user_id = self.request.user.id
        clasificado.vigente = True
        clasificado.save()
        clasificado = Clasificado.objects.latest('id')
        EnvioMailMasivo('Actualización Clasificados',clasificado.title)
        return HttpResponseRedirect(reverse('user_home',tipo_usuario))    

class BorrarClasificadoView(DeleteView):
    model = Clasificado
    template_name = "pages/legislacion_confirm_delete.html"

    def get_success_url(self):
        tipo_usuario = self.request.session['tipo_usuario']
        return reverse_lazy('user_home',args=[tipo_usuario])      


class EditarClasificadoView(UpdateView):
    model = Clasificado
    fields = ['title','content','foto','informes']
    template_name = 'pages/clasificado_form.html'
    
    def get_success_url(self):
        tipo_usuario = self.request.session['tipo_usuario']
        return reverse_lazy('user_home',args=[tipo_usuario])      

def PonerVendidoClasificadoView(request,id):
    tipo_usuario = request.session['tipo_usuario']
    Clasificado.objects.filter(id=id).update(vigente=False)
    ##return HttpResponseRedirect(reverse('user_home',tipo_usuario)) 
    return redirect('user_home',tipo_usuario)

def DireccionaSalidaClasificadoFormView(request):
    tipo_usuario = request.session['tipo_usuario']
    if tipo_usuario == 1:
        return redirect('pagina_administrador')
    else:
        if tipo_usuario == 2 or tipo_usuario == 5:
            return redirect('user_home',tipo_usuario)
        
def AjaxContarRegistrosPendientesAdministrador(request):
    num_pqr = Pqr.objects.filter(fecha_respuesta=None).count()
    data = {'num_pqr':num_pqr}
    return JsonResponse(data)

def ListaLegislacionView(request,page=1):
    legislacion = Legislacion.objects.all().order_by('-id')
    anexos = AnexoLegislacion.objects.all()
    paginator = Paginator(legislacion, 2)
    try:
        legislacion = paginator.page(page)
    except EmptyPage:
        legislacion = paginator.page(paginator.num_pages)
    return render(request, "pages/legislacion_lista.html", {"legislacion":legislacion,"anexos":anexos})
    
def DetalleLegislacionView(request,id):
    legislacion = legislacion =Legislacion.objects.filter(id=id)
    return render(request, "pages/legislacion_lista_detalle.html", {"legislacion":legislacion})

class CrearLegislacionView(CreateView):
    model = Legislacion
    template_name = 'pages/legislacion_form.html'
    form_class = LegislacionForm
    #success_url = reverse_lazy('lista_legislacion')

    def form_valid(self, form):
        legislacion = form.save(commit=False)
        legislacion.save()
        print('aqui')
        tipo_usuario = self.request.session['tipo_usuario']
        legislacion = Legislacion.objects.latest('id')
        EnvioMailMasivo('Actualización Legislación',legislacion.title) 
        return redirect('lista_legislacion')      
       
class BorrarLegislacionView(DeleteView):
    model = Legislacion
    success_url = reverse_lazy('lista_legislacion')
    template_name = "pages/legislacion_confirm_delete.html"

class EditarLegislacionView(UpdateView):
    model = Legislacion
    form_class = LegislacionForm
    success_url = reverse_lazy('lista_legislacion')   

""" def ListaLegislacionView(request):
    legislacion = legislacion =Legislacion.objects.all().order_by('-id')
    anexos = AnexoLegislacion.objects.all()
    return render(request, "pages/legislacion_lista.html", {"legislacion":legislacion,"anexos":anexos}) """
    
""" def DetalleLegislacionView(request,id):
    legislacion = legislacion =Legislacion.objects.filter(id=id)
    return render(request, "core/legislacion_lista_detalle.html", {"legislacion":legislacion}) """


def ListaComunicadoView(request,page=1):
    comunicados = Comunicado.objects.all().order_by('-id')
    paginator = Paginator(comunicados, 4)
    try:
        comunicados = paginator.page(page)
    except EmptyPage:
        comunicados = paginator.page(paginator.num_pages)
    return render(request, "pages/comunicados_lista.html", {"comunicados":comunicados})

def ComunicadoDetalleView(request,id):
    comunicado = Comunicado.objects.filter(id=id).order_by('-id')
    anexos = AnexoComunicado.objects.filter(comunicado_id=id)
    return render(request, "pages/comunicados_detalle.html", {"comunicado":comunicado,'anexos':anexos})

class CrearComunicadoView(CreateView):
    model = Comunicado
    template_name = 'pages/comunicado_form.html'
    form_class = ComunicadoForm
    #success_url = reverse_lazy('lista_comunicados')

    def form_valid(self, form):
        comunicado = form.save(commit=False)
        foto = form.cleaned_data['foto']
        comunicado.foto = foto
        comunicado.save()
        comunicado = Comunicado.objects.latest('id')
        EnvioMailMasivo('Actualización Comunicado',comunicado.title) 
        return HttpResponseRedirect(reverse('lista_comunicados'))

             
class BorrarComunicadoView(DeleteView):
    model = Comunicado
    success_url = reverse_lazy('lista_comunicados')
    template_name = "pages/comunicado_confirm_delete.html"

class EditarComunicadoView(UpdateView):
    model = Comunicado
    form_class = ComunicadoForm
    success_url = reverse_lazy('lista_comunicados')  

def ListaNormatividadView(request,page=1):
    normatividad = Normatividad.objects.all().order_by('-id')
    anexos = AnexoNormatividad.objects.all()
    paginator = Paginator(normatividad, 2)
    try:
        normatividad = paginator.page(page)
    except EmptyPage:
        normatividad = paginator.page(paginator.num_pages)
    return render(request, "pages/normatividad_lista.html", {"normatividad":normatividad,"anexos":anexos})

class CrearNormatividadView(CreateView):
    model = Normatividad
    template_name = 'pages/normatividad_form.html'
    form_class = NormatividadForm
    
    def form_valid(self, form):
        normatividad = form.save(commit=False)
        normatividad.save()
        tipo_usuario = self.request.session['tipo_usuario']
        normatividad = Normatividad.objects.latest('id')
        EnvioMailMasivo('Actualización Normatividad',normatividad.title) 
        return redirect('lista_normatividad')      
    
class BorrarNormatividadView(DeleteView):
    model = Normatividad
    success_url = reverse_lazy('lista_normatividad')
    template_name = "pages/normatividad_confirm_delete.html"

class EditarNormatividadView(UpdateView):
    model = Normatividad
    form_class = NormatividadForm
    success_url = reverse_lazy('lista_normatividad')     

def EnvioMailMasivo(subject,titulo):
    from_email = settings.EMAIL_HOST_USER
    residentes = Residente.objects.all()
    msg = []
    for residente in residentes:
        """ if residente.email != None:
            message ="Sres. "+residente.nombre+" Se ha a agregado una nueva publicación en la página: '"+titulo+"'"
            mail = EmailMessage(
            subject,
            message,
            from_email,
            to=[residente.email],
            bcc=None,
            )
            mail.send() """
        if residente.email != None:
            message ="Sres. "+residente.nombre+" Se ha a agregado una nueva publicación en la página: '"+titulo+"'"
            a = (subject,message,from_email,[residente.email])
            msg.append(a)
        send_mass_mail(msg, fail_silently=False)
    return     

def EnvioMailResidente(idapartamento,mensaje,asunto):
    apartamento = Apartamento.objects.get(id=idapartamento)
    residente = Residente.objects.filter(apartamento_id=idapartamento).exclude(email=None)
    for i in residente:
        nombre = i.nombre
        email = i.email
        message ="Sres. "+"Apartamento <"+apartamento.numero+"> "+i.nombre+" "+mensaje
        subject = asunto
        from_email = settings.EMAIL_HOST_USER
        mail = EmailMessage(
            subject,
            message,
            from_email,
            to=[email],
            bcc=None,
        )
        mail.send()
    return email