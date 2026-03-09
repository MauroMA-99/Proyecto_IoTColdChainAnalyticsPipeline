import base64
import json
import smtplib
from email.mime.text import MIMEText

GMAIL_USER = "mauricio2020marquez@gmail.com"
GMAIL_PASSWORD = "hpwd bgeb meyw aoht"

TO_EMAIL = "mauro2017pre@gmail.com"


def temperature_alert(event, context):

    message = base64.b64decode(event['data']).decode('utf-8')
    alert = json.loads(message)

    device_id = alert["device_id"]
    temperature = alert["temperature"]
    location = alert["location"]
    timestamp = alert["timestamp"]

    subject = "🚨 ALERTA DE TEMPERATURA"
    
    body = f"""
ALERTA DE CADENA DE FRÍO

Sensor: {device_id}
Temperatura: {temperature} °C
Ubicación: {location}
Hora: {timestamp}

La temperatura está fuera del rango permitido (2°C - 8°C)
"""

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = GMAIL_USER
    msg["To"] = TO_EMAIL

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(GMAIL_USER, GMAIL_PASSWORD)
    server.sendmail(GMAIL_USER, TO_EMAIL, msg.as_string())
    server.quit()

    print("Email enviado correctamente")