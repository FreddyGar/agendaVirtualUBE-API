from app.models.perfil import Perfil
from app.config.db import get_db_connection

def get_all_perfiles():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM perfiles")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [Perfil.from_dict(row) for row in rows]

def get_perfil_by_id(id_perfil):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM perfiles WHERE id_perfil = %s", (id_perfil,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return Perfil.from_dict(row) if row else None

def create_perfil(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO perfiles (nombre_perfil, descripcion) VALUES (%s, %s)",
        (data['nombre_perfil'], data.get('descripcion', ''))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def update_perfil(id_perfil, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE perfiles SET nombre_perfil = %s, descripcion = %s WHERE id_perfil = %s",
        (data['nombre_perfil'], data.get('descripcion', ''), id_perfil)
    )
    conn.commit()
    actualizado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return actualizado

def delete_perfil(id_perfil):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM perfiles WHERE id_perfil = %s", (id_perfil,))
    conn.commit()
    eliminado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return eliminado
