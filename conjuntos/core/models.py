from email.policy import default
from xmlrpc.client import Boolean
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.forms import BooleanField
from django.utils.timezone import now
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import datetime,timezone,tzinfo,date,timedelta


#from sqlalchemy import Integer 
#from django.contrib.auth import get_user_model
#UserPerfil = get_user_model()
#from django.utils import timezone
#from django.db.models.fields import DateField, DateTimeField, DurationField, Field, IntegerField, TimeField

# Create your models here.

class Conjunto(models.Model):
	nit = models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='Nit')
	razon_social = models.CharField(max_length=100,default='',verbose_name='Razón Social')
	nombre = models.CharField(max_length=50,default='',verbose_name='Nombre')
	direccion = models.CharField(max_length=100,verbose_name='Direccion')
	telefono = models.CharField(max_length=30,default='',verbose_name='Teléfono')
	nombre_administrador = models.CharField(max_length=50,verbose_name='Nombre Administrador')
	numero_unidades = models.IntegerField(null=True,blank=True,default=0,verbose_name='Número Unidades')
	foto = models.ImageField(upload_to='static/',null=True,blank=True)
	email=models.EmailField(max_length=254,verbose_name='Email')
	numero_unidades = models.IntegerField(default=0,verbose_name='Número de Unidades')
	estrato = models.IntegerField(default=0,verbose_name='Estrato')
	pagina_web = models.URLField(null=True,blank=True,default='',verbose_name='Link Página Web')
	horario_administrador = models.TextField(default='',verbose_name='Horario Adminsitrador')
	def __str__(self):
		return str(self.razon_social)	

class Interior(models.Model):
	numero = models.CharField(max_length=15,null=False,blank=False,default='',verbose_name='Número')
	#coeficiente = models.FloatField(null=False,blank=False,default=0,verbose_name='coeficiente')
	class Meta:
		ordering=["numero"]
		verbose_name='Interior'
		verbose_name_plural='Interiores'

	def __str__(self):
		return self.numero       

class Apartamento(models.Model):
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.CharField(max_length=15,null=False,blank=False,default='',verbose_name='Apartamento')
	numero = models.CharField(max_length=15,null=False,blank=False,default='',verbose_name='Número')
	coeficiente = models.FloatField(null=False,blank=False,default=0,verbose_name='coeficiente')
	class Meta:
		ordering=["numero"]
		verbose_name='Apartamento'
		verbose_name_plural='Apartamentos'

	def __str__(self):
		return self.numero

class Parqueadero(models.Model):
	numero = models.CharField(max_length=15,null=False,blank=False,default='',verbose_name='Número')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	coeficiente = models.FloatField(null=False,blank=False,default=0,verbose_name='coeficiente')
	
	class Meta:
		ordering=["numero"]
		verbose_name='Parqueadero'
		verbose_name_plural='Parqueaderos'

	def __str__(self):
		return str(self.numero)

class Deposito(models.Model):
	numero = models.CharField(max_length=15,null=False,blank=False,default='',verbose_name='Número')
	valor_arriendo = models.FloatField(null=False,blank=False,default=0,verbose_name='Valor Arriendo')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	class Meta:
		ordering=["numero"]
		verbose_name='Depósito'
		verbose_name_plural='Depósitos'
		

	def __str__(self):
		return str(self.numero)       

class Inmobiliaria(models.Model):
	nit = models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='Nit')
	razon_social = models.CharField(max_length=100,verbose_name='Razón Social')
	nombre_contacto = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Nombre Contacto')
	email = models.EmailField(max_length=254,default='',verbose_name='Email')
	pagina_web = models.URLField(null=True,blank=True,default='',verbose_name='Link Página Web')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	class Meta:
		ordering=["razon_social"]
		verbose_name='Inmobiliaria'
		verbose_name_plural='Inmobiliarias'

	def __str__(self):
		return self.razon_social

class Residente(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	TYPE_RESIDENTE = (
        ('Propietario', 'Propietario'),
        ('Arrendatario', 'Arrendatario'),
		('Residente', 'Residente'),
		('Inmoviliaria', 'Inmoviliaria'),
		('', 'No Determinado'),

    )
	tipo_residente = models.CharField(max_length=15,choices=TYPE_RESIDENTE,verbose_name='Propietario/Residente')
	telefono = models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='Teléfono')
	celular = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular')
	email=models.EmailField(max_length=254,verbose_name='Email')
	edad = models.IntegerField(null=True,blank=True,default=0,verbose_name='Edad')
	GENERO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
		('Otro', 'Otro'),
		('', 'No Determinado'),
    )
	genero = models.CharField(max_length=15,null=True,blank=True,default='',choices=GENERO,verbose_name='Género')
	TYPE_DISCAPACIDAD = (
        ('No', 'No'),
		('Si', 'Si'),
		('', 'No Determinado'),
    )
	persona_discapacitada = models.CharField(max_length=5,choices=TYPE_DISCAPACIDAD,verbose_name='Persona con Discapacidad')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
	updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
	token = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name='Token')
	envio_email = models.BooleanField(default=False,verbose_name='Envío Mail')
	envio_token = models.BooleanField(default=False,verbose_name='Envío Token')
	
	class Meta:
		ordering=["identificacion"]
		verbose_name='Residente'
		verbose_name_plural='Residentes'

	def __str__(self):
		return self.nombre

