import mysql.connector
from mysql.connector import Error

# Database connection
def db_connection():
    try:
        connection = mysql.connector.connect(
            host='127.0.0.1',
            user='myuser',
            password='mypassword',
            database='mydatabase'
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None
    
# SQL request
def sql_request(consulta):
    try:
        connection = db_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(consulta)
            results = cursor.fetchall()
            return results
    except Error as e:
        print(f"Error al realizar consulta: {e}")
    finally:
        if connection is not None and connection.is_connected():
            connection.close()