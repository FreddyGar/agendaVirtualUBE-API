from app.models.cita import Cita
from app.config.db import get_db_connection

def get_all_citas():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT * FROM citas
    """)
    citas = cursor.fetchall()
    cursor.close()
    conn.close()
    return citas


def get_cita_by_id(id_cita):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT *
        FROM citas
        WHERE id_cita = %s
    """, (id_cita,))
    cita = cursor.fetchone()
    cursor.close()
    conn.close()
    return cita

def create_cita(data):
    conn = get_db_connection()
    cursor = conn.cursor()
    sql = """
        INSERT INTO citas (
            id_solicitante, nombre_solicitante, cedula_solicitante,
            id_responsable, id_tipo_cita, id_modalidad,
            fecha_hora_inicio, fecha_hora_fin,
            estado, notas, email_solicitante
        ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        data['id_solicitante'], data['nombre_solicitante'], data['cedula_solicitante'],
        data['id_responsable'], data['id_tipo_cita'], data['id_modalidad'],
        data['fecha_hora_inicio'], data['fecha_hora_fin'],
        data.get('estado', 'Pendiente'),
        data.get('notas', ''),
        data.get('email_solicitante')
    )
    cursor.execute(sql, values)
    conn.commit()
    new_id = cursor.lastrowid
    cursor.close()
    conn.close()
    return new_id

def delete_cita(id_cita):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM citas WHERE id_cita = %s", (id_cita,))
    conn.commit()
    affected = cursor.rowcount
    cursor.close()
    conn.close()
    return affected > 0

def update_cita(id_cita, data):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        sql = """
            UPDATE citas
            SET id_solicitante = %s,
                nombre_solicitante = %s,
                cedula_solicitante = %s,
                id_responsable = %s,
                id_tipo_cita = %s,
                id_modalidad = %s,
                fecha_hora_inicio = %s,
                fecha_hora_fin = %s,
                estado = %s,
                notas = %s,
                email_solicitante = %s
            WHERE id_cita = %s
        """
        values = (
            data.get('id_solicitante'),
            data.get('nombre_solicitante'),
            data.get('cedula_solicitante'),
            data.get('id_responsable'),
            data.get('id_tipo_cita'),
            data.get('id_modalidad'),
            data.get('fecha_hora_inicio'),
            data.get('fecha_hora_fin'),
            data.get('estado', 'Pendiente'),
            data.get('notas'),
            data.get('email_solicitante'),
            id_cita
        )
        cursor.execute(sql, values)
        conn.commit()
        actualizado = cursor.rowcount > 0
        cursor.close()
        conn.close()
        return actualizado
    except Exception as e:
        print(f"[ERROR] {e}")
        return None
