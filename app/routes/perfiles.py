from flask import Blueprint, jsonify, request
from app.services.perfil_service import (
    get_all_perfiles,
    get_perfil_by_id,
    create_perfil,
    update_perfil,
    delete_perfil
)

perfiles_bp = Blueprint('perfiles', __name__)

@perfiles_bp.route('/perfiles', methods=['GET'])
def listar_perfiles():
    """
    Obtener todos los perfiles
    ---
    tags:
      - Perfiles
    responses:
      200:
        description: Lista de perfiles
    """
    perfiles = get_all_perfiles()
    return jsonify([p.__dict__ for p in perfiles])


@perfiles_bp.route('/perfiles/<int:id>', methods=['GET'])
def obtener_perfil(id):
    """
    Obtener un perfil por ID
    ---
    tags:
      - Perfiles
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Perfil encontrado
      404:
        description: Perfil no encontrado
    """
    perfil = get_perfil_by_id(id)
    if perfil:
        return jsonify(perfil.__dict__)
    return jsonify({'error': 'Perfil no encontrado'}), 404


@perfiles_bp.route('/perfiles', methods=['POST'])
def crear_perfil():
    """
    Crear un nuevo perfil
    ---
    tags:
      - Perfiles
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre_perfil
          properties:
            nombre_perfil:
              type: string
              example: Administrador
            descripcion:
              type: string
              example: Acceso total al sistema
    responses:
      201:
        description: Perfil creado
      400:
        description: Datos inválidos
    """
    data = request.get_json()
    if not data.get('nombre_perfil'):
        return jsonify({'error': 'nombre_perfil es requerido'}), 400
    new_id = create_perfil(data)
    return jsonify({'message': 'Perfil creado', 'id_perfil': new_id}), 201


@perfiles_bp.route('/perfiles/<int:id>', methods=['PUT'])
def actualizar_perfil(id):
    """
    Actualizar un perfil
    ---
    tags:
      - Perfiles
    parameters:
      - name: id
        in: path
        type: integer
        required: true
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre_perfil
          properties:
            nombre_perfil:
              type: string
              example: Supervisor
            descripcion:
              type: string
              example: Acceso limitado al sistema
    responses:
      200:
        description: Perfil actualizado
      404:
        description: Perfil no encontrado
    """
    data = request.get_json()
    if update_perfil(id, data):
        return jsonify({'message': 'Perfil actualizado'})
    return jsonify({'error': 'Perfil no encontrado'}), 404


@perfiles_bp.route('/perfiles/<int:id>', methods=['DELETE'])
def eliminar_perfil(id):
    """
    Eliminar un perfil
    ---
    tags:
      - Perfiles
    parameters:
      - name: id
        in: path
        type: integer
        required: true
    responses:
      200:
        description: Perfil eliminado
      404:
        description: Perfil no encontrado
    """
    if delete_perfil(id):
        return jsonify({'message': 'Perfil eliminado'})
    return jsonify({'error': 'Perfil no encontrado'}), 404
