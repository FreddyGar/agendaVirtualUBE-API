import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host='34.42.221.123',
        database='db_ubetesis',
        user='desarrollo',
        password='desarrolloUbeTesis#.'
    )
