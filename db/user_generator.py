import pandas as pd
import random

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
def user_generator(param):
    users = [] # lista de usuarios
    dni_check = []

    for person in range(param):
        user = [] # lista de usuario
        # Generar dni y comprobar si esta disponible, si no, se genera otro sucesivamente
        dni = random.randint(10000000,99999999) 
        while(dni in dni_check):
            dni = random.randint(10000000,99999999)
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
            pobabilities = [0.6536,0.3464]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 70 and age < 75):   
            pobabilities = [0.5914,0.4086]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 75 and age < 80):   
            pobabilities = [0.523,0.477]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33.00,65.00,80.00],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 80 and age < 85):   
            pobabilities = [0.4786,0.5214]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        elif(age >= 85):   
            pobabilities = [0.5432,0.4568]                      # frecuencias obtenidas del INE 
            disable = random.choices([False, True], weights=pobabilities)[0]
            if(disable == True):
                disability_grade = random.choices([33,65,80],weights=[0.57,0.24,0.19])[0]
            else:
                disability_grade = 0
        # seleccion estado_civil
        # seleccion año inicio IMSERSO
        # seleccion viajes_totales IMSERSO
        # seleccion viajes n - 2 años
        # seleccion destino TOP n-1 año
        # seleccion n veces cancela sin motivo n-3 año
        # seleccion calidad como cliente
        # Introducir usuario en la lista de usuarios
        user.append(dni) 
        user.append(name)
        user.append(last_name_1)
        user.append(last_name_2)
        user.append(sex)
        user.append(age)
        user.append(state)
        user.append(city)
        user.append(pension)
        user.append(disability_grade)
        users.append(user)
    
    return users
# --------------------------------------------------------


check_users = user_generator(25)

for user in check_users:
    print(f'{user}')