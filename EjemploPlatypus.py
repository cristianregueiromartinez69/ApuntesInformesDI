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
# listas para la tabla
cabeceira = ['', 'Lunes', 'Martes', 'Miercoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
manhana = ['Mañana', 'Estudiar', 'Gimnasio', 'Jugar', 'correr', 'ver al madrid', 'cagar', 'descansar']
tarde = ['Tarde', 'Trabajar', 'Trabajar', 'Cagar', 'Trabajar', 'Trabajar', 'descanso', 'cagar']
Noche = ['Noche', 'descanso', 'Trabajar', 'descanso', 'Trabajar', 'salir', 'descanso', 'furbol']

# se crea la tabla añadiendole la lista
tabla = Table([cabeceira, manhana, tarde, Noche])
documento.append(tabla)

# diferentes estilos para la tabla
tabla.setStyle([('BACKGROUND', (1, 1), (-1, -1), colors.lightgrey)])  # fondo de la tabla
tabla.setStyle([('BOX', (1, 1), (-1, -1), 0.5, colors.darkgrey)])  # caja que engloba la tabla
tabla.setStyle([('INNERGRID', (1, 1), (-1, -1), 0.25, colors.white)])  # lineas de la tabla
tabla.setStyle([('TEXTCOLOR', (0, 0), (0, -1), colors.red)])  # texto de la tabña izquierda
tabla.setStyle([('TEXTCOLOR', (1, 0), (-1, 0), colors.pink)])  # texto de la tabla arriba
tabla.setStyle([('ALIGN', (0, 0), (-1, -1), 'CENTER')])

documento.append(Spacer(0, 20))

datos = [['Esquina sup', '', '02', '03', '04'],
         ['', '', '12', '13', '14'],
         ['20', '21', '22', 'Esquina inf', ''],
         ['30', '31', '32', '', '']]

estilo = [('LINEABOVE', (0, 0), (4,0), 1, colors.blue),
          ('INNERGRID', (0, 0), (-1, -1), 0.5, colors.grey),
          ('BACKGROUND', (0, 0), (1, 1), colors.lavenderblush),
          ('SPAN', (0, 0), (1, 1)),
          ('BACKGROUND', (-2, -2), (-1, -1), colors.bisque),
          ('SPAN', (3, 2), (-1, -1)),
          ('LINEBELOW', (0, -1), (-1, -1), 1, colors.blue),
          ('VALIGN', (0,0), (1,1), 'MIDDLE'),
          ('VALIGN', (-2, -2), (-1,-1), 'MIDDLE'),
          ('ALIGN', (0,0), (-1,-1), 'CENTER')]

tabla2 = Table(data=datos, style=estilo)
documento.append(tabla2)

documento.append(Spacer(0, 20))

temperaturaTablas = [['','Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dec'],
                     ['Máximas', 15, 16, 20, 25, 27, 31, 35, 38, 33, 25, 20, 18],
                     ['Mínimas', -3, -4, -1, 5, 7, 9, 12, 15, 16, 10, 2, -1]]

estiloTablaTemperaturas = [('TEXTCOLOR', (0,0), (-1, 0), colors.grey),
                           ('TEXTCOLOR', (0,1), (0, -1), colors.grey),
                           ('BOX', (1,1), (-1,-1), 1.5, colors.grey),
                           ('INNERGRID', (1,1), (-1, -1), 0.5, colors.grey)]


for i, fila in enumerate(temperaturaTablas):
    for j, valor in enumerate(fila):
        if type(valor) == int:
            if valor > 0:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j,i), (j,i), colors.black))
                if valor > 30:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.red))
                elif valor <= 30 and valor > 20:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j,i), (j,i), colors.orange))
                elif valor <= 20 and valor > 10:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightpink))
                elif valor <= 10 and valor > 0:
                    estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightblue))
            else:
                estiloTablaTemperaturas.append(('TEXTCOLOR', (j, i), (j, i), colors.blue))
                estiloTablaTemperaturas.append(('BACKGROUND', (j, i), (j, i), colors.lightgrey))

tabla3 = Table(data = temperaturaTablas, style=estiloTablaTemperaturas)
documento.append(tabla3)

doc = SimpleDocTemplate("EjemploPlatypusTabla.pdf", pagesize=A4, showBoundary=1)
doc.build(documento)
