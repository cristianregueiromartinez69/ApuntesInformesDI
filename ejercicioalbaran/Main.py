import os
from reportlab.graphics.shapes import Drawing, Line
from reportlab.platypus import BaseDocTemplate, Frame, PageTemplate, Paragraph, Spacer, Image, Table, TableStyle
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors

from conexionBD import ConexionBD

#base de datos
base = ConexionBD("modelosClasicos.dat")
base.conectaBD()
base.creaCursor()

#consultas
consultaDatoCliente = base.consultaConParametros("SELECT nomeCliente, apelidosCliente FROM clientes WHERE numeroCliente = ?", 1)

consultaDatoAlbaran = base.consultaConParametros("SELECT numeroAlbara, dataAlbara FROM ventas WHERE numeroCliente = ?", 1)

consultaDatoFechaClienteAlbaran = base.consultaConParametros("SELECT numeroCliente, dataEntrega FROM ventas WHERE numeroAlbara = ?", 1)



#estilos parrafos
albaraEstilo = ParagraphStyle(
    name="albaraEstilo",
    fontName="Helvetica",
    textColor=colors.blue,
    fontSize=12
)

detalleEstilo = ParagraphStyle(
    name="detalleEstilo",
    fontName="Helvetica",
    textColor=colors.blue,
    fontSize=12
)

#parrafos
parrafoAlbara = Paragraph("Albará", albaraEstilo)
parrafodetalle = Paragraph("Detalle", detalleEstilo)

# Tabla Inicial
cabecera = ["MODELOS", "CLASICOS"]

tabla_inicio = Table(
    data=[cabecera],
    colWidths=[80, 80],
    rowHeights=29,
)



tabla_inicio.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (0, 0), colors.black),  # Primera celda con fondo negro
    ('TEXTCOLOR', (0, 0), (0, 0), colors.white),   # Texto blanco en la primera celda

    ('BACKGROUND', (1, 0), (1, 0), colors.white),  # Segunda celda con fondo blanco
    ('TEXTCOLOR', (1, 0), (1, 0), colors.black),   # Texto negro en la segunda celda

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Texto en negrita para ambas celdas
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrado
    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),  # Borde exterior
    ('INNERGRID', (0, 0), (-1, -1), 0.25, colors.white),  # Rejilla interna
]))

#tabla_albara

#datos que poner en la tabla
def checkConsultaCliente(consulta):
    if consulta:
        nome = consulta[0][0]
        apelidos = consulta[0][1]
        return nome, apelidos
nome, apelidos = checkConsultaCliente(consultaDatoCliente)

def checkNumeroAlabara(consulta):
    if consulta:
        numeroAlbara = consulta[0][0]
        fecha = consulta[0][1]
        return numeroAlbara, fecha

numeroAlabara, fecha = checkNumeroAlabara(consultaDatoAlbaran)

def checkfechaClienteAlbara(consulta):
    if consulta:
        nCliente =consulta[0][0]
        data_entrega = consulta[0][1]
        print(nCliente, data_entrega)
        return nCliente, data_entrega

numeroCliente, dataEntrega = checkfechaClienteAlbara(consultaDatoFechaClienteAlbaran)

#elementos
elemento1 = ["Número albará", numeroAlabara, "Data", fecha]
elemento2 = ["Número cliente", numeroCliente, "Data entrega", dataEntrega]
elemento3 = ["Nome cliente", nome, "Apelidos", apelidos]

tabla_datos1 = Table(
    [elemento1, elemento2, elemento3],
    colWidths=[80, 80, 80],
    rowHeights=25
)

tabla_datos1.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, -1), colors.lightblue),
    ('TEXTCOLOR', (0, 0), (0, 0), colors.black),

    #ultimas 2 filas de la primera celda
    ('BACKGROUND', (-2, 0), (-1, 0), colors.blue),
    ('TEXTCOLOR', (-2, 0), (-1, 0), colors.white),

    #ultimas 2 celdas de la segunda fila
    ('BACKGROUND', (-2, 1), (-1, 1), colors.blue),
    ('TEXTCOLOR', (-2, 1), (-1, 1), colors.white),

    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica'),
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),  # Centrado
    ('VALIGN', (0, -1), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),
]))

#tabla detalle
elemento_detalle_1 = ["Código producto", "descripción", "Cantidade", "Prezo unitario"]
elemento_detalle_2 = [1, "Vespa 150", 1, "10500"]
elemento_detalle_3 = [2, "Casco retro", 2, "45"]

tabla_detalle = Table(
    [elemento_detalle_1, elemento_detalle_2, elemento_detalle_3],
    colWidths=[90, 80, 80, 90],
    rowHeights=25
)

tabla_detalle.setStyle(TableStyle([
    ('BACKGROUND', (0, 0), (-1, 0), colors.lightblue),  # Fondo azul claro en la cabecera
    ('TEXTCOLOR', (0, 0), (-1, 0), colors.black),  # Texto negro en la cabecera
    ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),  # Texto en negrita
    ('BACKGROUND', (0, 1), (-1, -1), colors.white),  # Fondo blanco para el resto de filas
    ('TEXTCOLOR', (0, 1), (-1, -1), colors.black),  # Texto negro en el resto de filas
    ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
    ('BOX', (0, 0), (-1, -1), 0.5, colors.darkgrey),
]))

#contenidos

contenido_tablaInicio = [tabla_inicio, Spacer(0, 10)]
contenido_parrafo_albara = [parrafoAlbara, Spacer(0, 10)]
contenido_tabla_albara = [tabla_datos1, Spacer(0, 10)]
contenido_parrafo_detalle = [parrafodetalle, Spacer(0, 10)]
contenido_tabla_detalle = [tabla_detalle, Spacer(0, 10)]

frame_tabl1_inicio = Frame(x1=220, y1=650, width=160, height=50, showBoundary=1)
frame_parrafo_albara = Frame(x1=120, y1=600, width=70, height=30, showBoundary=0)
frame_tabla_albara = Frame(x1=120, y1=500, width=320, height=100, showBoundary=0)
frame_contenido_parrafo_detalle = Frame(x1=120, y1=460, width=100, height=30, showBoundary=0)
frame_tabla_detalle = Frame(x1=120, y1=360, width=320, height=100, showBoundary=0)

def generar_contenido(canvas, doc):
    frame_tabl1_inicio.addFromList(contenido_tablaInicio, canvas)
    frame_parrafo_albara.addFromList(contenido_parrafo_albara, canvas)
    frame_tabla_albara.addFromList(contenido_tabla_albara, canvas)
    frame_contenido_parrafo_detalle.addFromList(contenido_parrafo_detalle, canvas)
    frame_tabla_detalle.addFromList(contenido_tabla_detalle, canvas)

doc = BaseDocTemplate("EjercicioAlbaran.pdf", pagesize=A4)
plantilla = PageTemplate(id="Albaran", frames=[frame_tabl1_inicio], onPage=generar_contenido)
doc.addPageTemplates([plantilla])

doc.build([Spacer(0, 1)])
