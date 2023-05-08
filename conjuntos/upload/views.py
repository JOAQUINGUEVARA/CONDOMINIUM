from django.shortcuts import render, redirect
from django.views.generic import TemplateView, ListView, CreateView,DeleteView
from django.core.files.storage import FileSystemStorage
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.base import View
from django.http import JsonResponse
from django.shortcuts import render
from django.conf import settings
from django.core.files.storage import FileSystemStorage
#from django.contrib import messages
#from django.core.urlresolvers import reverse
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth.mixins import LoginRequiredMixin
from core.forms import ReunionConsejoForm
from django.contrib import messages

from .forms import AnexoContratoForm,AnexoMantenimientoForm,AnexoObraForm,AnexoAvanceObra,AnexoAvanceObraForm,AnexoReparacionForm,AnexoBajaActivoFijoForm,AnexoBajaActivoFijoForm
from .forms import AnexoReunionConsejoForm,AnexoNormatividadForm,AnexoProponenteProyectoForm,AnexoProveedorForm,AnexoGestionProcesoJuridicoForm,AnexoAsambleaForm,AnexoPagoReservaForm
from .forms import AnexoLegislacionForm,AnexoInformeRevisorForm,AnexoComunicadosForm,AnexoProyectoForm,AnexoProponenteForm,AnexoProcesoJuridicoForm,AnexoAsamblea
from .models import AnexoContrato,AnexoMantenimiento,AnexoObra,AnexoAvanceObra,AnexoReparacion, AnexoReunionConsejo,AnexoComunicado,AnexoGestionProcesoJuridico,AnexoBajaActivoFijo
from .models import AnexoInformeRevisor,AnexoLegislacion,AnexoNormatividad,AnexoProponenteProyecto,AnexoProyecto,AnexoProponente,AnexoProveedor,AnexoProcesoJuridico,AnexoPagoReserva
from core.models import Contrato,Obra,AvanceObra, ReunionConsejo,InformeRevisor,ProponenteProyecto,Proponente,Proveedor,ProcesoJuridico,GestionProcesoJuridico,Asamblea,ActivoFijo,BajaActivoFijo,Reservas,ZonaComun
from pages.models import Legislacion,Normatividad,Comunicado


def AnexoContratoView(request,id):
    request.session['idcontrato'] = id
    idcontrato = id
    if request.method == 'POST':
        form = AnexoContratoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoContrato()
            obj.contrato_id=idcontrato
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('contratos_detalle',idcontrato)
    else:
        form = AnexoContratoForm()
    return render(request, 'upload/anexo_contrato.html', {'form': form})


def AnexoMantenimientoView(request,id):
    request.session['idmantenimiento'] = id
    idmantenimiento = id
    if request.method == 'POST':
        form = AnexoMantenimientoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoMantenimiento()
            obj.mantenimiento_id=idmantenimiento
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('mantenimientos_detalle',idmantenimiento)
    else:
        form = AnexoMantenimientoForm()
    return render(request, 'upload/anexo_contrato.html', {'form': form})

def AnexoObraView(request,id):
    request.session['idobra'] = id
    idcontrato = id
    if request.method == 'POST':
        form = AnexoObraForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoObra()
            obj.obra_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('obra_detalle',id)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_obra.html', {'form': form})    

def AnexoReparacionView(request,id):
    request.session['irepracion'] = id
    idreparacion = id
    if request.method == 'POST':
        form = AnexoReparacionForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoReparacion()
            obj.reparacion_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('reparaciones_detalle',id)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_reparacion.html', {'form': form})

def AnexoAvanceObraView(request,id):
    request.session['idavanceobra'] = id
    idavanceobra = id
    avance = AvanceObra.objects.get(id=id)
    obra = Obra.objects.get(id=avance.obra_id)
    idobra = obra.id
    if request.method == 'POST':
        form = AnexoAvanceObraForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoAvanceObra()
            obj.avance_obra_id=idavanceobra
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('obra_detalle',idobra)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_avance_obra.html', {'form': form})       

def AnexoReunionConsejoView(request,id):
    request.session['idreunion'] = id
    idreunion = id
    reunion = ReunionConsejo.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoReunionConsejoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            print(descripcion)
            archivo = request.FILES['archivo']
            obj = AnexoReunionConsejo()
            obj.reunion_id=idreunion
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.publicar = False
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('detalle_reunion_consejo',idreunion)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_reunion_consejo.html', {'form': form})    

def AnexoInformeRevisorView(request,id):
    request.session['idinforme'] = id
    idinforme = id
    informe = InformeRevisor.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoInformeRevisorForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoInformeRevisor()
            obj.informe_revisor_id=idinforme
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.publicar = False
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('informe_revisor_detalle',idinforme)
    else:
        form = AnexoInformeRevisorForm()
    return render(request, 'upload/anexo_informe_revisor.html', {'form': form}) 

