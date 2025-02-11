import os

from reportlab.graphics.shapes import Drawing
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Frame, PageTemplate
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors


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
    fontSize=8,
    fontName="Helvetica",
    color=colors.green
)



parrafoFactura = Paragraph("FACTURA SIMPLIFICADA", estiloParrafoFactura)
logoImagenFactura = Image(os.path.relpath("/home/dam/Imágenes/empresaFake.png"), width=100, height=100)

#informacion
parrafoNombreEmpresa = Paragraph("PRIMOPLUS S.L.", estiloInformacion)


parrafoFechaEmision = Paragraph("Fecha Emisión: DD/MM/AAAA", estilosNumeroFecha)
parrafoNumeroFactura = Paragraph("Número de Factura: 10001", estilosNumeroFecha)

frame_izquierda = Frame(
    x1=400, y1= 700,
    width=300, height=100,
    showBoundary=0
)

frame_derecha = Frame(
    x1=40, y1=400,
    width=300, height=400,
    showBoundary=0
)

plantillaIzquierda = PageTemplate(id="Factura", frames=[frame_izquierda, frame_derecha])




doc = SimpleDocTemplate("EjercicioFactura.pdf", pagesize=A4, showBoundary=0)

doc.addPageTemplates([plantillaIzquierda])


contenido_factura_izquierda = [parrafoFactura, Spacer(0, 40), parrafoFechaEmision, Spacer(0, 5),  parrafoNumeroFactura]
contenido_factura_derecha = [parrafoNombreEmpresa]


doc.build(contenido_factura_izquierda + contenido_factura_derecha)
