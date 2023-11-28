from db_connection import * 

try:
    # Crear un nuevo cursor
    with conn.cursor() as cursor:
        
        # Preparar la consulta SQL para seleccionar datos
        sql = "SELECT columna1, columna2 FROM tu_tabla"  # Cambia 'tu_tabla', 'columna1', 'columna2' por tus datos reales
        
        # Ejecutar la consulta SQL
        cursor.execute(sql)
        
        # Obtener todos los resultados
        resultados = cursor.fetchall()
        
        # Iterar sobre los resultados y hacer algo con ellos
        for resultado in resultados:
            print(resultado)

except Exception as e:
    # Manejo de la excepción si algo va mal
    print(f"Ocurrió un error: {e}")

finally:
    # Cerrar la conexión
    conn.close()

