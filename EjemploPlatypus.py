import os
from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.platypus import Table

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


documento.append(Spacer(0, 20))
fila1 = ['', 'Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
manhana = ['Mañana', 'Estudiar','Gimnasio','Jugar resident evil','correr','ver al madrid','matarme a pajas','descansar']
tarde = ['Tarde', 'Trabajar','Trabajar','Cagar','Trabajar','Trabajar','descanso','cagar y mear']
Noche = ['Noche', 'descanso','Trabajar','descanso','Trabajar','salir','descanso','descanso y furbol']



doc = SimpleDocTemplate("EjemploPlatypus.pdf", pagesize=A4, showBoundary=1)
doc.build(documento)
