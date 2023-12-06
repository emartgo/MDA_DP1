import mysql.connector
from mysql.connector import Error
import time

# Database connection
def db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='myuser',
            password='mypassword',
            database='mydatabase'
        )
        return connection
    except Error as e:
        print(f"Error connecting to the database: {e}")
        return None

def db_connection_time():
    start_time = time.time()  # Guardar el tiempo de inicio
    while True:
        try:
            connection = mysql.connector.connect(
                host='db',
                user='myuser',
                password='mypassword',
                database='mydatabase'
            )
            print("Database connection successful.")
            return connection
        except Error as e:
            elapsed_time = time.time() - start_time
            print(f"Error connecting to the database: {e}. Retrying...")

            if elapsed_time >= 60:
                print("Connection attempt timed out after 60 seconds.")
                return None

            time.sleep(5)
# SQL request
def sql_request(consulta):
    try:
        connection = db_connection_time()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(consulta)
            connection.commit()
            results = cursor.fetchall()
            return results
    except Error as e:
        print(f"Error al realizar consulta: {e}")
    finally:
        if connection is not None and connection.is_connected():
            connection.close()

def sql_request_select(consulta):
    try:
        connection = db_connection_time()
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

def sql_request_test(consulta):
    try:
        connection = db_connection()
        if connection is not None:
            cursor = connection.cursor()
            cursor.execute(consulta)
            connection.commit()
            results = cursor.fetchall()
            return results
    except Error as e:
        print(f"Error al realizar consulta: {e}")
    finally:
        if connection is not None and connection.is_connected():
            connection.close()
            
def sql_request_test_select(consulta):
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