class ResidenteTemp(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	TYPE_RESIDENTE = (
        ('Propietario', 'Propietario'),
        ('Arrendatario', 'Arrendatario'),
		('Residente', 'Residente'),
		('Inmoviliaria', 'Inmoviliaria'),
		('', 'No Determinado'),

    )
	tipo_residente = models.CharField(max_length=15,choices=TYPE_RESIDENTE,verbose_name='Propietario/Residente')
	telefono = models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='Teléfono')
	celular = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular')
	email=models.EmailField(max_length=254,verbose_name='Email')
	edad = models.IntegerField(null=True,blank=True,default=0,verbose_name='Edad')
	GENERO = (
        ('Masculino', 'Masculino'),
        ('Femenino', 'Femenino'),
		('Otro', 'Otro'),
		('', 'No Determinado'),
    )
	genero = models.CharField(max_length=15,null=True,blank=True,default='',choices=GENERO,verbose_name='Género')
	TYPE_DISCAPACIDAD = (
        ('No', 'No'),
		('Si', 'Si'),
		('', 'No Determinado'),
    )
	persona_discapacitada = models.CharField(max_length=5,choices=TYPE_DISCAPACIDAD,verbose_name='Persona con Discapacidad')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	created = models.DateTimeField(auto_now_add=True,verbose_name="Fecha de creacion")
	updated = models.DateTimeField(auto_now=True,verbose_name="Fecha de edicion")
	token = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name='Token')
	
	class Meta:
		ordering=["identificacion"]
		verbose_name='Residente'
		verbose_name_plural='Residentes'

	def __str__(self):
		return self.nombre

class Vigilante(models.Model):
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	email=models.EmailField(max_length=254,verbose_name='Email',default='')
	foto = models.ImageField(upload_to='static/',null=True,blank=True)
	publicar = models.BooleanField(default=False,verbose_name='Publicar en Web')
	comunidad = models.BooleanField(default=False,verbose_name='Publicar sólo a Cominidad') 
	orden = models.IntegerField(default=0,verbose_name='Orden')
	token = models.CharField(max_length=100,null=True,blank=True,default='',verbose_name='Token')
	
	class Meta:
		ordering=["nombre"]
		verbose_name='Vigilante'
		verbose_name_plural='Vigilantes'

	def __str__(self):
		return self.nombre


