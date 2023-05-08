import django_tables2 as tables
from pages.models import Pqr,Legislacion,Comunicado

class PqrTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})

    pendiente = tables.Column(
        attrs={"td": {"id": "pendiente"}})    

    class Meta:
        model = Pqr
        fields = ('tipo_pqr','title','remitente','created','apartamento','fecha_respuesta','pendiente')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

    Detalle_Peticion = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a type="button" class="btn-floating btn-short waves-effect waves-light green" type="submit" href="{% url 'ver_detalle_pqr' record.id %}" hdata-toggle="tooltip" data-placement="top" title="Detalle" value="ver" ><i class="material-icons">dehaze</i></a>'''
    )
    Dar_Respuesta = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a type="button" class="btn-floating btn-short waves-effect waves-light red" type="submit" href="{% url 'buscar_respuesta_pqr' record.id %}" hdata-toggle="tooltip" data-placement="top" title="Dar Respuesta PQR"  value="Respuesta" ><i class="material-icons">replay</i></a>'''
    )
    Ver_Respuesta = tables.TemplateColumn(
        '{% csrf_token %}'
        '''<a type="button" class="btn-floating btn-short waves-effect waves-light orange" type="submit" href="{% url 'ver_respuesta_pqr' record.id %}" hdata-toggle="tooltip" data-placement="top" title="Ver Respuesta PQR"  value="Respuesta" ><i class="material-icons">visibility</i></a>'''
    )

class LegislacionTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})

    class Meta:
        model = Legislacion
        fields = ('title','content')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

    Editar = tables.TemplateColumn(
    '{% csrf_token %}'
    '''<a id="BtnEditarlegislacion" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "editar_legislacion" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
    '{% csrf_token %}'
    '''<a id="BtnBorrarLegislacion" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borrar_legislacion" pk=record.id %}" value="editar"><i class="material-icons">delete</i><</a>'''
    )

class ComunicadosTable(tables.Table):
    id = tables.Column(
        attrs={"td": {"id": "id"}})

    class Meta:
        model = Comunicado
        fields = ('title','content','dias_publicacion','order','created','updated')
        #sequence = ('instance', 'name', )
        template_name = "django_tables2/bootstrap.html"
        attrs = {"class": "table table-hover table-sm"}
        row_attrs = {
            "id": lambda record: record.pk
        }

    Editar = tables.TemplateColumn(
    '{% csrf_token %}'
    '''<a id="BtnEditarlegislacion" type="button" class="btn-floating btn-short waves-effect waves-light orange" href="{% url "editar_comunicado" pk=record.id %}" value="editar"><i class="material-icons">edit</i></a>'''
    )
    Borrar = tables.TemplateColumn(
    '{% csrf_token %}'
    '''<a id="BtnBorrarLegislacion" type="button" class="btn-floating btn-short waves-effect waves-light brown" href="{% url "borrar_comunicado" pk=record.id %}" value="borrar"><i class="material-icons">delete</i><</a>'''
    )            