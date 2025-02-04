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
imagen = Image(os.path.relpath("/home/dam/Imágenes/vinivini.jpg"), width=150, height=150)
documento.append(imagen)


documento.append(Spacer(0, 20))
#listas para la tabla
cabeceira = ['', 'Lunes','Martes','Miercoles','Jueves','Viernes','Sábado','Domingo']
manhana = ['Mañana', 'Estudiar','Gimnasio','Jugar','correr','ver al madrid','cagar','descansar']
tarde = ['Tarde', 'Trabajar','Trabajar','Cagar','Trabajar','Trabajar','descanso','cagar']
Noche = ['Noche', 'descanso','Trabajar','descanso','Trabajar','salir','descanso','furbol']

#se crea la tabla añadiendole la lista
tabla = Table([cabeceira,manhana,tarde,Noche])
documento.append(tabla)

#diferentes estilos para la tabla
tabla.setStyle([('BACKGROUND', (1,1), (-1,-1), colors.lightgrey)]) #fondo de la tabla
tabla.setStyle([('BOX',(1,1), (-1,-1),0.5, colors.darkgrey)]) # caja que engloba la tabla
tabla.setStyle([('INNERGRID', (1,1), (-1, -1), 0.25, colors.white)]) #lineas de la tabla
tabla.setStyle([('TEXTCOLOR', (0,0), (0,-1), colors.red)]) #texto de la tabña izquierda
tabla.setStyle([('TEXTCOLOR', (1,0), (-1,0), colors.pink)]) # texto de la tabla arriba

documento.append(Spacer(0, 20))

datos = [['Esquina sup', '', '02', '03', '04'],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Esquina inf', ''],
         ['30', '31', '32', '', '']]

estilo = [('GRID', (0,0), (-1,-1), 0.5, colors.grey),
          ('BACKGROUND', (0,0), (1,1), colors.lavenderblush),
          ('SPAN', (0,0), (1,1)),
          ('BACKGROUND', (-2,-2), (-1,-1), colors.bisque),
          ('SPAN', (3,2), (-1,-1))]

tabla2 = Table(data= datos, style= estilo)
documento.append(tabla2)

doc = SimpleDocTemplate("EjemploPlatypusTabla.pdf", pagesize=A4, showBoundary=1)
doc.build(documento)
