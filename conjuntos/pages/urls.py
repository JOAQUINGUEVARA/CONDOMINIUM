from django.urls import path
from . import views
from pages.views import LegislacionListView,CreaPQRView,VerRespuestaPqrView,VerDetallePqrView,PageListView
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.decorators import login_required

urlpatterns = [
   #path('',PageListView.as_view(), name="pages"),
   path('<int:page_id>/<slug:page_slug>/', views.page, name="page"),
   
   #path('pqr/<int:id>',views.PqrResidenteListView,name='pqr'),
   
   #path('pqr_administrador_uno/<int:pk>',views.PqrAdministradorUnoListView,name='pqr_administrador_uno'),

   path('lista_pqr',views.PqrListaView,name='lista_pqr'),   
   path('crear_pqr',views.CreaPQRView.as_view(), name="crear_pqr"),
   path('borra_respuesta_pqr/<int:id>',views.BorraRespuestaPQRView, name="borra_respuesta_pqr"),
   path('edita_respuesta_pqr/<int:pk>',views.EditaRespuestaPQRView.as_view(), name="edita_respuesta_pqr"),   
   path('ver_detalle_pqr/<int:id>',views.VerDetallePqrView,name='ver_detalle_pqr'),
   path('ver_respuesta_pqr/<int:id>/:',views.VerRespuestaPqrView,name='ver_respuesta_pqr'),
   #path('ver_respuesta_pqr_usuario/<int:id>/<int:tipo_usuario>/',views.VerRespuestaPqrUsuarioView,name='ver_respuesta_pqr_usuario'),
   path('buscar_respuesta_pqr/<int:id>',views.BuscarRespuestaPqrView,name='buscar_respuesta_pqr'),
   path('dar_respuesta_pqr/<pk>/',views.DarRespuestaPqrView.as_view(),name='dar_respuesta_pqr'),
   path('pqr_detalle/<int:id>',views.PqrDetalleView,name='pqr_detalle'),
   path('direcciona_lista_pqr',views.DireccionaListaPqrView,name='direcciona_lista_pqr'), 
   
   path('<int:legislacion_id>/<slug:legislacion_slug>',views.LegislacionPaginasView, name="page_legislacion"),
   path('legislacion',LegislacionListView, name="legislacion"),
   path('lista_legislacion/<int:page>/',views.ListaLegislacionView,name='lista_legislacion'),
   path('crear_legislacion/',views.CrearLegislacionView.as_view(),name='crear_legislacion'),
   path('borrar_legislacion/<int:pk>/',views.BorrarLegislacionView.as_view(),name='borrar_legislacion'),
   path('editar_legislacion/<int:pk>/',views.EditarLegislacionView.as_view(),name='editar_legislacion'),
   path('legislacion_lista_detalle/<int:id>/', views.DetalleLegislacionView, name='legislacion_lista_detalle'),
   
   path('editar_clasificado/<int:pk>/',views.EditarClasificadoView.as_view(),name='editar_clasificado'),
   path('clasificados_list',views.ClasificadosListView.as_view(),name='clasificados_list'),
   path('clasificados_detalle/<int:id>',views.ClasificadosDetalleView,name='clasificados_detalle'),
   #path('borrar_clasificado/<pk>/',views.BorrarClasificadoView.as_view(),name='borrar_clasificado'),
   path('crear_clasificado',login_required(views.CrearClasificadoView.as_view()),name='crear_clasificado'),
   path('poner_vendido_clasificado/<int:id>/',views.PonerVendidoClasificadoView,name='poner_vendido_clasificado'),
   #path('contar_registros_eventos',views.AjaxContarRegistrosEventos,name='contar_registros_eventos'),
   #path('contar_registros_pendientes_administrador',views.AjaxContarRegistrosPendientesAdministrador,name='contar_registros_pendientes_administrador'),
   path('lista_clasificados/',views.ListaClasificadoView,name='lista_clasificados'),
   #path('crear_clasificado/',login_required(views.CrearClasificadoView.as_view()),name='crear_clasificado'),
   path('borrar_clasificado/<int:pk>/',views.BorrarClasificadoView.as_view(),name='borrar_clasificado'),
   path('editar_clasificado/<int:pk>/',views.EditarClasificadoView.as_view(),name='editar_clasificado'),
   path('direcciona_salida_clasificado_form',views.DireccionaSalidaClasificadoFormView,name='direcciona_salida_clasificado_form'),   
   path('lista_comunicados/<int:page>/',views.ListaComunicadoView,name='lista_comunicados'),
   path('comunicados_detalle/<int:id>/',views.ComunicadoDetalleView,name='comunicados_detalle'),
   path('crear_comunicado/',login_required(views.CrearComunicadoView.as_view()),name='crear_comunicado'),
   path('borrar_comunicado/<int:pk>/',views.BorrarComunicadoView.as_view(),name='borrar_comunicado'),
   path('editar_comunicado/<int:pk>/',views.EditarComunicadoView.as_view(),name='editar_comunicado'),

   path('lista_normatividad/<int:page>/',views.ListaNormatividadView,name='lista_normatividad'),
   path('crear_normatividad/',views.CrearNormatividadView.as_view(),name='crear_normatividad'),
   path('borrar_normatividad/<int:pk>/',views.BorrarNormatividadView.as_view(),name='borrar_normatividad'),
   path('editar_normatividad/<int:pk>/',views.EditarNormatividadView.as_view(),name='editar_normatividad'),


   #path('legislacion_list',views.LegislacionListView.as_view(),name='legislacion_list'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)