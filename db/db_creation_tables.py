from db_connection import *
from db_connection import *

# ----------------- tables creation ----------------
sql_users = """
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dni VARCHAR(10),
    nombre VARCHAR(200),
    apellido_1 VARCHAR(200),
    apellido_2 VARCHAR(200),
    sexo VARCHAR(200),
    edad INT,
    comunidad_autonoma VARCHAR(200),
    provincia VARCHAR(200),
    pension FLOAT,
    grado_discapacidad INT,
    estado_civil VARCHAR(200),
    inicio_imserso INT,
    viajes_totales_IMSERSO INT,
    viajes_2_year INT
)
"""
sql_request(sql_users)