class TipoIngreso(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Ingreso'
		verbose_name_plural='Tipos Ingresos'

	def __str__(self):
		return self.descripcion

class TipoAutoriza(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Nombre')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Autorización'
		verbose_name_plural='Tipo Autorización'

	def __str__(self):
		return self.descripcion

class TipoPlataformaWeb(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Nombre')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Plataforma Web Autorización'
		verbose_name_plural='Tipos plataforma Web Autorización'

	def __str__(self):
		return self.descripcion

class Autorizado(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	tipo_autoriza = models.ForeignKey(TipoAutoriza,on_delete=models.CASCADE)
	foto = models.ImageField(upload_to='static/',null=True,blank=True)
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	activo = models.BooleanField(default=True,verbose_name='Activo')
	permanente = models.BooleanField(default=False,verbose_name='Permanente')
	fecha_inicial = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	fecha_final = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Final')
	#dias = models.IntegerField(default=0,verbose_name='Dias')
	class Meta:
		ordering=["identificacion"]
		verbose_name='Autorizado'
		verbose_name_plural='Autorizados'

	def __str__(self):
		return self.nombre

class PlataformaWebPeatonal(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	fecha_inicial = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	fecha_final = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Final')
	tipo_plataforma = models.ForeignKey(TipoPlataformaWeb,on_delete=models.CASCADE) 
	class Meta:
		ordering=["identificacion"]
		verbose_name='Autorización Plataforma Web Peatonal'
		verbose_name_plural='Autorizaciones Plataforma Web Peatonal'

	def __str__(self):
		return self.nombre	

class PlataformaWebVehiculo(models.Model):
	placa = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	fecha_inicial = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	fecha_final = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Final')
	tipo_plataforma = models.ForeignKey(TipoPlataformaWeb,on_delete=models.CASCADE)
	class Meta:
		ordering=["placa"]
		verbose_name='Autorizacion Plataforma Web Vehicular'
		verbose_name_plural='Autorizaciones Plataforma Web Vehicular'

	def __str__(self):
		return self.nombre

class Visitante(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=100,verbose_name='Nombre')
	foto = models.ImageField(upload_to='media/',null=True, blank=True,default='/static/core/img/no-avatar.jpg')
	class Meta:
		ordering=["nombre"]
		verbose_name='Visitante'
		verbose_name_plural='Visitante'

	def __str__(self):
		return self.nombre

class IngresoPeatonal(models.Model):
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(default='',max_length=100,verbose_name='Nombre')
	tipoingreso = models.ForeignKey(TipoIngreso,on_delete=models.CASCADE,verbose_name='Tipo de Ingreso')
	tipo_autoriza = models.ForeignKey(TipoAutoriza,on_delete=models.CASCADE,default=1,verbose_name='Tipo de Autorización')
	#foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/core/img/no-avatar.jpg')
	vigilante = models.ForeignKey(User,verbose_name="Vigilante",on_delete=models.CASCADE)
	hora_ingreso = models.DateTimeField(editable=False,auto_now_add=True)
	hora_salida = models.DateTimeField(editable=False,null=True,verbose_name='Hora de Salida')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')

	class Meta:
		ordering=["hora_ingreso"]
		verbose_name='Ingreso Peatonal'
		verbose_name_plural='Ingresos Peatonales'

	def __str__(self):
		return self.identificacion


class VisitanteVehiculo(models.Model):
	placa = models.CharField(max_length=10,null=False,blank=False,default='',verbose_name='Placa')
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=100,verbose_name='Nombre')
	foto = models.ImageField(upload_to='static/',null=True, blank=True,default='/static/core/img/Vehiculo.jpg')
	class Meta:
		ordering=["nombre"]
		verbose_name='Vehículo Visitante'
		verbose_name_plural='Vehículo Visitante'

	def __str__(self):
		return self.nombre

class AutorizacionVehiculo(models.Model):
	tipo_autoriza = models.ForeignKey(TipoAutoriza,verbose_name='Tipo Autorización',on_delete=models.CASCADE)
	placa = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Placa')
	identificacion = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	nombre = models.CharField(max_length=100,verbose_name='Nombre')
	fecha_inicial = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	fecha_final = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Final')
	foto = models.ImageField(upload_to='static/',null=True, blank=True,default='/static/img/Vehiculo.jpg')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
	class Meta:
		ordering=["identificacion"]
		verbose_name='Autorización'
		verbose_name_plural='Autorización'

	def __str__(self):
		return self.nombre

class IngresoVehiculo(models.Model):
	placa = models.CharField(max_length=10,null=False,blank=False,default='',verbose_name='Placa')
	tipo_autoriza = models.ForeignKey(TipoAutoriza,on_delete=models.CASCADE,default=1,verbose_name='Tipo de Autorización')
	foto = models.ImageField(upload_to='static/',null=True,blank=True)
	vigilante = models.ForeignKey(User,on_delete=models.CASCADE)
	hora_ingreso = models.DateTimeField(editable=False,auto_now_add=True,verbose_name='Hora de Ingreso')
	hora_salida = models.DateTimeField(editable=False,null=True,verbose_name='Hora de Salida')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)

	class Meta:
		ordering=["hora_ingreso"]
		verbose_name='Ingreso Vehículo'
		verbose_name_plural='Ingreso Vehículos'

	def __str__(self):
		return self.placa

class Vehiculo(models.Model):
	TYPE_USO = (
		('Particular', 'Particular'),
		('Público', 'Público'),
		('', 'No Determinado'),
    )
	TYPE_AUTOMOVIL = (
		('Automóvil', 'Automóvil'),
		('Camioneta', 'Camioneta'),
		('Campero', 'Campero'),
		('Pick','Up'),
		('', 'No Determinado'),
	)
    
	placa = models.CharField(max_length=10,null=False,blank=False,default='',verbose_name='placa')
	tipo_vehiculo = models.CharField(max_length=15,choices=TYPE_AUTOMOVIL,verbose_name='Tipo de vehículo')
	uso = models.CharField(max_length=15,choices=TYPE_USO,verbose_name='Tipo de Uso')
	marca = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Marca')
	modelo = models.IntegerField(null=True,blank=True,default=0,verbose_name='Modelo')
	color = models.CharField(max_length=30,null=False,blank=False,default='',verbose_name='Color')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	parqueadero = models.ForeignKey(Parqueadero,on_delete=models.CASCADE)

	class Meta:
		ordering=["placa"]
		verbose_name='vehículo'
		verbose_name_plural='Vehículos'

	def __str__(self):
		return self.placa	

class Mascota(models.Model):
	TYPE_VACUNA = (
		('Si', 'Si'),
		('No', 'No'),
		('', 'No Determinado'),
	)
	TYPE_MASCOTA = (
		('Perro', 'Perro'),
		('Gato', 'Gato'),
		('Otro', 'Otro'),
		('', 'No Determinado'),
	)
	nombre = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Nombre')
	tipo_mascota = models.CharField(max_length=10,choices=TYPE_MASCOTA,verbose_name='Tipo de Mascota')
	raza = models.CharField(max_length=20,null=True,blank=True,default='',verbose_name='Raza')
	edad = models.IntegerField(null=True,blank=True,default=0,verbose_name='Edad')
	#vacuna = models.CharField(max_length=5,choices=TYPE_VACUNA,verbose_name='Vacuna')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	foto = models.ImageField(verbose_name="Foto Mascota", upload_to="conjuntos",null=True,blank=True)
	
	class Meta:
		ordering=["nombre"]
		verbose_name='Mascota'
		verbose_name_plural='Mascotas'

	def __str__(self):
		return self.nombre


class Correspondencia(models.Model):
	CLASE_CORRESPONDENCIA = (
		('Sobre', 'Sobre'),
		('Paquete', 'Paquete'),
		('', 'No Determinado'),
	)
	TYPE_CORRESPONDENCIA = (
		('Normal', 'Normal'),
		('Urgente', 'Urgente'),
		('', 'No Determinado'),
	)
	remitente = models.CharField(max_length=100,null=False,blank=False,default='',verbose_name='Remitente')
	destinatario = models.CharField(max_length=100,null=False,blank=False,default='',verbose_name='Destinatario')
	clase_correspondencia =  models.CharField(max_length=10,default='',choices=CLASE_CORRESPONDENCIA,verbose_name='Clase de Correspondencia')
	tipo_correspondencia =  models.CharField(max_length=10,default='',choices=TYPE_CORRESPONDENCIA,verbose_name='Tipo de Correspondencia')
	detalle = models.CharField(max_length=300,default='',null=True,verbose_name='Detalle')
	vigilante = models.ForeignKey(User,verbose_name="Vigilante",default='',on_delete=models.CASCADE)
	fechahora_recibo = models.DateTimeField(null=True,blank=True,default=now,verbose_name='Fecha Hora Recibo')
	fechahora_entrega = models.DateTimeField(null=True,blank=True,default=None,verbose_name='Fecha Hora Entrega')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE)
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE)
	entregado = models.BooleanField(null=True,blank=True,default=False)
	observacion =  models.TextField(blank=True,null=True,default='',verbose_name='Observaciones')
	
	class Meta:
		ordering=["fechahora_recibo"]
		verbose_name='Correspondencia'
		verbose_name_plural='Correspondencias'

	def __str__(self):
		return self.remitente


class Parametros(models.Model):
	valor_parametro_uno = models.IntegerField(null=True,blank=True,default=0)
	valor_parametro_dos = models.IntegerField(null=True,blank=True,default=0)
	user = models.IntegerField(verbose_name='Usuario')

class Meta:
	verbose_name='Parametro'
	verbose_name_plural='Parametros'	

class ZonaComun(models.Model):
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/placeholderpng.png')
	descripcion =  models.CharField(max_length=80,verbose_name='Descripcion')
	tarifa =models.FloatField(null=False,blank=False,default=0,verbose_name='Tarifa')
	arrienda = models.BooleanField(null=True,blank=True,default=False)
	orden = models.IntegerField(default=0,verbose_name='Orden')
	observaciones =  RichTextField(blank=True,null=True,default='',verbose_name='Observaciones')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Zona Común'
		verbose_name_plural='Zonas Comunes'

	def __str__(self):
		return self.descripcion

class Reservas(models.Model):
	user = models.ForeignKey(User,null=False,blank=False,on_delete=models.CASCADE)
	zona_comun = models.ForeignKey(ZonaComun,null=False,blank=False,on_delete=models.CASCADE)
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	hora_inicio = models.TimeField(null=False,blank=False,default=None,help_text='Ingrese la Hora de Inicio')
	hora_final = models.TimeField(null=False,blank=False,default=None,help_text='Ingrese la Hora Final')
	estado = models.BooleanField(default=False,verbose_name = "Pagado")
	anexo_pago = models.BooleanField(default=False,verbose_name = "Anexo Pago")
	confirmada = models.BooleanField(default=False,verbose_name = "Confirmada")
    
	class Meta:
		ordering=["zona_comun"]
		verbose_name='Reserva Zona Común'
		verbose_name_plural='Reservas Zonas Comunes'

	def __str__(self):
		return self.zona_comun.descripcion

""" class ReservaZonasComunes(models.Model):
	user = models.ForeignKey(User,verbose_name="Residente",default='',on_delete=models.CASCADE)
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
	anexo = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	pagado = models.BooleanField(null=True,blank=True,default=False)
	zona_comun = models.ForeignKey(ZonaComun,on_delete=models.CASCADE,verbose_name='zona_comun')
	fecha = models.DateField ()
	horas_disponibles = (
        
		(1, '1:00'),
        (2, '2:00'),
        (3, '3:00'),
        (4, '4:00'),
        (5, '5:00'),
        (6, '6:00'),
        (7, '7:00'),
        (8, '8:00'),
        (9, '9:00'),
        (10, '10:00'),
        (11, '11:00'),
        (12, '12:00'),
        (13, '13:00'),
		(14, '14:00'),
		(15, '15:00'),
		(16, '16:00'),
		(17, '17:00'),
		(18, '18:00'),
		(19, '19:00'),
		(20, '20:00'),
		(21, '21:00'),
		(22, '22:00'),
		(23, '23:00'),
		(24, '24:00'),
    )
	hora_id = models.IntegerField (choices = horas_disponibles) # almacenar números, parámetros de opciones
	class Meta:
		unique_together = (# Las tres articulaciones son únicas, evitando que alguien vuelva a reservar
            ('zona_comun', 'fecha', 'hora_id'),
        )
    
	def __str__(self):
		return str (self.user) + "reservado" + str (self.zona_comun) """

""" class ReservaZonasComunes(models.Model):
	TYPE_HORARIO = (
		('AM', 'AM'),
		('PM', 'PM'),
	)
	zona_comun = models.ForeignKey(ZonaComun,on_delete=models.CASCADE,verbose_name='zona_comun')
	
	fecha = models.DateField(default=datetime.now,verbose_name='Fecha')
	
	fecha_inicial = models.DateField(default=datetime.now,verbose_name='Fecha Final')
	hora_inicial = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(12)],verbose_name='Hora Inicial')
	minuto_inicial = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(60)],verbose_name='Minuto Inicial')
	
	fecha_final = models.DateField(default=datetime.now,verbose_name='Fecha Final')
	hora_final = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(12)],verbose_name='Hora Final')
	minuto_final = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(60)],verbose_name='Minuto Final')
		
	horas = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(12)],verbose_name='Horas')
	minutos = models.IntegerField(default=0,validators=[MinValueValidator(1), MaxValueValidator(60)],verbose_name='Minutos')

	residente = models.ForeignKey(User,verbose_name="Residente",default='',on_delete=models.CASCADE)
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
	anexo = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	pagado = models.BooleanField(null=True,blank=True,default=False)

	class Meta:
		ordering=["fecha_inicial"]
		verbose_name='Reserva Zona Común'
		verbose_name_plural='Reserva Zonas Comunes'
		unique_together = (('zona_comun', 'fecha_inicial', 'hora_inicial'))
		
	def __str__(self):
		return str (self.residente) + "reservado" + str (self.zona_comun) """



""" class Perfil(models.Model):
	residente = models.OneToOneField(User, on_delete=models.CASCADE)
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior',related_name='profile_interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento',related_name='profile_apartamento')

	class Meta:
		ordering=["interior","apartamento"]
		verbose_name='Perfil'
		verbose_name_plural='Perfiles' """

class UserPerfil(models.Model):
	user = models.ForeignKey(User, on_delete=models.CASCADE)
	#nombre =  models.CharField(max_length=100,blank=True,default='',verbose_name='Nombre')
	#usuario = models.CharField(max_length=150,blank=True,default='',verbose_name='Usuario')
	email = models.EmailField(max_length = 254,verbose_name='Email')
	#activa = models.BooleanField(default=True)
	clave = models.CharField(max_length=20,blank=True,default='',verbose_name='Clave')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior',related_name='perfil_interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento',related_name='perfil_apartamento')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Fecha de Creación')
	updated = models.DateTimeField(auto_now=True,verbose_name='Fecha de Edición')

	class Meta:
		ordering = ['interior']
		verbose_name='Perfil Usuario'
		verbose_name_plural='Perfil Usuarios'

	def __str__(self):
		return self.nombre

