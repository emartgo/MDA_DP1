import pandas as pd
import random
from datetime import date, datetime
import numpy as np

ROOT_CSV = 'db/csv/'
# -------------- lectura de las data bases --------------
df_woman_names = pd.read_csv('csv/woman_name.csv', 
                             dtype = {
                                 "nombre": str,
                                 "frec":int
                             })
df_woman_frec_names = df_woman_names["frec"]
df_woman_names = df_woman_names["nombre"]

df_man_names = pd.read_csv('csv/man_name.csv', 
                             dtype = {
                                 "nombre": str,
                                 "frec":int
                             })
df_man_frec_names = df_man_names["frec"]
df_man_names = df_man_names["nombre"]

df_last_names = pd.read_csv('csv/last_name.csv', 
                             dtype = {
                                 "apellido": str,
                                 "frec_pri": int,
                                 "frec_seg": int
                             })
df_frec_1_last_names = df_last_names["frec_pri"]
df_frec_2_last_names = df_last_names["frec_seg"]
df_last_names = df_last_names["apellido"]

df_cities = pd.read_csv('csv/city.csv', delimiter=';',
                        dtype= {
                            "Nombre_CCAA":str,
                            "Nombre_Provincia":str,
                            "id":int,
                            "frec":int
                        })
df_frec_cities = df_cities["frec"]
df_num_prov = df_cities["id"]
df_cities = df_cities[["Nombre_CCAA", "Nombre_Provincia"]]

df_ages = pd.read_csv('csv/edades_españa.csv', delimiter=';',
                        dtype = {
                            "Edad":str,
                            "Total":int
                        })
df_ages["Edad"] = df_ages["Edad"].str.extract("(\d+)").fillna(-1).astype(int)
df_frec_ages = df_ages["Total"]
df_ages = df_ages["Edad"]
df_pension = pd.read_csv('csv/pensiones.csv', delimiter=';',      
                           dtype = {
                               "CUANTIA":str,
                               "JUBILACION":int
                           })
# para calcular la pension solo se tendrá en cuenta la cuantia por jubilacion
df_pension["CUANTIA"] = df_pension["CUANTIA"].str.extract('De \d+,\d+ a (\d+,\d+)')
df_pension["CUANTIA"] = df_pension["CUANTIA"].str.replace(',', '.').astype(float)
df_frec_pension = df_pension["JUBILACION"]
df_pension = df_pension["CUANTIA"]
# --------------------------------------------------------

