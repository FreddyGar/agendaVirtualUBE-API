from app.models.modalidad_cita import ModalidadCita
from app.config.db import get_db_connection

def get_all_modalidades():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modalidades_citas")
    rows = cursor.fetchall()
    cursor.close()
    conn.close()
    return [ModalidadCita.from_dict(row) for row in rows]

def get_modalidad_by_id(id_modalidad):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM modalidades_citas WHERE id_modalidad = %s", (id_modalidad,))
    row = cursor.fetchone()
    cursor.close()
    conn.close()
    return ModalidadCita.from_dict(row) if row else None

def create_modalidad(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO modalidades_citas (nombre_modalidad, descripcion) VALUES (%s, %s)"
    values = (data['nombre_modalidad'], data.get('descripcion', ''))
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def update_modalidad(id_modalidad, data):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = "UPDATE modalidades_citas SET nombre_modalidad = %s, descripcion = %s WHERE id_modalidad = %s"
    values = (data.get('nombre_modalidad'), data.get('descripcion', ''), id_modalidad)
    cursor.execute(sql, values)
    conn.commit()
    actualizado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return actualizado

def delete_modalidad(id_modalidad):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM modalidades_citas WHERE id_modalidad = %s", (id_modalidad,))
    conn.commit()
    eliminado = cursor.rowcount > 0
    cursor.close()
    conn.close()
    return eliminado