def AnexoLegislacionView(request,id):
    request.session['idlegislacion'] = id
    idlegislacion = id
    legislacion = Legislacion.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoLegislacionForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoLegislacion()
            obj.legislacion_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.publicar = False
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('lista_legislacion')
    else:
        form = AnexoLegislacionForm()
    return render(request, 'upload/anexo_legislacion.html', {'form': form})     

def ValidaAnexoLegislacionView(request):
    #solicitud = Solicitud.objects.filter(user=request.user.id).latest('id')
    idlegislacion = request.session['Idlegislacion']
    data = {
        'is_anexo': AnexoLegislacion.objects.filter(legislacion_id=id).exists(),'idlegislacion':idlegislacion
    }
    print(data)
    return JsonResponse(data)

class BorraAnexoLegislacionView(LoginRequiredMixin,DeleteView):
    model = AnexoLegislacion
    success_url = reverse_lazy('lista_legislacion')
    template_name = 'core/confirmar_borrado_registro.html'

class BorraAnexoNormatividadView(LoginRequiredMixin,DeleteView):
    model = AnexoNormatividad
    success_url = reverse_lazy('lista_normatividad')
    template_name = 'core/confirmar_borrado_registro.html'

class BorraAnexoComunicadoView(LoginRequiredMixin,DeleteView):
    model = AnexoComunicado
    success_url = reverse_lazy('lista_comunicados')
    template_name = 'core/confirmar_borrado_registro.html'

class BorraAnexoContratoView(LoginRequiredMixin,DeleteView):
    model = AnexoContrato
    #success_url = reverse_lazy('contratos_detalle,id')
    template_name = 'core/confirmar_borrado_registro.html'

    def get_success_url(self):
        id = self.object.id
        print(id)
        anexo_contrato = AnexoContrato.objects.get(id=id)
        idcontrato = anexo_contrato.contrato_id 
        print(idcontrato)
        return reverse_lazy('contratos_detalle',args=[idcontrato])

class BorraAnexoProponenteView(LoginRequiredMixin,DeleteView):
    model = AnexoProponente
    success_url = reverse_lazy('')
    template_name = 'core/confirmar_borrado_registro.html'

    def get_success_url(self):
        idanexo = self.object.id
        anexo = AnexoProponente.objects.get(id=idanexo)
        proponente = Proponente.objects.get(id=anexo.proponente_id)
        idproponente = proponente.id 
        return reverse_lazy('proponente_detalle',args=[idproponente])

class BorraAnexoProveedorView(LoginRequiredMixin,DeleteView):
    model = AnexoProveedor
    success_url = reverse_lazy('')
    template_name = 'core/confirmar_borrado_registro.html'

    def get_success_url(self):
        idanexo = self.object.id
        anexo = AnexoProveedor.objects.get(id=idanexo)
        proveedor = Proveedor.objects.get(id=anexo.proveedor_id)
        idproveedor = proveedor.id 
        return reverse_lazy('proveedor_detalle',args=[idproveedor])

""" class BorraAnexoPublicacionView(LoginRequiredMixin,DeleteView):
    model = Publicacion
    success_url = reverse_lazy('lista_normatividad')
    template_name = 'core/confirmar_borrado_registro.html' """

def AnexoNormatividadView(request,id):
    request.session['idnormatividad'] = id
    idnormatividad = id
    normatividad = Normatividad.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoNormatividadForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            descripcion = form.cleaned_data.get('descripcion')
            obj = AnexoNormatividad()
            obj.normatividad_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.publicar = False
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('lista_normatividad')
    else:
        form = AnexoNormatividadForm()
    return render(request, 'upload/anexo_normatividad.html', {'form': form}) 

def AnexoComunicadoView(request,id):
    request.session['idcomunicado'] = id
    idcomunicado = id
    comunicado = Comunicado.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoComunicadosForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoComunicado()
            obj.comunicado_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('lista_comunicados')
    else:
        form = AnexoLegislacionForm()
    return render(request, 'upload/anexo_comunicado.html', {'form': form}) 

""" def AnexoPagoReservaView(request,id):
    request.session['idZonaComun'] = id
    zona_comun = zona_comun.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoZonaComunForm(request.POST, request.FILES)
        if form.is_valid():
            archivo = request.FILES['archivo']
            descripcion = form.cleaned_data.get('descripcion')
            obj = AnexoPagoZonaComun()
            obj.zona_comun_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.publicar = False
            obj.save()
            ##return reverse_lazy('obra_detalle',args=idobra)
            return redirect('reserva_zonas_comunes')
    else:
        form = AnexoPagoZonaComunForm()
    return render(request, 'upload/anexo_pago_reserva.html', {'form': form})  """

def AnexoProponenteProyectoView(request,id):
    request.session['idproponente_proyecto'] = id
    idproponente_proyecto = id
    proponente_proyecto = ProponenteProyecto.objects.get(id=id)
    idproyecto = proponente_proyecto.proyecto_id
    if request.method == 'POST':
        form = AnexoProponenteProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoProponenteProyecto()
            obj.proponente_proyecto_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proyecto_detalle',idproyecto)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_proponente_proyecto.html', {'form': form})


