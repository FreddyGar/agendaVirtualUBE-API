from flask import Blueprint, request, jsonify, session
from app.services.usuario_service import (
    get_all_usuarios,
    get_usuario_by_id,
    create_usuario,
    update_usuario,
    delete_usuario
)

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    """
    Obtener todos los usuarios
    ---
    tags:
      - Usuarios
    responses:
      200:
        description: Lista de usuarios
        schema:
          type: array
          items:
            type: object
            properties:
              id_usuario:
                type: integer
              nombre:
                type: string
              apellido:
                type: string
              email:
                type: string
              telefono:
                type: string
              estado:
                type: string
              fecha_creacion:
                type: string
              ultima_sesion:
                type: string
              id_perfil:
                type: integer
    """
    usuarios = get_all_usuarios()
    return jsonify([u.__dict__ for u in usuarios])


@usuarios_bp.route('/usuarios/<int:id>', methods=['GET'])
def obtener_usuario(id):
    """
    Obtener un usuario por ID
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario
    responses:
      200:
        description: Usuario encontrado
        schema:
          type: object
          properties:
            id_usuario:
              type: integer
            nombre:
              type: string
            apellido:
              type: string
            email:
              type: string
            telefono:
              type: string
            estado:
              type: string
            fecha_creacion:
              type: string
            ultima_sesion:
              type: string
            id_perfil:
              type: integer
      404:
        description: Usuario no encontrado
    """
    usuario = get_usuario_by_id(id)
    if usuario:
        return jsonify(usuario.__dict__)
    return jsonify({'error': 'Usuario no encontrado'}), 404

@usuarios_bp.route('/usuarios/perfil', methods=['GET'])
def obtener_perfil_usuario():
    """
    Obtener perfil del usuario logueado
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: query
        type: integer
        required: true
        description: ID del usuario logueado
    responses:
      200:
        description: Datos del usuario
        schema:
          type: object
          properties:
            id_usuario:
              type: integer
            nombre:
              type: string
            apellido:
              type: string
            email:
              type: string
            telefono:
              type: string
            estado:
              type: string
            fecha_creacion:
              type: string
            ultima_sesion:
              type: string
            id_perfil:
              type: integer
      404:
        description: Usuario no encontrado
    """
    
    id_usuario = session.get('user_id')
    if not id_usuario:
        return jsonify({'error': 'ID de usuario requerido'}), 400

    usuario = get_usuario_by_id(id_usuario)
    if usuario:
        return jsonify(usuario.to_dict())
    return jsonify({'error': 'Usuario no encontrado'}), 404

@usuarios_bp.route('/usuarios', methods=['POST'])
def crear_usuario():
    """
    Crear un nuevo usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - nombre
            - apellido
            - email
            - contrasena
          properties:
            nombre:
              type: string
              example: Juan
            apellido:
              type: string
              example: Pérez
            email:
              type: string
              example: juan.perez@email.com
            contrasena:
              type: string
              example: secreta123
            telefono:
              type: string
              example: "0987654321"
            estado:
              type: string
              enum: [Activo, Inactivo]
              example: Activo
            id_perfil:
              type: integer
              example: 1
    responses:
      201:
        description: Usuario creado exitosamente
        schema:
          type: object
          properties:
            message:
              type: string
            id_usuario:
              type: integer
      400:
        description: Datos inválidos o incompletos
    """
    data = request.get_json()
    campos_obligatorios = ['nombre', 'apellido', 'email', 'contrasena']
    for campo in campos_obligatorios:
        if campo not in data:
            return jsonify({'error': f'{campo} es requerido'}), 400

    new_id = create_usuario(data)
    return jsonify({'message': 'Usuario creado', 'id_usuario': new_id}), 201

@usuarios_bp.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    """
    Actualizar un usuario
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario a actualizar
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            nombre:
              type: string
              example: Carlos
            apellido:
              type: string
              example: Coronel
            email:
              type: string
              example: carlos@email.com
            contrasena:
              type: string
              example: nuevaContrasena123
            telefono:
              type: string
              example: "0999999999"
            estado:
              type: string
              enum: [Activo, Inactivo]
              example: Activo
            id_perfil:
              type: integer
              example: 2
    responses:
      200:
        description: Usuario actualizado
      404:
        description: Usuario no encontrado
    """
    data = request.get_json()
    print("📥 Recibido en el PUT /usuarios:", data)

    if update_usuario(id, data):
        return jsonify({'message': 'Usuario actualizado'})
    return jsonify({'error': 'Usuario no encontrado'}), 404

@usuarios_bp.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    """
    Eliminar un usuario por ID
    ---
    tags:
      - Usuarios
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del usuario a eliminar
    responses:
      200:
        description: Usuario eliminado
        schema:
          type: object
          properties:
            message:
              type: string
      404:
        description: Usuario no encontrado
    """
    if delete_usuario(id):
        return jsonify({'message': 'Usuario eliminado'})
    return jsonify({'error': 'Usuario no encontrado'}), 404

