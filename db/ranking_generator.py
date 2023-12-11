from db_connection import *
import datetime
import time

time.sleep(60) # espera 2 minutos para que se cree la base de datos

start = time.time()
PONDERACIONES = [1, 0.01, 0.3, 0.5, 3, 9, 5, 1.5]
# age, pension, disc, tot_trip, tn2, t_can, top, score

sql_usuarios = "SELECT id, age, pension, disability_grade, total_trips, trips_n2_years, canceled_trips_n3, top_trip_last_year, mean_score FROM users"
usuarios = sql_request_select(sql_usuarios)

# ------------- LÓGICA DE PONDERACIONES -------------

sql_values = ""
for usuario in usuarios:
    age = usuario[1]
    pension = usuario[2]
    disability_grade = usuario[3]
    total_trips = usuario[4]
    trips_n2_years = usuario[5]
    canceled_trips_n3 = usuario[6]
    top_trip_last_year = usuario[7]
    mean_score = usuario[8]
    ponderacion = 0
    
    ponderacion += PONDERACIONES[0] * age # más cuanto más viejo
    ponderacion -= PONDERACIONES[1] * pension # menos cuando más pension
    ponderacion += PONDERACIONES[2] * disability_grade # más cuando más discapacidad
    ponderacion += PONDERACIONES[3] * total_trips # mas cuanto mas uso 
    ponderacion -= PONDERACIONES[4] * trips_n2_years # menos cuanto mas uso cercano (preferencia al que no ha usadao el IMSERSO)
    ponderacion -= PONDERACIONES[5] * canceled_trips_n3 # menos si cancela sin justificacion
    ponderacion -= PONDERACIONES[6] * top_trip_last_year # menos si fue a un sitio top
    if(mean_score<0):                                   
        ponderacion += PONDERACIONES[7] * 5         # si no ha usado el IMSERSO puntuacion maxima
    else:
        ponderacion += PONDERACIONES[7] * mean_score    # mas a mas puntuacion de usuario

    ponderacion = round(ponderacion,2)
    sql_values += f"({usuario[0]}, {ponderacion}),"
    
# ------------- LÓGICA DE PONDERACIONES -------------

sql = "INSERT INTO rankings (user_id, ranking) VALUES"
sql_values = sql_values[:-1] + ";"
sql_request(sql + sql_values)

end = time.time()
print(f"Time elapsed for ranking generator: {round((end - start), 2)} s")