class TipoActivo(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Nombre')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Activo'
		verbose_name_plural='Tipo Activo'

	def __str__(self):
		return self.descripcion

TIENE_MANTENIMIENTO = (
		('SI','Si'),
		('NO','No'),
		)
ESTADO = (
		('Activo','Activo'),
		('Baja','Baja'),
		)				
class ActivoFijo(models.Model):
	nombre = models.CharField(verbose_name="Nombre", max_length=200)
	tipo_activo = models.ForeignKey(TipoActivo,on_delete=models.CASCADE,verbose_name='Tipo de Activo')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripcion')
	marca = models.CharField(blank=True,null=True,default='',verbose_name="Marca", max_length=50)
	serial = models.CharField(blank=True,null=True,default='',verbose_name="Serial", max_length=50)
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='')
	valor_libros = models.FloatField(null=False,blank=False,default=0,verbose_name='Valor Libros')
	cantidad = models.IntegerField(null=False,blank=False,default=0,verbose_name='Cantidad')
	prestado = models.BooleanField(default=False,verbose_name='En Préstamo')
	mantenimiento =models.CharField(max_length=2,blank=True,default='NO',choices=TIENE_MANTENIMIENTO,verbose_name='Tiene Mantenimiento')
	frecuencia_mantenimiento =  models.IntegerField(null=False,blank=False,default=0,verbose_name='Meses Frec.Mant.')
	ultimo_mantenimiento = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Ultimo Mant.')
	placa_numero = models.CharField(blank=True,null=True,default='',verbose_name="Número de Placa", max_length=10)
	fecha_vence_mantenimiento =  models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Vence Mant.')
	meses_sin_mantenimiento =  models.IntegerField(null=False,blank=False,default=0,verbose_name='Meses sin Mant.')
	dias_sin_mantenimiento =  models.IntegerField(null=False,blank=False,default=0,verbose_name='Días sin Mant.')
	estado =models.CharField(max_length=10,blank=True,default='Activo',choices=ESTADO,verbose_name='eSTADO')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Activo Fijo'
		verbose_name_plural='Activos Fijos'

	def __str__(self):
		return self.nombre