def AnexoProyectoView(request,id):
    request.session['idproyecto'] = id
    idproyecto = id
    if request.method == 'POST':
        form = AnexoProyectoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoProyecto()
            obj.proyecto_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proyecto_detalle',id)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_proyecto.html', {'form': form})

def AnexoProponenteView(request,id):
    request.session['idproponente'] = id
    idproponente = id
    proponente = Proponente.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoProponenteForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoProponente()
            obj.proponente_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proponente_detalle',idproponente)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_proponente.html', {'form': form})

def AnexoProveedorView(request,id):
    request.session['idproveedor'] = id
    idproveedor = id
    proveedor = Proveedor.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoProveedorForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoProveedor()
            obj.proveedor_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proveedor_detalle',idproveedor)
    else:
        form = AnexoObraForm()
    return render(request, 'upload/anexo_proveedor.html', {'form': form})

def AnexoProcesoJuridicoView(request,id):
    request.session['idproceso'] = id
    idproceso = id
    proceso = ProcesoJuridico.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoProcesoJuridicoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoProcesoJuridico()
            obj.proceso_juridico_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proceso_juridico_detalle',idproceso)
    else:
        form = AnexoProcesoJuridicoForm()
    return render(request, 'upload/anexo_proceso_juridico.html', {'form': form})

def AnexoGestionProcesoJuridicoView(request,id):
    request.session['idgestion'] = id
    idgestion = id
    gestion_proceso_juridico = GestionProcesoJuridico.objects.get(id=id)
    idproceso = gestion_proceso_juridico.proceso_juridico_id
    if request.method == 'POST':
        form = AnexoGestionProcesoJuridicoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoGestionProcesoJuridico()
            obj.gestion_proceso_juridico_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('proceso_juridico_detalle',idproceso)
    else:
        form = AnexoProcesoJuridicoForm()
    return render(request, 'upload/anexo_gestion_proceso_juridico.html', {'form': form})

def AnexoAsambleaView(request,id):
    request.session['idasamblea'] = id
    idasamblea = id
    proceso = Asamblea.objects.get(id=id)
    if request.method == 'POST':
        form = AnexoAsambleaForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoAsamblea()
            obj.asamblea_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('detalle_asamblea',idasamblea)
    else:
        form = AnexoAsambleaForm()
    return render(request, 'upload/anexo_asamblea.html', {'form': form})

def AnexoBajaActivoFijoView(request,id):
    baja_activo = BajaActivoFijo.objects.get(id=id)
    print(baja_activo.activo_fijo_id)
    activo = ActivoFijo.objects.get(id=baja_activo.activo_fijo_id)
    idactivo = activo.id
    if request.method == 'POST':
        form = AnexoBajaActivoFijoForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoBajaActivoFijo()
            obj.baja_activo_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            return redirect('activos_fijos_detalle',idactivo)
    else:
        form = AnexoProcesoJuridicoForm()
    return render(request, 'upload/anexo_baja_activo_fijo.html', {'form': form})

class BorraAnexoBajaActivoView(LoginRequiredMixin,DeleteView):
    model = AnexoBajaActivoFijo
    #success_url = reverse_lazy('contratos_detalle,id')
    template_name = 'core/confirmar_borrado_registro.html'

    def get_success_url(self):
        id = self.object.id
        anexo_baja = AnexoBajaActivoFijo.objects.get(id=id)
        idactivo = anexo_baja.activo_fijo_id 
        return reverse_lazy('activos_fijos_detalle',args=[idactivo])

def AnexoPagoReservaView(request,id):
    if AnexoPagoReserva.objects.filter(reserva_id=id).exists():
        AnexoPagoReserva.objects.filter(reserva_id=id).delete()
    reserva = Reservas.objects.get(id=id)
    zona_comun = ZonaComun.objects.get(id=reserva.zona_comun_id)
    if request.method == 'POST':
        form = AnexoPagoReservaForm(request.POST, request.FILES)
        if form.is_valid():
            descripcion = form.cleaned_data.get('descripcion')
            archivo = request.FILES['archivo']
            obj = AnexoPagoReserva()
            obj.reserva_id=id
            obj.archivo=archivo
            obj.descripcion = descripcion
            obj.save()
            Reservas.objects.filter(id=reserva.id).update(anexo_pago=True,estado=True) 
            return redirect('reserva_zonas_comunes',zona_comun.id)
    else:
        form = AnexoPagoReservaForm()
    return render(request, 'upload/anexo_pago_reserva.html', {'form': form})

class BorraAnexoPagoReservaView(LoginRequiredMixin,DeleteView):
    model = AnexoPagoReserva
    template_name = 'core/confirmar_borrado_registro.html'

    def get_success_url(self):
        id = self.object.id
        anexo_pago = AnexoPagoReserva.objects.get(id=id)
        idreserva = anexo_pago.reserva_id
        reserva = Reservas.objects.get(id=idreserva)
        zona_comun = ZonaComun.objects.get(id=reserva.zona_comun_id)
        return reverse_lazy('reserva_zonas_comunes',args=[zona_comun.id])    