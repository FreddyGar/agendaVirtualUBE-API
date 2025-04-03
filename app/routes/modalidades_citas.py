from flask import Blueprint, jsonify, request
from app.services.modalidad_cita_service import (
    get_all_modalidades,
    get_modalidad_by_id,
    create_modalidad,
    update_modalidad,
    delete_modalidad
)

modalidades_bp = Blueprint('modalidades_citas', __name__)

@modalidades_bp.route('/modalidades_citas', methods=['GET'])
def listar_modalidades():
    """
    Obtener todas las modalidades de cita
    ---
    tags:
      - Modalidades de Citas
    responses:
      200:
        description: Lista de modalidades
        schema:
          type: array
          items:
            type: object
            properties:
              id_modalidad:
                type: integer
              nombre_modalidad:
                type: string
              descripcion:
                type: string
    """
    modalidades = get_all_modalidades()
    return jsonify([m.__dict__ for m in modalidades])


@modalidades_bp.route('/modalidades_citas/<int:id>', methods=['GET'])
def obtener_modalidad(id):
    """
    Obtener una modalidad por ID
    ---
    tags:
      - Modalidades de Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la modalidad
    responses:
      200:
        description: Modalidad encontrada
        schema:
          type: object
          properties:
            id_modalidad:
              type: integer
            nombre_modalidad:
              type: string
            descripcion:
              type: string
      404:
        description: Modalidad no encontrada
    """
    modalidad = get_modalidad_by_id(id)
    if modalidad:
        return jsonify(modalidad.__dict__)
    return jsonify({'error': 'Modalidad no encontrada'}), 404


@modalidades_bp.route('/modalidades_citas', methods=['POST'])
def crear_modalidad():
    """
    Crear una nueva modalidad
    ---
    tags:
      - Modalidades de Citas
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre_modalidad
          properties:
            nombre_modalidad:
              type: string
              example: Virtual
            descripcion:
              type: string
              example: Cita por videollamada
    responses:
      201:
        description: Modalidad creada
        schema:
          type: object
          properties:
            message:
              type: string
            id_modalidad:
              type: integer
      400:
        description: Datos inválidos
    """
    data = request.get_json()
    if not data.get('nombre_modalidad'):
        return jsonify({'error': 'nombre_modalidad es requerido'}), 400
    new_id = create_modalidad(data)
    return jsonify({'message': 'Modalidad creada', 'id_modalidad': new_id}), 201


@modalidades_bp.route('/modalidades_citas/<int:id>', methods=['PUT'])
def actualizar_modalidad(id):
    """
    Actualizar una modalidad existente
    ---
    tags:
      - Modalidades de Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la modalidad a actualizar
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre_modalidad
          properties:
            nombre_modalidad:
              type: string
              example: Presencial
            descripcion:
              type: string
              example: Reunión en oficina
    responses:
      200:
        description: Modalidad actualizada
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Modalidad no encontrada
    """
    data = request.get_json()
    if update_modalidad(id, data):
        return jsonify({'message': 'Modalidad actualizada'})
    return jsonify({'error': 'Modalidad no encontrada'}), 404


@modalidades_bp.route('/modalidades_citas/<int:id>', methods=['DELETE'])
def eliminar_modalidad(id):
    """
    Eliminar una modalidad
    ---
    tags:
      - Modalidades de Citas
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID de la modalidad a eliminar
    responses:
      200:
        description: Modalidad eliminada
      404:
        description: Modalidad no encontrada
    """
    if delete_modalidad(id):
        return jsonify({'message': 'Modalidad eliminada'})
    return jsonify({'error': 'Modalidad no encontrada'}), 404
