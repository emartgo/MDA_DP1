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
        # Introducir usuario en la lista de usuarios
        user.append(dni) 
        user.append(name)
        user.append(last_name_1)
        user.append(last_name_2)
        user.append(sex)
        user.append(age)
        user.append(state)
        user.append(city)
        users.append(user)
    
    return users
# --------------------------------------------------------
