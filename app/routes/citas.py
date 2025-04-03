from flask import Blueprint, request, jsonify
from app.services.cita_service import (
    get_all_citas,
    get_cita_by_id,
    create_cita,
    update_cita,
    delete_cita
)

citas_bp = Blueprint('citas', __name__)

@citas_bp.route('/citas', methods=['GET'])
def obtener_citas():
    """
    Obtener todas las citas
    ---
    tags:
      - Citas
    responses:
      200:
        description: Lista de citas
        schema:
          type: array
          items:
            type: object
            properties:
              id_cita:
                type: integer
              id_solicitante:
                type: integer
              nombre_solicitante:
                type: string
              cedula_solicitante:
                type: string
              email_solicitante:
                type: string
              id_responsable:
                type: integer
              id_tipo_cita:
                type: integer
              id_modalidad:
                type: integer
              fecha_hora_inicio:
                type: string
              fecha_hora_fin:
                type: string
              estado:
                type: string
              notas:
                type: string
    """
    citas = get_all_citas()
    return jsonify(citas)


@citas_bp.route('/citas/<int:id>', methods=['GET'])
def obtener_cita(id):
    """
    Obtener cita por ID
    ---
    tags:
      - Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la cita
    responses:
      200:
        description: Cita encontrada
        schema:
          type: object
          properties:
            id_cita:
              type: integer
            id_solicitante:
              type: integer
            nombre_solicitante:
              type: string
            cedula_solicitante:
              type: string
            id_responsable:
              type: integer
            id_tipo_cita:
              type: integer
            id_modalidad:
              type: integer
            fecha_hora_inicio:
              type: string
            fecha_hora_fin:
              type: string
            estado:
              type: string
            notas:
              type: string
      404:
        description: Cita no encontrada
    """
    cita = get_cita_by_id(id)
    if cita:
        return jsonify(cita)
    else:
        return jsonify({'error': 'Cita no encontrada'}), 404


@citas_bp.route('/citas', methods=['POST'])
def crear_cita():
    """
    Crear una nueva cita
    ---
    tags:
      - Citas
    parameters:
        - name: body
          in: body
          required: true
          schema:
            type: object
            required:
              - id_solicitante
              - nombre_solicitante
              - cedula_solicitante
              - id_responsable
              - id_tipo_cita
              - id_modalidad
              - fecha_hora_inicio
              - fecha_hora_fin
            properties:
              id_solicitante:
                type: integer
                example: 1
              nombre_solicitante:
                type: string
                example: Juan Pérez
              cedula_solicitante:
                type: string
                example: "0102030405"
              email_solicitante:
                type: string
                example: juanperez@ejemplo.com
              id_responsable:
                type: integer
                example: 2
              id_tipo_cita:
                type: integer
                example: 1
              id_modalidad:
                type: integer
                example: 1
              fecha_hora_inicio:
                type: string
                example: "2025-04-01 10:00:00"
              fecha_hora_fin:
                type: string
                example: "2025-04-01 11:00:00"
              estado:
                type: string
                enum: [Pendiente, Confirmada, Cancelada, Completada]
              notas:
                type: string
                example: Confirmación previa por correo
    responses:
      201:
        description: Cita creada exitosamente
        schema:
          type: object
          properties:
            message:
              type: string
            id_cita:
              type: integer
      400:
        description: Error en los datos enviados
    """
    data = request.get_json()
    campos_obligatorios = [
        'id_solicitante', 'nombre_solicitante', 'cedula_solicitante',
        'id_responsable', 'id_tipo_cita', 'id_modalidad',
        'fecha_hora_inicio', 'fecha_hora_fin'
    ]
    for campo in campos_obligatorios:
        if campo not in data:
            return jsonify({'error': f'{campo} es requerido'}), 400

    new_id = create_cita(data)
    return jsonify({'message': 'Cita creada', 'id_cita': new_id}), 201


@citas_bp.route('/citas/<int:id>', methods=['PUT'])
def actualizar_cita(id):
    """
    Actualizar una cita existente
    ---
    tags:
      - Citas
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - id_solicitante
            - nombre_solicitante
            - cedula_solicitante
            - email_solicitante
            - id_responsable
            - id_tipo_cita
            - id_modalidad
            - fecha_hora_inicio
            - fecha_hora_fin
          properties:
            id_solicitante:
              type: integer
            nombre_solicitante:
              type: string
            cedula_solicitante:
              type: string
            email_solicitante:
              type: string
              example: juanperez@ejemplo.com
            id_responsable:
              type: integer
            id_tipo_cita:
              type: integer
            id_modalidad:
              type: integer
            fecha_hora_inicio:
              type: string
            fecha_hora_fin:
              type: string
            estado:
              type: string
              enum: [Pendiente, Confirmada, Cancelada, Completada]
            notas:
              type: string
    responses:
      200:
        description: Cita actualizada
      404:
        description: Cita no encontrada
    """
    data = request.get_json()
    if update_cita(id, data):
        return jsonify({'message': 'Cita actualizada'})
    return jsonify({'error': 'Cita no encontrada'}), 404


@citas_bp.route('/citas/<int:id>', methods=['DELETE'])
def eliminar_cita(id):
    """
    Eliminar una cita por ID
    ---
    tags:
      - Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la cita a eliminar
    responses:
      200:
        description: Cita eliminada
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Cita no encontrada
    """
    if delete_cita(id):
        return jsonify({'message': 'Cita eliminada'})
    return jsonify({'error': 'Cita no encontrada'}), 404
