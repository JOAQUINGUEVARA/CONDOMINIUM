from django.db import models
from core.models import Contrato,Obra,AvanceObra,Mantenimiento,Reparacion,ReunionConsejo,InformeRevisor,ProcesoJuridico,ZonaComun,Proponente,Proyecto,ProponenteProyecto,Proveedor
from core.models import GestionProcesoJuridico,Asamblea,ActivoFijo,BajaActivoFijo,Reservas
from pages.models import Legislacion,Normatividad,Comunicado

class TipoAnexo(models.Model):
    descripcion = models.CharField(max_length=30)
    
    def __str__(self):
        return self.descripcion

    class Admin:
        pass

class AnexoContrato(models.Model):
    contrato = models.ForeignKey(Contrato,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Contrato No.',related_name='anexo_contrato')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo Contrato No.'+self.contrato.numero.trim()+'-'+self.contrato.descripcion.trim()
    
    class Admin:
        pass

class AnexoObra(models.Model):
    obra = models.ForeignKey(Obra,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Obra',related_name='anexo_obra')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo Obra '+self.obra.descripcion.trim()
    
    class Admin:
        pass

class AnexoAvanceObra(models.Model):
    avance_obra = models.ForeignKey(AvanceObra,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Avance Obra',related_name='anexo_avance_obra')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo Avace Obra: '+self.avance_obra.obra.descripccion.trim()
    
    class Admin:
        pass

class AnexoMantenimiento(models.Model):
    mantenimiento = models.ForeignKey(Mantenimiento,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Mantenimiento',related_name='anexo_mantenimiento')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo Mantenimiento: '+self.mantenimiento.activo_fijo.descripccion.trim()
    
    class Admin:
        pass

class AnexoReparacion(models.Model):
    reparacion = models.ForeignKey(Reparacion,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Reparación',related_name='anexo_reparacion')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)

    def __str__(self):
           return 'Anexo Reparación: '+self.reparacion.descripcion.trim()
    
    class Admin:
        pass

class AnexoReunionConsejo(models.Model):
    reunion = models.ForeignKey(ReunionConsejo,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Reunión Consejo',related_name='anexo_reunion')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Reunión Consejo: '+self.reunion.id
    
    class Admin:
        pass


class AnexoInformeRevisor(models.Model):
    informe_revisor = models.ForeignKey(InformeRevisor,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Informe Revisor',related_name='anexo_informe_revisor')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Informe Auditor: '+self.informe_revisor.id
    
    class Admin:
        pass

class AnexoProcesoJuridico(models.Model):
    proceso_juridico = models.ForeignKey(ProcesoJuridico,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Proceso Juridico',related_name='anexo_proceso_juridico')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Proceso Juridico: '+self.proceso_juridico.proceso_numero
    
    class Admin:
        pass

class AnexoLegislacion(models.Model):
    legislacion = models.ForeignKey(Legislacion,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Legislación',related_name='anexo_legislacion')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return +self.descripcion
    
    class Admin:
        pass

class AnexoComunicado(models.Model):
    comunicado = models.ForeignKey(Comunicado,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Legislación',related_name='anexo_legislacion')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return +self.descripcion
    
    class Admin:
        pass

class AnexoNormatividad(models.Model):
    normatividad = models.ForeignKey(Normatividad,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Normatividad',related_name='anexo_normatividad')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Normatividad: '+self.normatividad.title
    
    class Admin:
        pass

class AnexoProponente(models.Model):
    proponente = models.ForeignKey(Proponente,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Proponente',related_name='anexo_proponente')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Proponente: '+self.proponente.nombre
    
    class Admin:
        pass

class AnexoProyecto(models.Model):
    proyecto = models.ForeignKey(Proyecto,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Proyecto Proponente',related_name='anexo_proyecto_proponente')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Proyecto: '+self.proyecto.descripcion
    
    class Admin:
        pass

class AnexoProponenteProyecto(models.Model):
    proponente_proyecto = models.ForeignKey(ProponenteProyecto,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Proponente Proyecto',related_name='proponente_proyecto')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Proponente Proyecto: '+self.proponente_proyecto.proponente.nombre
    
    class Admin:
        pass

class AnexoProveedor(models.Model):
    proveedor = models.ForeignKey(Proveedor,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Proveedor',related_name='anexo_proveedor')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Proveedor: '+self.proveedor.nombre
    
    class Admin:
        pass

class AnexoGestionProcesoJuridico(models.Model):
    gestion_proceso_juridico = models.ForeignKey(GestionProcesoJuridico,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Gestion Proceso Juridico',related_name='anexo_gestion_proceso_juridico')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Gestión Proceso: '+self.gestion_proceso_juridico.fecha

class AnexoAsamblea(models.Model):
    asamblea = models.ForeignKey(Asamblea,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo Asamblea',related_name='anexo_asamblea')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Asamblea: '+self.asamblea.fecha    

class AnexoBajaActivoFijo(models.Model):
    baja_activo = models.ForeignKey(BajaActivoFijo,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo BajaActivoFijo',related_name='anexo_baja_activo_fijo')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Baja Activo Fijo: '+self.baja_activo.id        

class AnexoPagoReserva(models.Model):
    reserva = models.ForeignKey(Reservas,null=True,blank=True,default='',on_delete=models.CASCADE,verbose_name='Anexo BajaActivoFijo',related_name='anexo_baja_activo_fijo')
    descripcion = models.CharField(max_length=50,default='')
    archivo = models.FileField(upload_to="upload/anexos", null=True, blank=True)
    publicar = models.BooleanField(default=False,verbose_name='Publicar Anexo ')

    def __str__(self):
           return 'Anexo Pago Reserva: '+self.reserva.id            