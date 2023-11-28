from db_connection import *
from user_generator import *
import pandas as pd
# ----------------- users generator ----------------

check_user = user_generator(1000)
for i in range(len(check_user)):
    user = check_user[i]
    sql_insert = f"INSERT INTO users (dni, nombre, apellido_1, apellido_2, sexo, edad, comunidad_autonoma, provincia, pension, grado_discapacidad, estado_civil, inicio_imserso, viajes_totales_IMSERSO, viajes_2_year) VALUES ('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}', {user[5]}, '{user[6]}', '{user[7]}', {user[8]}, {user[9]}, '{user[10]}', {user[11]}, {user[12]}, {user[13]});"
    sql_request(sql_insert)

    