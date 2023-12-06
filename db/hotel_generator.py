import pandas as pd
import random
from datetime import datetime, timedelta
import numpy as np


ROOT_CSV = 'db/csv/'
this_year = datetime.now().year
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
def hotel_generator(n_rooms):
    hotels = [] #lista de hoteles
    n_hotels = len(df_hotels)

    # comprobar que se han pasado por parametro mas plazas de hoteles que hoteles
    if(n_rooms < n_hotels):
        print(f"ERROR, el numero de plazas a asingar debe ser como mínimo {n_hotels} (una plaza por cada hotel)")
        return 0
    
    cif_check = []
    rooms_left = n_rooms
    hotels_left = n_hotels

    for i, turistic_hotel in enumerate(range(n_hotels)):

        hotel = [] #el hotel

        # asignar aleatoriamente un CIF a cada hotel y comprobar que no se repiten
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

        # telefono fijo con los prefijos por provincia correspondientes
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
            pool = random.choices([True, False], weights=[0.65,0.35])[0]
            reduced_mobility = random.choices([True, False], weights=[0.85,0.15])[0]
            if stars == 3:
                full_board = random.choices([True, False], weights=[0.5,0.5])[0]
            else:
                full_board = random.choices([True, False], weights=[0.75,0.25])[0]
        else:
            pool = random.choices([True, False], weights=[0.25,0.75])[0]
            reduced_mobility = random.choices([True, False], weights=[0.5,0.5])[0]
            full_board = False

        # tipo de turismo segun IMSERSO 2023
        if(state == "Andalucía" or state == "Comunidad Valenciana" or state == "Murcia" or state == "Cataluña"):
            travel_mod = random.choices(["Costa peninsular", "Escapada"], weights=[0.75,0.25])[0]
        elif(state == "Canarias" or state == "Islas Baleares"):
            travel_mod = random.choices(["Costa insular", "Escapada"], weights=[0.9,0.1])[0]
        else:
            travel_mod = "Escapada"

        # habitaciones ofertadas por hotel
        if(rooms_left > hotels_left):
            no_overrooms = False
            while(no_overrooms == False):
                avg_rooms = int(round(rooms_left/hotels_left,0))
                half_rooms = int(round(avg_rooms/2,0))
                if(half_rooms<1):
                    half_rooms = 1
                double_rooms = int(round(avg_rooms*2,0))
                rooms = random.randint(half_rooms,double_rooms)     #seleccionamos n habitaciones en un rango
                if(rooms_left - rooms >= hotels_left):
                    no_overrooms = True
        else:   # para evitar que no haya hoteles sin habitacion
            rooms = 1
        
        if(hotels_left == 1):   # completamos las habitaciones sobrantes
            rooms = rooms_left

        # introducir fechas
        # si es un viaje de costa, puede ir en dos temporadas y el viaje ser de 8 o 10 dias
        if(travel_mod == "Costa peninsular" or travel_mod == "Costa insular"):
            season = random.choice(["first", "second"])
            if(season == "first"):
                begin_season = datetime(this_year, 9, 1)
                end_season = datetime(this_year, 11, 15)
                days_between = (end_season - begin_season).days
                initial_date = begin_season + timedelta(days=random.randint(0, days_between))
                trip_days = random.choice([8, 10])
                final_date = initial_date + timedelta(days=trip_days)
            else:
                begin_season = datetime(this_year+1, 3, 15)
                end_season = datetime(this_year+1, 6, 30)
                days_between = (end_season - begin_season).days
                initial_date = begin_season + timedelta(days=random.randint(0, days_between))
                trip_days = random.choice([8, 10])
                final_date = initial_date + timedelta(days=trip_days)
        else:
            begin_season = datetime(this_year, 10, 15)
            end_season = datetime(this_year+1, 5, 15)
            days_between = (end_season - begin_season).days
            initial_date = begin_season + timedelta(days=random.randint(0, days_between))
            trip_days = random.choice([4, 5, 6])
            final_date = initial_date + timedelta(days=trip_days)

        # inclusion de transporte
        if(travel_mod == "Escapada"):
            transportation = True
        else: 
            transportation = random.choices([True, False], weights=[0.5,0.5])[0]

        # incluir las veces que el hotel ha participado en el IMSERSO
        first_year_IMSERSO = random.randint(1978, this_year)

        # incluir la valoracion de los usuarios de IMSERSO
        score_per_trip=[]
        mean_score = -1.0
        years_participated = this_year-1-first_year_IMSERSO
        for trip in range(0, years_participated*rooms):
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

        # precio segun IMSERSO
        if(travel_mod != "Escapada"):
            if(transportation == False):
                if(trip_days >= 9):
                    price = 253.65
                else:
                    price = 210.72
            else:
                if(travel_mod == "Costa peninsular"):
                    if(trip_days >= 9):
                        price = 290.07
                    else:
                        price = 228.93
                else:
                    if(state == "Islas Baleares"):
                        if(trip_days >= 9):
                            price = 331.49
                        else:
                            price = 267.73
                    else:
                        if(trip_days >= 9):
                            price = 435.95
                        else:
                            price = 355.30
        else:
            if(trip_days == 4):
                price = 124.68
            elif(trip_days == 5):
                price = 286.62
            else:
                price = 293.16


        

        
        # introduce los campos generados en el hotel
        hotel.append(cif)
        hotel.append(name)
        hotel.append(state)
        hotel.append(province)
        hotel.append(location)
        hotel.append(stars)
        hotel.append(phone)
        hotel.append(email)
        hotel.append(reduced_mobility)
        hotel.append(pool)
        hotel.append(full_board)
        hotel.append(travel_mod)
        hotel.append(rooms)
        hotel.append(transportation)
        hotel.append(initial_date)
        hotel.append(final_date)
        hotel.append(first_year_IMSERSO)
        hotel.append(mean_score)
        hotel.append(price)
        # introduce el hotel generado en la lista de hoteles
        hotels.append(hotel)
        rooms_left -= rooms
        hotels_left -= 1
    
    return(hotels)

