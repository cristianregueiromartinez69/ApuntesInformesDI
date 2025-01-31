from reportlab.pdfgen import canvas

cadena = ["Tres tristes tigres",  "comen trigo en un trigal", "en que trigal", "comieron los tristes tigres"]

aux = canvas.Canvas("probandoTexto.pdf")
objetoTexto = aux.beginText()

objetoTexto.setTextOrigin(100,500)
objetoTexto.setFont("Helvetica", 12)
