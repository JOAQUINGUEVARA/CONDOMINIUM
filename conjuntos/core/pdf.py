from reportlab.pdfgen.canvas import Canvas
from reportlab.platypus import Table
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import cm
try:
    from django.utils import importlib
except ImportError:
    import importlib
from django.http import HttpResponse
from .models import ActivoFijo
from io import BytesIO

def pdf_response(draw_funk, file_name, *args, **kwargs):
    response = HttpResponse(content_type="application/pdf")
    response["Content-Disposition"] = "attachment; filename=\"%s\"" % file_name
    draw_funk(response, *args, **kwargs)
    return response

def draw_header(canvas):
    """ Draws the invoice header """
    canvas.setStrokeColorRGB(0.9, 0.5, 0.2)
    canvas.setFillColorRGB(0.2, 0.2, 0.2)
    canvas.setFont('Helvetica', 16)
    canvas.drawString(18 * cm, -1 * cm, 'ACTIVOS FIJOS')
    #canvas.drawInlineImage(settings.INV_LOGO, 1 * cm, -1 * cm, 250, 16)
    canvas.setLineWidth(4)
    canvas.line(0, -1.25 * cm, 21.7 * cm, -1.25 * cm)

header_func = draw_header

def draw_header(canvas):
    """ Draws the invoice header """
    canvas.setStrokeColorRGB(0.9, 0.5, 0.2)
    canvas.setFillColorRGB(0.2, 0.2, 0.2)
    canvas.setFont('Helvetica', 16)
    canvas.drawString(18 * cm, -1 * cm, 'Invoice')
    canvas.drawInlineImage(settings.INV_LOGO, 1 * cm, -1 * cm, 250, 16)
    canvas.setLineWidth(4)
    canvas.line(0, -1.25 * cm, 21.7 * cm, -1.25 * cm)


def draw_address(canvas):
    """ Draws the business address """
    business_details = (
        u'COMPANY NAME LTD',
        u'STREET',
        u'TOWN',
        U'COUNTY',
        U'POSTCODE',
        U'COUNTRY',
        u'',
        u'',
        u'Phone: +00 (0) 000 000 000',
        u'Email: example@example.com',
        u'Website: www.example.com',
        u'Reg No: 00000000'
    )
    canvas.setFont('Helvetica', 9)
    textobject = canvas.beginText(13 * cm, -2.5 * cm)
    for line in business_details:
        textobject.textLine(line)
    canvas.drawText(textobject)


def draw_footer(canvas):
    """ Draws the invoice footer """
    note = (
        u'Bank Details: Street address, Town, County, POSTCODE',
        u'Sort Code: 00-00-00 Account No: 00000000 (Quote invoice number).',
        u'Please pay via bank transfer or cheque. All payments should be made in CURRENCY.',
        u'Make cheques payable to Company Name Ltd.',
    )
    textobject = canvas.beginText(1 * cm, -27 * cm)
    for line in note:
        textobject.textLine(line)
    canvas.drawText(textobject)

def draw_pdf(buffer, activos):
    """ Draws the invoice """
    canvas = Canvas(buffer, pagesize=A4)
    canvas.translate(0, 29.7 * cm)
    canvas.setFont('Helvetica', 10)

    canvas.saveState()
    header_func(canvas)
    canvas.restoreState()

    #canvas.saveState()
    #footer_func(canvas)
    #canvas.restoreState()

    #canvas.saveState()
    #address_func(canvas)
    #canvas.restoreState()

    # Client address
    """ textobject = canvas.beginText(1.5 * cm, -2.5 * cm)
    textobject.textLine(invoice.address.contact_name)
    textobject.textLine(invoice.address.address_one)
    if invoice.address.address_two:
        textobject.textLine(invoice.address.address_two)
    textobject.textLine(invoice.address.town)
    if invoice.address.county:
        textobject.textLine(invoice.address.county)
    textobject.textLine(invoice.address.postcode)
    textobject.textLine(invoice.address.country.name)
    canvas.drawText(textobject) """

    # Info
    """ textobject = canvas.beginText(1.5 * cm, -6.75 * cm)
    textobject.textLine(u'Invoice ID: %s' % invoice.invoice_id)
    textobject.textLine(u'Invoice Date: %s' % invoice.invoice_date.strftime('%d %b %Y'))
    textobject.textLine(u'Client: %s' % invoice.user.username)
    canvas.drawText(textobject) """

    # Items
    buffer = BytesIO()
    #Canvas nos permite hacer el reporte con coordenadas X y Y
    pdf = Canvas(buffer)
    encabezados = ('Nombre', 'Tipo Activo', 'Cantidad', 'Prestado')
    #Creamos una lista de tuplas que van a contener a las personas
    cuerpo = ActivoFijo.objects.all()
    detalles = [(cuerpo.nombre, cuerpo.tipo_activo.descripcion,cuerpo.cantidad,cuerpo.prestado) for cuerpo in cuerpo]
    #Establecemos el tamaño de cada una de las columnas de la tabla
    table = Table([encabezados] + detalles, colWidths=[12 * cm, 2 * cm, 2.5 * cm, 2.5 * cm])
    tw, th, = table.wrapOn(canvas, 15 * cm, 19 * cm)
    table.drawOn(canvas, 1 * cm, -8 * cm - th)
    y = 770
    for a in cuerpo:
        y -= 8
    # Descontamos el encabezado
    #Establecemos el tamaño de la hoja que ocupará la tabla
    table.wrapOn(pdf, 500, 800)
    #Definimos la coordenada donde se dibujará la tabla
    table.drawOn(pdf, 30,y)
    #stotal = format(total_pedido,',d')
    y -= 10
    canvas.showPage()
    canvas.save()