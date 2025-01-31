import os
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

hojaEstilo = getSampleStyleSheet()

documento = []

cabecera = hojaEstilo['Heading1']
cabecera.pageBreakBefore = 4
cabecera.keepWithNext = 0
cabecera.backColor = colors.blue

parrafo1 = Paragraph("Cabecera del documento", cabecera)

documento.append(parrafo1)

cadena = "vinicius balon de oro, vinicius balon de oro, vinicius balon de oro" * 1000

estiloP = hojaEstilo['BodyText']
parrafo2 = Paragraph(cadena, estiloP)

documento.append(parrafo2)

documento.append(Spacer(0, 20))
imagen = Image(os.path.relpath("/home/dam/Imágenes/vinivini.jpg"), width=200, height=200)
documento.append(imagen)

doc = SimpleDocTemplate("EjemploPlatypus.pdf", pagesize=A4, showBoundary=1)
doc.build(documento)
