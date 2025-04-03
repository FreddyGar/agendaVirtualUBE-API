from flask import Blueprint, request, jsonify
from app.services.email_service import enviar_correo

utils_bp = Blueprint('utils', __name__)

@utils_bp.route('/email', methods=['POST'])
def enviar_email():
    """
    Enviar correo a uno o varios destinatarios
    ---
    tags:
      - Utilidades
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - to
            - subject
            - body
          properties:
            to:
              type: array
              items:
                type: string
              example: ["correo1@dominio.com", "correo2@dominio.com"]
            subject:
              type: string
              example: "Recordatorio de cita"
            body:
              type: string
              example: "Esta es una prueba para múltiples correos"
    responses:
      200:
        description: Correo enviado exitosamente
      400:
        description: Faltan datos
      500:
        description: Error inesperado
    """
    try:
        data = request.get_json()
        to = data.get('to')
        subject = data.get('subject')
        body = data.get('body')

        if not to or not subject or not body:
            return jsonify({"error": "Campos 'to', 'subject' y 'body' son obligatorios"}), 400

        # Asegurar que sea lista
        if isinstance(to, str):
            to = [to]

        enviar_correo(to, subject, body)
        return jsonify({"message": "Correo enviado exitosamente"}), 200

    except Exception as e:
        return jsonify({"error": "Ocurrió un error inesperado", "detalle": str(e)}), 500

