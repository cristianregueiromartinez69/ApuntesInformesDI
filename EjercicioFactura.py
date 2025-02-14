import os

from reportlab.graphics.shapes import Drawing, Line
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Frame, PageTemplate, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.graphics.shapes import Drawing
from reportlab.graphics.widgets.markers import makeMarker
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table


hojaEstilo = getSampleStyleSheet()

estiloParrafoFactura = ParagraphStyle(
    name="titulo",
    fontSize=15,
    textColor=colors.green,
    fontName="Helvetica-Bold",
)

estilosNumeroFecha = ParagraphStyle(
    name="text",
    fontSize=8,
    textColor=colors.green
)

estiloInformacion = ParagraphStyle(
    name="informacion",
    fontSize=16,
    fontName="Helvetica-Bold",
    textColor=colors.green
)

estiloInformacionDatos = ParagraphStyle(
    name = "datos",
    fontSize=12,
    textColor=colors.green,
    fontName="Helvetica-Oblique"
)

estiloRespuestas = ParagraphStyle(
    name = "respuestas",
    fontSize = 10,
    textColor=colors.black,
    fontName="Helvetica"
)

estiloCalculoTabla = ParagraphStyle(
    name = "total",
    fontSize=20,
    textColor=colors.white,
    fontName="Helvetica"
)

estilosConfianza = ParagraphStyle(
    name="text",
    fontSize=13,
    textColor=colors.black,
    fontName="Helvetica-Bold"
)


#informacion izquierda
parrafoFactura = Paragraph("FACTURA SIMPLIFICADA", estiloParrafoFactura)
parrafoFechaEmision = Paragraph("Fecha Emisión: 20/12/2022", estilosNumeroFecha)
parrafoNumeroFactura = Paragraph("Número de Factura: 10001", estilosNumeroFecha)
logoImagenFactura = Image(os.path.relpath("C:/Users/crm23/OneDrive/Imágenes/umbrellaCorp.png"), width=50, height=50)

#informacion derecha
parrafoNombreEmpresa = Paragraph("UMBRELLA CORPORATION", estiloInformacion)

parrafoDirrecion = Paragraph("Dirección:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Rúa Principe, 18", estiloInformacionDatos)

parrafoCiudad = Paragraph("Ciudad y País:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;Vigo", estiloInformacionDatos)

parrafoNif = Paragraph("CIF/NIF:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;36039618K", estiloInformacionDatos)

parrafoTelefono = Paragraph("Teléfono:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;680997886", estiloInformacionDatos)

parrafoEmail = Paragraph("Mail:&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;primopluscontactos@outlook.com", estiloInformacionDatos)

parrafoGracias = Paragraph("GRACIAS POR SU CONFIAZA", estilosConfianza)

#tabla

def calculo_importe(valor1, valor2):
    resultado = float(valor1) * float(valor2)
    return str(resultado)

def calculoTotal(valor1, valor2, valor3, valor4, valor5, valor6):
    resultado = float(valor1) + float(valor2) +  float(valor3) + float(valor4) + float(valor5) + float(valor6)
    return str(resultado)


cabecera = ["Descripción", "Importe", "Cantidad", "Total"]
producto1 = ["metralletas", "450.2", "20", calculo_importe("450.2", "20")]
producto2 = ["extintores", "100", "5", calculo_importe("100", "5")]
producto3 = ["agujas", "6.15", "125", calculo_importe("6.15", "125")]
producto4 = ["carne de cerdo", "3.80", "245", calculo_importe("3.80", "245")]
producto5 = ["granadas", "78.5", "90", calculo_importe("78.5", "90")]
producto6 = ["tanques", "200000.20", "3", calculo_importe("2000000.20", "3")]

total = ["TOTAL", calculoTotal(producto1[3], producto2[3],
                               producto3[3], producto4[3],
                               producto5[3], producto6[3])]

tabla = Table(
    [cabecera, producto1, producto2, producto3, producto4, producto5, producto6],
    colWidths=[100, 100, 100, 100],
    rowHeights=18
              )
tabla.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
    ('BACKGROUND', (0, 1), (-1, -1), colors.lightgreen),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.black),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
]))

#tabla del resultado
tablaResultado = Table(
    [total,],
    colWidths=[80, 80],
    rowHeights=22
)
tablaResultado.setStyle(TableStyle([
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),
    ('BACKGROUND', (0, 0), (-1, 0), colors.darkgreen),
    ('TEXTCOLOR', (0, 0), (0, -1), colors.white),
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.white),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER')
]))

#linea negra
dibujoLinea = Drawing(300, 10)
linea = Line(25,15,550, 15)
linea.strokeColor = colors.black
linea.strokeWidth = 2
dibujoLinea.add(linea)

frame_info_general = Frame(
    x1=350, y1= 700,
    width=300, height=100,
    showBoundary=0
)

frame_datos_factura = Frame(
    x1=40, y1=500,
    width=300, height=200,
    showBoundary=0
)

frame_tabla_datos = Frame(
    x1 = 100, y1 = 400,
    width=400, height=140,
    showBoundary=0
)

frame_tabla_total = Frame(
    x1=368, y1=350,
    width=100, height=50,
    showBoundary=0
)

frame_linea_separatoria = Frame(
    x1=10, y1=290,
    width=400, height=30,
    showBoundary=0
)

frame_gracias_confianza = Frame(
    x1 = 190, y1 = 230,
    width=240, height=50,
    showBoundary=0
)


plantillaIzquierda = PageTemplate(id="Factura", frames=[frame_info_general, frame_datos_factura, frame_tabla_datos, frame_tabla_total, frame_linea_separatoria, frame_gracias_confianza])

doc = SimpleDocTemplate("EjercicioFactura.pdf", pagesize=A4, showBoundary=0)

doc.addPageTemplates([plantillaIzquierda])


contenido_factura_izquierda = [parrafoFactura, Spacer(0,20), parrafoFechaEmision, Spacer(0, 5),  parrafoNumeroFactura]
contenido_factura_derecha = [parrafoNombreEmpresa, Spacer(0, 20), parrafoDirrecion,
                             Spacer(0,10), parrafoCiudad,  Spacer(0,10),
                             parrafoNif, Spacer(0,10), parrafoTelefono,Spacer(0,10),
                             parrafoEmail]
contenido_tabla = [Spacer(50, 60), tabla]
contenido_total_tabla = [Spacer(0,2), tablaResultado]
contenido_dibujo_linea = [Spacer(width=0, height=10), dibujoLinea]
contenido_gracias = [Spacer(width=0, height=2), parrafoGracias]


doc.build(contenido_factura_izquierda + contenido_factura_derecha + contenido_tabla +  contenido_total_tabla + contenido_dibujo_linea + contenido_gracias)


