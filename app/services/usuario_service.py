from app.models.usuario import Usuario
from app.config.db import get_db_connection

def get_all_usuarios():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios')
    usuarios = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Usuario.from_dict(u) for u in usuarios]

def get_usuario_by_id(id_usuario):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM usuarios WHERE id_usuario = %s', (id_usuario,))
    usuario = cursor.fetchone()
    cursor.close()
    conn.close()
    return Usuario.from_dict(usuario) if usuario else None

def create_usuario(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO usuarios (nombre, apellido, email, contrasena, telefono, estado, id_perfil)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['nombre'],
        data['apellido'],
        data['email'],
        data['contrasena'],
        data.get('telefono', ''),
        data.get('estado', 'Activo'),
        data.get('id_perfil', None)
    )
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def delete_usuario(id_usuario):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM usuarios WHERE id_usuario = %s", (id_usuario,))
    conn.commit()
    eliminado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return eliminado

def update_usuario(id_usuario, data):
    conn = get_db_connection()
    cursor = conn.cursor()

    campos_actualizables = ['nombre', 'apellido', 'email', 'contrasena', 'telefono', 'estado', 'id_perfil']
    campos_sql = []
    valores = []

    for campo in campos_actualizables:
        if campo in data and data[campo] is not None:
            campos_sql.append(f"{campo} = %s")
            valores.append(data[campo])

    if not campos_sql:
        return False  # No hay nada que actualizar

    sql = f"""
        UPDATE usuarios
        SET {', '.join(campos_sql)}
        WHERE id_usuario = %s
    """
    valores.append(id_usuario)

    cursor.execute(sql, valores)
    conn.commit()
    actualizado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return actualizado

