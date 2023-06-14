# link para ativar o acesso a app menos segura do gmail:
# https://myaccount.google.com/u/1/lesssecureapps
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# import smtplib

# mensaje = MIMEMultipart()
# mensaje['From'] = 'Hola mundo'
# mensaje['To'] = 'correo_electronico'
# mensaje['Subject'] = 'Esta es una prueba'
# cuerpo = MIMEText("Cuero del mensaje")
# mensaje.attach(cuerpo)

# with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
#     smtp.ehlo()
#     smtp.starttls()
#     smtp.login("correo_electronico", "3QSqN*lF")
#     smtp.send_message(mensaje)
#     print("Mensaje enviado...")

# Para adjuntar una imagen
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

path = Path("modulos-nativos/Fondo.jpg")
mime_image = MIMEImage(path.read_bytes())
mensaje = MIMEMultipart()
mensaje['From'] = 'Hola mundo'
mensaje['To'] = 'correo_electronico'
mensaje['Subject'] = 'Esta es una prueba'
cuerpo = MIMEText("Cuero del mensaje")
mensaje.attach(cuerpo)
mensaje.attach(mime_image)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login("correo_electronico", "Contrasenia")
    smtp.send_message(mensaje)
    print("Mensaje enviado...")
