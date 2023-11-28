from db_connection import *
from user_generator import *
import pandas as pd
# ----------------- users generator ----------------

check_user = user_generator(25)
columns = ["dni", "nombre", "apellido_1", "apellido_2", "sexo", "edad", "comunidad_autonoma", "provincia", "pension", "grado_discapacidad", "estado_civil", "año_inicio_IMSERSO", "viajes_totales_IMSERSO", "viajes_2_year"]
df_check_users = pd.DataFrame(check_user, columns=columns)

counter = 1
for i in df_check_users.index:
    user = df_check_users.loc[i].to_list()
    print(user)
    sql_insert = f"INSERT INTO users (dni, nombre, apellido_1, apellido_2, sexo, edad, comunidad_autonoma, provincia, pension, grado_discapacidad, estado_civil, inicio_imserso, viajes_totales_IMSERSO, viajes_2_year) VALUES ('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}', {user[5]}, '{user[6]}', '{user[7]}', {user[8]}, {user[9]}, '{user[10]}', {user[11]}, {user[12]}, {user[13]});"
    print(sql_insert)
    sql_request(sql_insert)
    counter += 1
    break