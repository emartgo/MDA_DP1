import pandas as pd
import random

ROOT_CSV = 'db/csv/'
# -------------- lectura de las data bases --------------
df_woman_names = pd.read_csv('csv/woman_name.csv', 
                             dtype = {
                                 "nombre": str
                             })
df_woman_names = df_woman_names["nombre"].head(5000)
df_man_names = pd.read_csv('csv/man_name.csv', 
                             dtype = {
                                 "nombre": str
                             })
df_man_names = df_man_names["nombre"].head(5000)
df_last_names = pd.read_csv('csv/last_name.csv', 
                             dtype = {
                                 "apellido": str
                             })
df_last_names = df_last_names["apellido"].head(5000)

df_cities = pd.read_csv('csv/city.csv', delimiter=';')
df_cities = df_cities[["Nombre_CCAA", "Nombre_Provincia"]]
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
        sex_choice = random.randint(1,2) # seleccion hombre mujer
        if(sex_choice == 1):
            n = random.randint(0,5000)
            name = df_man_names.iloc[n]
            sex = "HOMBRE"
        else:
            n = random.randint(0,5000)
            name = df_woman_names.iloc[n]
            sex = "MUJER"
        age = random.randint(65, 100)
        n_last_name_1 = random.randint(0,5000)
        n_last_name_2 = random.randint(0,5000)
        last_name_1 = df_last_names.iloc[n_last_name_1]
        last_name_2 = df_last_names.iloc[n_last_name_2]
        n_city = random.randint(0, len(df_cities))
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
