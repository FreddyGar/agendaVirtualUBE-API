from flask import Flask, jsonify
from flasgger import Swagger
import mysql.connector  # Necesario para manejar errores de MySQL
import logging
from logging.handlers import RotatingFileHandler
import os
from flask_cors import CORS

# Importar blueprints
from app.routes.usuarios import usuarios_bp
from app.routes.citas import citas_bp
from app.routes.modalidades_citas import modalidades_bp
from app.routes.tipos_citas import tipos_citas_bp
from app.routes.perfiles import perfiles_bp
from app.routes.auth import auth_bp
from app.routes.utils import utils_bp


app = Flask(__name__)
app.secret_key = 'clave_super_secreta_ube_2025'  # Puedes cambiarla por una más segura
CORS(app, supports_credentials=True)  # Permitir CORS con credenciales

# Configurar logging
if not os.path.exists('logs'):
    os.makedirs('logs')

file_handler = RotatingFileHandler('logs/error.log', maxBytes=10240, backupCount=5)
file_handler.setLevel(logging.ERROR)
formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s [en %(pathname)s:%(lineno)d]')
file_handler.setFormatter(formatter)
app.logger.addHandler(file_handler)

# Configurar Swagger
swagger = Swagger(app)

# Registrar los blueprints con prefijo '/api'
app.register_blueprint(usuarios_bp, url_prefix='/api')
app.register_blueprint(citas_bp, url_prefix='/api')
app.register_blueprint(modalidades_bp, url_prefix='/api')
app.register_blueprint(tipos_citas_bp, url_prefix='/api')
app.register_blueprint(perfiles_bp, url_prefix='/api')
app.register_blueprint(auth_bp, url_prefix='/api')
app.register_blueprint(utils_bp, url_prefix='/api')


# 🔴 Aquí comienzan los manejadores globales de errores

# Error específico de MySQL
@app.errorhandler(mysql.connector.Error)
def handle_mysql_error(error):
    app.logger.error(f"MySQL Error: {error}")
    return jsonify({
        "error": "Error en la base de datos",
        "detalle": str(error)
    }), 400

@app.errorhandler(Exception)
def handle_generic_error(error):
    app.logger.error(f"Error inesperado: {error}", exc_info=True)
    return jsonify({
        "error": "Ocurrió un error inesperado",
        "detalle": str(error)
    }), 500


# 🔚 Fin de los manejadores

if __name__ == '__main__':
    print(app.url_map)  # Muestra todas las rutas registradas
    app.run(debug=True)
