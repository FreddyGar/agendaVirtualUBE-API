from flask import Blueprint, request, jsonify
from app.services.tipo_cita_service import (
    get_all_tipos_citas,
    get_tipo_cita_by_id,
    create_tipo_cita,
    update_tipo_cita,
    delete_tipo_cita
)

tipos_citas_bp = Blueprint('tipos_citas', __name__)

@tipos_citas_bp.route('/tipos_citas', methods=['GET'])
def obtener_tipos_citas():
    """
    Obtener todos los tipos de cita
    ---
    tags:
      - Tipos de Cita
    responses:
      200:
        description: Lista de tipos de cita
        schema:
          type: array
          items:
            type: object
            properties:
              id_tipo_cita:
                type: integer
              tipo_departamento:
                type: string
              nombre_tipo_cita:
                type: string
              descripcion:
                type: string
    """
    tipos = get_all_tipos_citas()
    return jsonify(tipos)


@tipos_citas_bp.route('/tipos_citas/<int:id>', methods=['GET'])
def obtener_tipo_cita(id):
    """
    Obtener tipo de cita por ID
    ---
    tags:
      - Tipos de Cita
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del tipo de cita
    responses:
      200:
        description: Tipo de cita encontrado
        schema:
          type: object
          properties:
            id_tipo_cita:
              type: integer
            tipo_departamento:
              type: string
            nombre_tipo_cita:
              type: string
            descripcion:
              type: string
      404:
        description: Tipo de cita no encontrado
    """
    tipo = get_tipo_cita_by_id(id)
    if tipo:
        return jsonify(tipo)
    return jsonify({'error': 'Tipo de cita no encontrado'}), 404


@tipos_citas_bp.route('/tipos_citas', methods=['POST'])
def crear_tipo_cita():
    """
    Crear un nuevo tipo de cita
    ---
    tags:
      - Tipos de Cita
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - tipo_departamento
            - nombre_tipo_cita
          properties:
            tipo_departamento:
              type: string
              example: ACADEMICO
            nombre_tipo_cita:
              type: string
              example: Tutoría
            descripcion:
              type: string
              example: Reunión para revisión académica
    responses:
      201:
        description: Tipo de cita creado exitosamente
        schema:
          type: object
          properties:
            message:
              type: string
            id_tipo_cita:
              type: integer
      400:
        description: Error en los datos enviados
    """
    data = request.get_json()
    if 'tipo_departamento' not in data or 'nombre_tipo_cita' not in data:
        return jsonify({'error': 'tipo_departamento y nombre_tipo_cita son requeridos'}), 400

    new_id = create_tipo_cita(data)
    return jsonify({'message': 'Tipo de cita creado', 'id_tipo_cita': new_id}), 201


@tipos_citas_bp.route('/tipos_citas/<int:id>', methods=['PUT'])
def actualizar_tipo_cita(id):
    """
    Actualizar un tipo de cita existente
    ---
    tags:
      - Tipos de Cita
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            tipo_departamento:
              type: string
            nombre_tipo_cita:
              type: string
            descripcion:
              type: string
    responses:
      200:
        description: Tipo de cita actualizado
      404:
        description: Tipo de cita no encontrado
    """
    data = request.get_json()
    if update_tipo_cita(id, data):
        return jsonify({'message': 'Tipo de cita actualizado'})
    return jsonify({'error': 'Tipo de cita no encontrado'}), 404


@tipos_citas_bp.route('/tipos_citas/<int:id>', methods=['DELETE'])
def eliminar_tipo_cita(id):
    """
    Eliminar un tipo de cita por ID
    ---
    tags:
      - Tipos de Cita
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del tipo de cita
    responses:
      200:
        description: Tipo de cita eliminado
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Tipo de cita no encontrado
    """
    if delete_tipo_cita(id):
        return jsonify({'message': 'Tipo de cita eliminado'})
    return jsonify({'error': 'Tipo de cita no encontrado'}), 404
