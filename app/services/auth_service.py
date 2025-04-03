from app.config.db import get_db_connection

def login_usuario(codigo, contrasena):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM usuarios WHERE codigo = %s AND contrasena = %s AND estado = 'Activo'",
        (codigo, contrasena)
    )
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return usuario
