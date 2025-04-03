from app.models.tipo_cita import TipoCita
from app.config.db import get_db_connection

def get_all_tipos_citas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_citas")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return rows

def get_tipo_cita_by_id(id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM tipos_citas WHERE id_tipo_cita = %s", (id,))
    resultado = cursor.fetchone()
    cursor.close()
    conn.close()
    return resultado

def create_tipo_cita(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO tipos_citas (nombre_tipo_cita, descripcion) VALUES (%s, %s)",
        (data['nombre_tipo_cita'], data.get('descripcion', ''))
    )
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def update_tipo_cita(id_tipo_cita, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE tipos_citas SET nombre_tipo_cita = %s, descripcion = %s WHERE id_tipo_cita = %s",
        (data['nombre_tipo_cita'], data.get('descripcion', ''), id_tipo_cita)
    )
    conn.commit()
    actualizado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return actualizado

def delete_tipo_cita(id_tipo_cita):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tipos_citas WHERE id_tipo_cita = %s", (id_tipo_cita,))
    conn.commit()
    eliminado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return eliminado
