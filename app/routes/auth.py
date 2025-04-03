from flask import Blueprint, request, session, jsonify
from app.services.auth_service import login_usuario

auth_bp = Blueprint('auth', __name__, url_prefix='/api/auth')

# Simulación de usuarios en una "base de datos"
USUARIOS = {
    "u12345": {
        "id": 1,
        "codigo": "u12345",
        "nombre": "Freddy",
        "apellido": "Garcia Naranjo",
        "email": "freddygarcia@ube.edu.ec",
        "telefono": "+593321654987",
        "estado": "Activo",
        "ultima_sesion": "19/03/2025",
        "horario": "07:00 AM - 06:00 PM",
        "password": "123456"  # En un sistema real usarías hashes
    }
}

@auth_bp.route('/login', methods=['POST'])
def login():
    """
    Login de usuario
    ---
    tags:
      - Autenticación
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          required:
            - codigo
            - password
          properties:
            codigo:
              type: string
              example: admin
            password:
              type: string
              example: admin
    responses:
      200:
        description: Login exitoso
        schema:
          type: object
          properties:
            message:
              type: string
            usuario:
              type: object
      401:
        description: Credenciales inválidas
    """
    data = request.get_json()
    codigo = data.get('codigo')
    password = data.get('password')

    usuario = login_usuario(codigo, password)
    if usuario:
        session['user_id'] = usuario['id_usuario']  # ⚠️ GUARDAMOS EL ID EN LA SESIÓN
        return jsonify({"message": "Login exitoso", "usuario": usuario})
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401
    

@auth_bp.route('/logout', methods=['POST'])
def logout():
    session.clear()
    return jsonify({"mensaje": "Sesión cerrada"})    