# ----------------- generacion de usuarios ----------------
def user_generator(param:int):
    users = [] # lista de usuarios
    dni_check = []

    for person in range(param):
        if param >= 89999999: # numero maximo (n DNIs) 
            break

        user = [] # lista de usuario

        # Generar dni y comprobar si esta disponible, si no, se genera otro sucesivamente
        dni = str(random.randint(10000000,99999999))
        dni = dni + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        while(dni in dni_check):
            dni = str(random.randint(10000000,99999999))
            dni = dni + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        dni_check.append(dni)

        # seleccion hombre mujer y su nombre segun su frecuencia
        sex_choice = random.randint(1,2) 
        if(sex_choice == 1):
            name = random.choices(df_man_names, weights=df_man_frec_names, k=1)[0]
            sex = "HOMBRE"
        else:
            name = random.choices(df_woman_names, weights=df_woman_frec_names, k=1)[0]
            sex = "MUJER"

        # seleccion edad segun frecuencia
        age = random.choices(df_ages, weights=df_frec_ages, k=1)[0]
        # Dato importante. La edad es la que se tendrá a finales de año

        # seleccion apellidos segun su frecuencia
        last_name_1 = random.choices(df_last_names, weights=df_frec_1_last_names, k=1)[0]
        last_name_2 = random.choices(df_last_names, weights=df_frec_2_last_names, k=1)[0]

        # seleccion provincia, ciudad segun frecuencia real
        n_city = random.choices(df_num_prov, weights=df_frec_cities, k=1)[0] - 1
        city = df_cities["Nombre_Provincia"].iloc[n_city]
        state = df_cities["Nombre_CCAA"].iloc[n_city]

        # seleccion pension usuario
        pension = random.choices(df_pension, weights=df_frec_pension, k=1)[0]

        # seleccion discapacidad
        if(age >= 65 and age < 70):   
            pobabilities = [0.864,0.136]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 70 and age < 75):   
            pobabilities = [0.816,0.184]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 75 and age < 80):   
            pobabilities = [0.778,0.222]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 80 and age < 85):   
            pobabilities = [0.415,0.585]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 85):   
            pobabilities = [0.868,0.132]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0

        # seleccion estado_civil
        if(age >= 65 and age < 70):
            if(sex == "HOMBRE"):
                marital_status = random.choices(["SOLTERX","CASADX","VIUDX"], weights=[0.102,0.847,0.051])[0]
            else:
                marital_status = random.choices(["SOLTERX","CASADX","VIUDX"], weights=[0.091,0.736,0.173])[0]
        else:
            if(sex == "HOMBRE"):
                marital_status = random.choices(["SOLTERX","CASADX","VIUDX"], weights=[0.061,0.8,0.139])[0]
            else:
                marital_status = random.choices(["SOLTERX","CASADX","VIUDX"], weights=[0.065,0.46,0.475])[0]

        # seleccion año inicio IMSERSO
        actual_year = datetime.now().year
        posible_years = []
        for posible_year in range(65, age+1):
            n = posible_year - 65
            posible_years.append(actual_year-n)
        first_year_IMSERSO = random.choice(posible_years)

        # seleccion viajes_totales IMSERSO y seleccion viajes n - 2 años
        # seleccion destino TOP n-1 año y seleccion n veces cancela sin motivo n-3 años
        total_trips = 0
        trips_n2_years = 0
        top_trip_last_year = 0
        canceled_trips_n3 = 0
        for years in range(first_year_IMSERSO, actual_year):
            trips_per_year = random.choices([0, 1, 2], weights= [0.45, 0.45, 0.1])[0]   # total viajes
            total_trips += trips_per_year
            if(actual_year - years < 4 and trips_per_year > 0): # viajes cancelados en n-3 años
                for trip in range(0,trips_per_year):
                    # Si ha cancelado previamente algun viaje es más propenso a cancelar otra viaje
                    if(canceled_trips_n3 > 0):
                        canceled_trips_n3 += random.choices([0, 1], weights= [0.63, 0.37])[0]
                    else:
                        canceled_trips_n3 += random.choices([0, 1], weights= [0.9, 0.1])[0]
            if(actual_year - years < 3):    # viajes en los ultimos 2 años
                trips_n2_years += trips_per_year
            if(years == actual_year-1 and trips_per_year > 0):  # destino TOP
                top_trip_last_year = random.choices([0, 1], weights= [0.9, 0.1])[0]
        
        # seleccion calidad como cliente
        # cada hotel da una puntuacion del 1 al 5 al cliente segun haya sido como huesped, usuarios que no han viajado nunca tendra -1 y no será tomado en cuenta
        score_per_trip=[]
        mean_score = -1.0
        for trip in range(0,total_trips):
            if(mean_score == -1):
                score = random.choices([1.0, 2.0, 3.0, 4.0, 5.0], weights= [0.05,0.05,0.1,0.2,0.6])[0]
                score_per_trip.append(score)
                mean_score = score
            else:                       # si ha tenido una mala puntuacion es mas probable a que la repita
                if(mean_score > 3):
                    score = random.choices([1.0, 2.0, 3.0, 4.0, 5.0], weights= [0.05,0.05,0.1,0.2,0.6])[0]
                else:
                    score = random.choices([1.0, 2.0, 3.0, 4.0, 5.0], weights= [0.1,0.1,0.15,0.15,0.5])[0]
                score_per_trip.append(score)
                mean_score = float(np.mean(score_per_trip))
        mean_score = round(mean_score,2)
       
        # Introducir usuario en la lista de usuarios
        user.append(dni) 
        user.append(name)
        user.append(last_name_1)
        user.append(last_name_2)
        user.append(sex)
        user.append(int(age))
        user.append(state)
        user.append(city)
        user.append(float(pension))
        user.append(disability_grade)
        user.append(marital_status)
        user.append(first_year_IMSERSO)
        user.append(total_trips)
        user.append(trips_n2_years)
        user.append(canceled_trips_n3)
        user.append(top_trip_last_year)
        user.append(mean_score)
        users.append(user)
        
    
    return users
# --------------------------------------------------------