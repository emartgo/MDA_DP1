from db_connection import *
import datetime
import time

time.sleep(60) # espera 2 minutos para que se cree la base de datos

start = time.time()
PONDERACIONES = [1, 0.01, 0.3, 0.5, 3, 9, 5, 1.5]
# age, pension, disc, tot_trip, tn2, t_can, top, score

sql_usuarios = "SELECT id, age, pension, disability_grade, first_year_IMSERSO, canceled_trips_n3 FROM users"
usuarios = sql_request_select(sql_usuarios)

# ------------- LÓGICA DE PONDERACIONES -------------

sql_values = ""
for usuario in usuarios:
    age = usuario[1]
    pension = usuario[2]
    disability_grade = usuario[3]
    first_year_IMSERSO = usuario[4]
    canceled_trips_n3 = usuario[5]
    ponderacion = 0
    
    ponderacion += PONDERACIONES[0] * age # más cuanto más viejo
    ponderacion += PONDERACIONES[1] * pension # menos cuando más pension
    ponderacion += PONDERACIONES[2] * disability_grade # más cuando más discapacidad
    current_year = datetime.datetime.now().year
    years_in_IMSERSO = current_year - first_year_IMSERSO
    ponderacion += PONDERACIONES[3] * years_in_IMSERSO
    ponderacion -= PONDERACIONES[4] * canceled_trips_n3 # menos cuanto más viajes cancelados en los últimos 3 años
    ponderacion = round(round(ponderacion,2)*100)
    sql_values += f"({usuario[0]}, {ponderacion}),"
    
# ------------- LÓGICA DE PONDERACIONES -------------

sql = "INSERT INTO rankings (user_id, ranking) VALUES"
sql_values = sql_values[:-1] + ";"
sql_request(sql + sql_values)

end = time.time()
print(f"Time elapsed for ranking generator: {round((end - start), 2)} s")