class PrestamoActivoFijo(models.Model):
	activo_fijo = models.ForeignKey(ActivoFijo,on_delete=models.CASCADE,related_name='activo_prestamo')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	responsable =  models.TextField(blank=True,null=True,default='',verbose_name='Responsable')
	cantidad = models.IntegerField(null=False,blank=False,default=0,verbose_name='Cantidad')
	dias = models.CharField(null=False,blank=False,max_length=20,default='',verbose_name='Dias')
	devuelto = models.BooleanField(default=False,verbose_name='Devuelto')
	fecha_devuelto = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Devuelto')
	
	class Meta:
		ordering=["id"]
		verbose_name='Préstamo Activo Fijo'
		verbose_name_plural='Préstamos Activos Fijos'

	def __str__(self):
		return self.activo_fijo.nombre

CAUSA_BAJA_ACTIVO = (
		('Obsolescencia','Obsolescencia'),
		('Desperfecto','Desperfecto'),
		('Mal Estado','Mal Estado'),
		)		

class BajaActivoFijo(models.Model):
	activo_fijo = models.ForeignKey(ActivoFijo,on_delete=models.CASCADE,related_name='activo_baja')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	detalle =  models.TextField(blank=True,null=True,default='',verbose_name='Detalle')
	cantidad = models.IntegerField(null=False,blank=False,default=0,verbose_name='Cantidad')
	causa_baja = models.CharField(max_length=15,blank=True,default='NO',choices=CAUSA_BAJA_ACTIVO,verbose_name='Causa Baja')
		
	class Meta:
		ordering=["fecha"]
		verbose_name='Baja Activo Fijo'
		verbose_name_plural='Bajas Activos Fijos'

	def __str__(self):
		return self.activo_fijo.nombre

class ServicioProveedor(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='descripcion')
	
	class Meta:
		ordering=["descripcion"]
		verbose_name='Servicio Proveedor'
		verbose_name_plural='Servicios Proveedor'

	def __str__(self):
		return self.descripcion

class TipoIdentificacion(models.Model):
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo de Identificacion'
		verbose_name_plural='Tipos de Identificacion'

	def __str__(self):
		return self.descripcion

class Proponente(models.Model):
	cc_nit = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	tipo_identificacion = models.ForeignKey(TipoIdentificacion,on_delete=models.CASCADE,verbose_name='Tipo de Identificación')
	servicio_provee = models.ForeignKey(ServicioProveedor,on_delete=models.CASCADE,verbose_name='Servicio Proponente')
	nombre = models.CharField(max_length=50,null=False,blank=False,default='',verbose_name='Nombre/Razón Social')
	telefono = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Teléfono')
	celular = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular')
	direccion = models.CharField(max_length=80,null=True,blank=True,default='',verbose_name='Dirección')
	email=models.EmailField(max_length=200,verbose_name='Email')
	persona_contacto = models.CharField(max_length=50,null=True,blank=True,default='',verbose_name='Persona Contacto')
	telefono_contacto = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Teléfono Contacto')
	celular_contacto = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular Contacto')
	email_contacto=models.EmailField(max_length=200,null=True,blank=True,default='',verbose_name='Email Contacto')
	calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')
		 
	class Meta:
		ordering=["nombre"]
		verbose_name='Proponentes'
		verbose_name_plural='Proponentes'

	def __str__(self):
		return self.nombre

class Proveedor(models.Model):
	cc_nit = models.CharField(max_length=20,null=False,blank=False,default='',verbose_name='Identificaciòn')
	tipo_identificacion = models.ForeignKey(TipoIdentificacion,on_delete=models.CASCADE,verbose_name='Tipo de Identificación')
	servicio_provee = models.ForeignKey(ServicioProveedor,on_delete=models.CASCADE,verbose_name='Servicio Proveedor')
	nombre = models.CharField(max_length=80,null=False,blank=False,default='',verbose_name='Nombre/Razón Social')
	telefono = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Teléfono')
	celular = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular')
	direccion = models.CharField(max_length=80,null=True,blank=True,default='',verbose_name='Dirección')
	email=models.EmailField(max_length=200,verbose_name='Email')
	persona_contacto = models.CharField(max_length=50,null=True,blank=True,default='',verbose_name='Persona Contacto')
	telefono_contacto = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Teléfono Contacto')
	celular_contacto = models.CharField(max_length=30,null=True,blank=True,default='',verbose_name='Celular Contacto')
	email_contacto=models.EmailField(max_length=200,null=True,blank=True,default='',verbose_name='Email Contacto')
	calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')
		 
	class Meta:
		ordering=["nombre"]
		verbose_name='Proveedor'
		verbose_name_plural='Proveedores'

	def __str__(self):
		return self.nombre.strip()

