import smtplib
from email.message import EmailMessage

import smtplib
from email.message import EmailMessage

def enviar_correo(to, subject, body, nombre_solicitante=None, fecha_hora_inicio=None):
    remitente = "agendaube@gmail.com"
    smtp_server = "smtp.gmail.com"
    password = "zyeu dpcp plfp vpvb"  # ⚠️ Reemplazar en producción

    # Estructura del asunto
    asunto = f"[Agenda UBE] {subject}"
    if nombre_solicitante and fecha_hora_inicio:
        asunto += f" - {nombre_solicitante} ({fecha_hora_inicio})"

    mensaje = EmailMessage()
    mensaje['Subject'] = asunto
    mensaje['From'] = f"Agenda UBE <{remitente}>"
    mensaje['To'] = ", ".join(to) if isinstance(to, list) else to
    mensaje.set_content(body)

    try:
        servidor = smtplib.SMTP(smtp_server, 587)
        servidor.ehlo()
        servidor.starttls()
        servidor.login(remitente, password)
        servidor.send_message(mensaje)
        servidor.quit()
        return True
    except Exception as e:
        print(f"Error al enviar el correo: {e}")
        return False
