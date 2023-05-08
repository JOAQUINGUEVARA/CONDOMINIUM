from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from upload import views

upload_patterns = ([
    path('anexo_contrato/<int:id>/', views.AnexoContratoView,name='anexo_contrato'),
    path('anexo_mantenimiento/<int:id>/', views.AnexoMantenimientoView,name='anexo_mantenimiento'),
    path('anexo_obra/<int:id>/', views.AnexoObraView,name='anexo_obra'),
    path('anexo_avance_obra/<int:id>/', views.AnexoAvanceObraView,name='anexo_avance_obra'),
    path('anexo_reparacion/<int:id>/', views.AnexoReparacionView,name='anexo_reparacion'),
    path('anexo_reunion_consejo/<int:id>/', views.AnexoReunionConsejoView,name='anexo_reunion_consejo'),
    path('anexo_asamblea/<int:id>/', views.AnexoAsambleaView,name='anexo_asamblea'),
    path('anexo_informe_revisor/<int:id>/', views.AnexoInformeRevisorView,name='anexo_informe_revisor'),
    path('anexo_legislacion/<int:id>/', views.AnexoLegislacionView,name='anexo_legislacion'),
    path('ajax_valida_anexo_legislacion/',views.ValidaAnexoLegislacionView,name='ajax_valida_anexo_legislacion'),
    path('anexo_normatividad/<int:id>/', views.AnexoNormatividadView,name='anexo_normatividad'),
    #path('anexo_pago_reserva/<int:id>/', views.AnexoPagoReservaView,name='anexo_pago_reserva'),
    path('anexo_proponente_poyecto/<int:id>/', views.AnexoProponenteProyectoView,name='anexo_proponente_proyecto'),
    path('anexo_proyecto/<int:id>/', views.AnexoProyectoView,name='anexo_proyecto'),
    path('anexo_comunicados/<int:id>/', views.AnexoComunicadoView,name='anexo_comunicados'),
    path('anexo_proponente/<int:id>/', views.AnexoProponenteView,name='anexo_proponente'),
    path('anexo_proveedor/<int:id>/', views.AnexoProveedorView,name='anexo_proveedor'),
    path('borra_anexo_comunicado/<int:pk>/',views.BorraAnexoComunicadoView.as_view(),name='borra_anexo_comunicado'),
    path('borra_anexo_legislacion/<int:pk>/',views.BorraAnexoLegislacionView.as_view(),name='borra_anexo_legislacion'),
    #path('borra_anexo_publicacion/<int:pk>/',views.BorraAnexoPublicacionView.as_view(),name='borra_anexo_publicacion'),
    path('borra_anexo_normatividad/<int:pk>/',views.BorraAnexoNormatividadView.as_view(),name='borra_anexo_normatividad'),
    path('borra_anexo_contrato/<int:pk>/',views.BorraAnexoContratoView.as_view(),name='borra_anexo_contrato'),
    path('borra_anexo_proponente/<int:pk>/',views.BorraAnexoProponenteView.as_view(),name='borra_anexo_proponente'),
    path('borra_anexo_proveedor/<int:pk>/',views.BorraAnexoProveedorView.as_view(),name='borra_anexo_proveedor'),
    path('anexo_proceso_juridico/<int:id>/', views.AnexoProcesoJuridicoView,name='anexo_proceso_juridico'),
    path('anexo_gestion_proceso_juridico/<int:id>/', views.AnexoGestionProcesoJuridicoView,name='anexo_gestion_proceso_juridico'),
    path('anexo_baja_activo_fijo/<int:id>/', views.AnexoBajaActivoFijoView,name='anexo_baja_activo_fijo'),   
    path('borra_anexo_baja_activo/<int:pk>/',views.BorraAnexoBajaActivoView.as_view(),name='borra_anexo_baja_activo'),
    path('anexo_pago_reserva/<int:id>/', views.AnexoPagoReservaView,name='anexo_pago_reserva'),   
    path('borra_anexo_pago_reserva/<int:pk>/',views.BorraAnexoPagoReservaView.as_view(),name='borra_anexo_pago_reserva'),

], 'upload')