class TipoContrato(models.Model):
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo de Contrato'
		verbose_name_plural='Tipos de Contratos'

	def __str__(self):
		return self.descripcion


CONTRATO_ACTIVO = (
		('SI','Si'),
		('NO','No'),
		)	

class Contrato(models.Model):
	numero = models.CharField(max_length=10,default='',verbose_name='Número del contrato')
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE)
	objeto = models.CharField(max_length=100,default='',verbose_name='Objeto del contrato')
	fecha_contrato =models.DateField(default=None,verbose_name='Fecha Contrato')
	valor = models.FloatField(default = 0,verbose_name='Valor Contrato')
	valor_anticipo = models.FloatField(default = 0,verbose_name='Valor Anticipo')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	activo = models.CharField(max_length=2,blank=True,default='NO',choices=CONTRATO_ACTIVO,verbose_name='Contrato Activo')
	vigencia = models.IntegerField(default=0,verbose_name='Vigencia en Meses')
	meses_vence =  models.IntegerField(null=False,blank=False,default=0,verbose_name='Meses Vencido')
	fecha_vence =  models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	dias_vence =  models.IntegerField(null=False,blank=False,default=0,verbose_name='Días Vencido')
	tipo_contrato = models.ForeignKey(TipoContrato,on_delete=models.CASCADE,default=1,verbose_name='Tipo de Contrato')
	
	class Meta:
		ordering=["proveedor"]
		verbose_name='Contrato'
		verbose_name_plural='Contratos'

	def __str__(self):
		return (self.numero).strip() + ' ' +(self.objeto)

class Mantenimiento(models.Model):
	activo_fijo = models.ForeignKey(ActivoFijo,on_delete=models.CASCADE,related_name='activo_mantenimiento')
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='proveedor_mantenimiento')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	#fecha_vence =  models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	terminado = models.BooleanField(default=False,verbose_name='Terminado')
	contrato = models.ForeignKey(Contrato,on_delete=models.CASCADE)
	calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')

	class Meta:
		ordering=["id"]
		verbose_name='Mantenimiento'
		verbose_name_plural='Mantenimientos'

	def __str__(self):
		return self.activo_fijo.nombre

	def save(self, *args, **kwargs):
		super(Mantenimiento, self).save(*args, **kwargs)
		self.idactivo = self.activo_fijo_id


class Reparacion(models.Model):
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='proveedor_reparacion')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	terminado = models.BooleanField(blank=True,default=False,verbose_name='Terminado')
	valor = models.FloatField(default = 0,verbose_name='Valor Reparación')
	valor_anticipo = models.FloatField(default = 0,verbose_name='Valor Anticipo')
	observacion =  models.TextField(blank=True,null=True,default='',verbose_name='Observaciones')
	calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')
	fecha_terminacion = models.DateTimeField(null=True,blank=True,default=None,verbose_name='Fecha Terminación')

	class Meta:
		ordering=["id"]
		verbose_name='Reparacion'
		verbose_name_plural='Reparaciones'

	def __str__(self):
		return self.proveedor

class TipoProyecto(models.Model):
	descripcion=models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo de Proyecto'
		verbose_name_plural='Tipos de Proyectos'

	def __str__(self):
		return self.descripcion

APROBADO_SELECCION = (
	    ('No Determinado','No Determinado'), 
		('Asamblea','Asamblea'),
		('Consejo','Consejo'),
		('Administrador','Administrador'),
		)		
class Proyecto(models.Model):
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	tipo_proyecto =   models.ForeignKey(TipoProyecto,default=1,on_delete=models.CASCADE)
	aprobado = models.BooleanField(default=False,verbose_name='Aprobado')
	aprobado_por =models.CharField(max_length=15,default='No Determinado',blank=True,null=True,choices = APROBADO_SELECCION,verbose_name = 'Aprobado Por')
	fecha_aprobacion = models.DateTimeField(null=True,blank=True,default=None,verbose_name='Fecha Aprobación')
	presupuesto = models.FloatField(default = 0,verbose_name='Valor Presupuesto')
	#calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')
	
	class Meta:
		ordering=["id"]
		verbose_name='Proyecto'
		verbose_name_plural='Proyectos'

	def __str__(self):
		return self.descripcion

class ProponenteProyecto(models.Model):
	proyecto = models.ForeignKey(Proyecto,on_delete=models.CASCADE,related_name='proponente_proyecto')
	proponente = models.ForeignKey(Proponente,on_delete=models.CASCADE,related_name='proponente_proyecto')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	valor = models.FloatField(default = 0,verbose_name='Valor Propuesta')
	seleccionado = models.BooleanField(max_length=2,blank=True,default=False,verbose_name='Seleccionado')
	fecha_seleccion = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Selección')
	votos_favor = models.IntegerField(default=0,verbose_name='Votaciones a Favor')
	votos_contra = models.IntegerField(default=0,verbose_name='Votaciones en Contra')
	
	class Meta:
		ordering=["id"]
		verbose_name='Proponente Proyecto'
		verbose_name_plural='Proponente Proyecto'

	def __str__(self):
		return self.descripcion

class Obra(models.Model):
	proveedor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='proveedor_obra')
	interventor = models.ForeignKey(Proveedor,on_delete=models.CASCADE,related_name='interventor_obra')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	terminada = models.BooleanField(default=False,verbose_name='Terminada')
	contrato = models.ForeignKey(Contrato,default='',on_delete=models.CASCADE)
	valor = models.FloatField(default = 0,verbose_name='Valor Obra')
	valor_anticipo = models.FloatField(default = 0,verbose_name='Valor Anticipo')
	valor_pagado = models.FloatField(default = 0,verbose_name='Valor Pagado')
	saldo_pagar = models.FloatField(default = 0,verbose_name='Saldo Por Pagar')
	avance_obra = models.FloatField(default = 0,verbose_name='% Avance Obra')
	calificacion = models.IntegerField(default=0,validators=[MaxValueValidator(5), MinValueValidator(0)],verbose_name='Calificación')
	fecha_terminacion = models.DateTimeField(null=True,blank=True,default=None,verbose_name='Fecha Terminación')

	class Meta:
		ordering=["id"]
		verbose_name='Obra'
		verbose_name_plural='Obras'

	def __str__(self):
		return self.descripcion

	
