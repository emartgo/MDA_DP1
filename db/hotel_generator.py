import pandas as pd
import random

ROOT_CSV = 'db/csv/'
# -------------- lectura de las data bases --------------
df_hotels = pd.read_csv('csv/alojamientos_turisticos.csv', delimiter=',',
                        dtype= {
                            "nombre":str,
                            "CCAA":str,
                            "provincia":str,
                            "localidad":str
                        })
df_telf = pd.read_csv('csv/telefono_fijo.csv', delimiter=';',
                      dtype= {
                            "provincia":str,
                            "prefijo":str
                            })
#---------------------------------------------------------

#--------------- Generacion de hoteles -------------------
def hotel_generator():
    hotels = [] #lista de hoteles
    n_hotles = len(df_hotels)
    cif_check = []
    
    for i, turistic_hotel in enumerate(range(n_hotles)):

        hotel = [] #el hotel

        # asignar aleatoriamente un CIF  a cada hotel y comprobar que no se repiten
        cif = str(random.randint(1000000,9999999)) 
        cif =  random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')+ cif + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        while(cif in cif_check):
            cif = str(random.randint(1000000,9999999))
            cif =  random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ') + cif + random.choice('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
        cif_check.append(cif)

        # nombre y ubicacion del hotel
        name = df_hotels["nombre"][i]
        state = df_hotels["CCAA"][i]
        province = df_hotels["provincia"][i]
        location = df_hotels["localidad"][i]

        # generacion de las estrellas del hotel
        stars = random.choices([1,2,3,4,5],weights=[0.05,0.1,0.5,0.25,0.1])[0]

        # telefono fijo con los prefijos correspondientes
        for i, prefix in enumerate(df_telf["provincia"]):
            if province == prefix:
                prefijo = df_telf["prefijo"][i]
                phone = str(prefijo)
                for numbers_left in range(0, 9-len(prefijo)):
                    phone += str(random.randint(0,9))
                phone = "+34 " + phone

        # generacion del email
        email_nombre = name.replace(' ', '_')
        email = email_nombre + random.choices(['@hotmail.com','@gmail.com','@outlook.com'],weights=[0.1,0.85,0.05])[0]

        # tiene piscina, apto para movilidad reducida, pension completa segun estrellas
        if(stars == 5):
            pool = True
            reduced_mobility = True
            full_board = True
        elif(stars >= 3 and stars <= 4):
            pool = random.choices([True, False], weights=[0.65,0.35])
            reduced_mobility = random.choices([True, False], weights=[0.85,0.15])
            if stars == 3:
                full_board = random.choices([True, False], weights=[0.5,0.5])
            else:
                full_board = random.choices([True, False], weights=[0.75,0.25])
        else:
            pool = random.choices([True, False], weights=[0.25,0.75])
            reduced_mobility = random.choices([True, False], weights=[0.5,0.5])
            full_board = False


        #introduce los campos generados en el hotel
        hotel.append(cif)
        hotel.append(name)
        hotel.append(state)
        hotel.append(province)
        hotel.append(location)
        hotel.append(stars)
        hotel.append(phone)
        hotel.append(email)
        # introduce el hotel generado en la lista de hoteles
        hotels.append(hotel)
        
    print(hotels[0])

hotel_generator()
