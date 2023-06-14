from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template
import smtplib

# plantilla = """
#     <b> Hola Mundo! $usuario</b>
# """
# temlate = Template(plantilla)
# cuerpo = temlate.substitute({"usuario": "Chanchito Feliz"})
# cuerpo = temlate.substitute(usuario="Chanchito Feliz")

# Esto es cuando tenemos una plantilla en un archivo html
plantilla = Path("modulos-nativos/plantilla.html").read_text("utf-8")
temlate = Template(plantilla)
cuerpo = temlate.substitute(usuario="Chanchito Triste")


path = Path("modulos-nativos/Fondo.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje['From'] = 'Hola mundo'
mensaje['To'] = 'correo-electonico'
mensaje['Subject'] = 'Esta es una prueba'
cuerpo = MIMEText(cuerpo, 'html')
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("correo-electonico", "Contrasenia")
    smtp.send_message(mensaje)
    print("Mensaje enviado...")