PROCESO_ACTIVO = (
		('SI','Si'),
		('NO','No'),
		)

class AvanceObra(models.Model):
	obra = models.ForeignKey(Obra,on_delete=models.CASCADE,related_name='obra_entrega_obra')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	descripcion =  models.TextField(blank=True,null=True,default='',verbose_name='Descripción')
	valor = models.FloatField(default = 0,verbose_name='Valor Desembolsado')
	porcentaje_avance = models.FloatField(default = 0,verbose_name='% Avance')
	
	class Meta:
		ordering=["id"]
		verbose_name='Avance Obra'
		verbose_name_plural='Avances Obra'

	def __str__(self):
		return self.descripcion

class ReunionConsejo(models.Model):
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	contenido =  models.TextField(blank=True,null=True,default='',verbose_name='Contenido')
	numero_acta = models.CharField(max_length=10,blank=True,default='',verbose_name='Número Acta')
	hora_inicio =  models.TimeField(blank=True,default=datetime.time(datetime.now()),verbose_name='Hora Inicio')
	hora_final =  models.TimeField(blank=True,default=datetime.time(datetime.now()),verbose_name='Hora Final')
	
	class Meta:
		ordering=["id"]
		verbose_name='Reunion Consejo'
		verbose_name_plural='Reuniones Consejo'

	def __str__(self):
		return str(self.fecha)

COMPROMISO = (
		('SI','Si'),
		('NO','No'),
		)

class CompromisoConsejo(models.Model):
	reunion_consejo = models.ForeignKey(ReunionConsejo,on_delete=models.CASCADE,related_name='reunion_consejo_compromiso')
	compromiso = models.CharField(max_length=250,blank=True,default='',verbose_name='Compromiso')
	cumplido = models.BooleanField(max_length=2,blank=True,default=False,verbose_name='Cumplido')
	fecha_cumplido = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Cumplido')
	
	class Meta:
		ordering=["id"]
		verbose_name='Compromiso Consejo'
		verbose_name_plural='Compromisos Consejo'

	def __str__(self):
		return str(self.reunion_consejo.id)


class DecisionConsejo(models.Model):
	reunion_consejo = models.ForeignKey(ReunionConsejo,on_delete=models.CASCADE,related_name='reunion_consejo_decision')
	decision = models.CharField(max_length=250,blank=True,default='',verbose_name='Decisión')
	numero_votos_contra = models.IntegerField(default=0,verbose_name='Número de Votos Contra')
	numero_votos_favor = models.IntegerField(default=0,verbose_name='Número de Votos Favor')
	numero_votos_abstencion = models.IntegerField(default=0,verbose_name='Número de Votos Abstencion')

		
	class Meta:
		ordering=["id"]
		verbose_name='Decisión Consejo'
		verbose_name_plural='Decisiones Consejo'

	def __str__(self):
		return str(self.reunion_consejo.id)

CARGOS = (
		('*','No determinado'),
		('P','Presidente'),
		('V','Vicepresidente'),
		('S','Secretario'),
		('T','Tesorero'),
		('L','Vocal'),
		)

MIEMBRO_ACTIVO = (
		('SI','Si'),
		('NO','No'),
		)
ENVIO_COMUNICADO = (
		('SI','Si'),
		('NO','No'),
		)		
class MiembroConsejo(models.Model):
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
	nombre = models.CharField(max_length=60,default='',verbose_name='Nombre')
	cargo = models.CharField(max_length=1,default='*',choices=CARGOS,verbose_name='Cargo')
	email=models.EmailField(max_length=254,verbose_name='Email')
	envio = models.BooleanField(max_length=2,default=False,verbose_name='Envío Cominicado')
	activo = models.BooleanField(max_length=2,default=False,verbose_name='Miembro Activo')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	contenido =  RichTextField(blank=True,null=True,default='',verbose_name='Contenido')
	publicar = models.BooleanField(default=False,verbose_name='Publicar en Web')
	comunidad = models.BooleanField(default=False,verbose_name='Publicar sólo a Cominidad') 
	orden = models.IntegerField(default=0,verbose_name='Orden')
	class Meta:
		ordering=["id"]
		verbose_name='Miembro Consejo'
		verbose_name_plural='Miembros Consejo'

	def __str__(self):
		return self.nombre

CARGOS = (
		('*','No determinado'),
		('R','Revisor Fiscal'),
		('L','Contador'),
		)

MIEMBRO_ACTIVO = (
		('SI','Si'),
		('NO','No'),
		)
""" ENVIO_COMUNICADO = (
		('SI','Si'),
		('NO','No'),
		) """

class MiembroComiteConvivencia(models.Model):
	#anio = models.IntegerField(default=0,verbose_name='Año')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento')
	nombre = models.CharField(max_length=60,default='',verbose_name='Nombre')
	email=models.EmailField(max_length=150,verbose_name='Email')
	envio = models.BooleanField(max_length=2,default=False,verbose_name='Envío Cominicado')
	activo = models.BooleanField(max_length=2,default='False',verbose_name='Miembro Activo')
	publicar = models.BooleanField(default=False,verbose_name='Publicar en Web')
	comunidad = models.BooleanField(default=False,verbose_name='Publicar sólo a Cominidad') 
	orden = models.IntegerField(default=0,verbose_name='Orden')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	class Meta:
		ordering=["id"]
		verbose_name='Miembro Comité Convivencia'
		verbose_name_plural='Miembros Comité Convivencia'

	def __str__(self):
		return self.anio

CARGOS = (
		('*','No determinado'),
		('R','Revisor Fiscal'),
		('C','Contador'),
		)

class MiembroStaff(models.Model):
	nombre = models.CharField(max_length=60,default='',verbose_name='Nombre')
	cargo = models.CharField(max_length=1,default='*',choices=CARGOS,verbose_name='Cargo')
	email=models.EmailField(max_length=254,verbose_name='Email')
	envio = models.BooleanField(max_length=2,default='False',verbose_name='Envío Cominicado')
	#activo = models.BooleanField(max_length=2,blank=True,default='False',choices=MIEMBRO_ACTIVO,verbose_name='Miembro Activo')
	#envio = models.BooleanField(max_length=2,default=False,verbose_name='Envío Cominicado')
	foto = models.ImageField(upload_to='static/',null=True,blank=True,default='/static/img/no-avatar.jpg')
	orden = models.IntegerField(default=0,verbose_name='Orden')
	publicar = models.BooleanField(default=False,verbose_name='Publicar en Web')
	comunidad = models.BooleanField(default=False,verbose_name='Publicar sólo a Cominidad') 
	class Meta:
		ordering=["nombre"]
		verbose_name='Miembro Staff'
		verbose_name_plural='Miembros Staff'

	def __str__(self):
		return self.nombre

class InformeRevisor(models.Model):
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	contenido =  models.TextField(blank=True,null=True,default='',verbose_name='Contenido')
	
	class Meta:
		ordering=["id"]
		verbose_name='Informe Revisor'
		verbose_name_plural='Informes Revisor'

	def __str__(self):
		return str(self.fecha)

class RecomendacionRevisor(models.Model):
	informe_revisor = models.ForeignKey(ReunionConsejo,on_delete=models.CASCADE,related_name='recomendacion_auditor')
	recomendacion = models.CharField(max_length=250,blank=True,default='',verbose_name='Recomendación')
	cumplido = models.BooleanField(max_length=2,blank=True,default='False',verbose_name='Cumplido')
	fecha_cumplido = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Cumplido')
	
	class Meta:
		ordering=["id"]
		verbose_name='Recomendacion Auditor'
		verbose_name_plural='Recomendaciones Auditor'

	def __str__(self):
		return str(self.id)

class TipoProceso(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Proceso'
		verbose_name_plural='Tipos Procesos'

	def __str__(self):
		return self.descripcion

class ProcesoJuridico(models.Model):
	proceso_numero = models.CharField(max_length=10,blank=True,default='',verbose_name='Proceso Número')
	tipo_proceso =   models.ForeignKey(TipoProceso,default=1,on_delete=models.CASCADE)
	fecha_inicial = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	abogado = models.ForeignKey(Proveedor,on_delete=models.CASCADE,verbose_name='Abogado',related_name='abogado_proveedor')
	demandante = models.CharField(max_length=100,blank=True,default='',verbose_name='Demandante')
	demandado = models.CharField(max_length=100,blank=True,default='',verbose_name='Demandado')
	juzgado = models.CharField(max_length=100,blank=True,default='',verbose_name='Juzgado')
	contenido =  RichTextField(blank=True,null=True,default='',verbose_name='Contenido')
	interior = models.ForeignKey(Interior,on_delete=models.CASCADE,verbose_name='Interior',related_name='proceso_interior')
	apartamento = models.ForeignKey(Apartamento,on_delete=models.CASCADE,verbose_name='Apartamento',related_name='proceso_apartamento')
	fecha_final = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Final')
	valor_demanda = models.FloatField(null=False,blank=False,default=0,verbose_name='Valor Demanda')
	activo = models.BooleanField(max_length=2,blank=True,default='False')

	class Meta:
		ordering=["fecha_inicial"]
		verbose_name='Proceso Jurídico'
		verbose_name_plural='Procesos Juridicos'

	def __str__(self):
		return str(self.proceso_numero)

class GestionProcesoJuridico(models.Model):
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha Inicial')
	titulo = models.CharField(max_length=100,blank=True,default='',verbose_name='Titulo')
	proceso_juridico = models.ForeignKey(ProcesoJuridico,on_delete=models.CASCADE,related_name='gestion_proceso_juridico')
	gestion =  RichTextField(blank=True,null=True,default='',verbose_name='Contenido') 
		
	class Meta:
		ordering=["id"]
		verbose_name='Recomendacion Auditor'
		verbose_name_plural='Recomendaciones Auditor'

	def __str__(self):
		return str(self.id)

class TipoAsamblea(models.Model):
	descripcion = models.CharField(max_length=100,verbose_name='Descripción')

	class Meta:
		ordering=["descripcion"]
		verbose_name='Tipo Asamblea'
		verbose_name_plural='Tipos Asamblea'

	def __str__(self):
		return self.descripcion
	
class Asamblea(models.Model):
	fecha = models.DateField(null=True,blank=True,default=None,verbose_name='Fecha')
	tipo_asamblea = models.ForeignKey(TipoAsamblea,on_delete=models.CASCADE,related_name='tipo_asamblea')
	contenido =  models.TextField(blank=True,null=True,default='',verbose_name='Contenido')
	numero_acta = models.CharField(max_length=10,blank=True,default='',verbose_name='Número Acta')
	hora_inicio =  models.TimeField(blank=True,default=datetime.time(datetime.now()),verbose_name='Hora Inicio')
	hora_final =  models.TimeField(blank=True,default=datetime.time(datetime.now()),verbose_name='Hora Final')
	class Meta:
		ordering=["id"]
		verbose_name='Asamblea'
		verbose_name_plural='Asambleas'

	def __str__(self):
		return str(self.fecha)

class DecisionAsamblea(models.Model):
	asamblea = models.ForeignKey(Asamblea,on_delete=models.CASCADE,related_name='asamblea_decision')
	decision = models.CharField(max_length=250,blank=True,default='',verbose_name='Decisión')
	numero_votos_contra = models.IntegerField(default=0,verbose_name='Número de Votos Contra')
	numero_votos_favor = models.IntegerField(default=0,verbose_name='Número de Votos Favor')
			
	class Meta:
		ordering=["id"]
		verbose_name='Decisión Asamblea'
		verbose_name_plural='Decisiones Asamblea'

	def __str__(self):
		return str(self.asamblea.id)	

