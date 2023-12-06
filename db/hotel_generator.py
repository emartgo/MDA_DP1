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

        # inclusion de transporte 

        # incluir las veces que el hotel ha participado en el IMSERSO

        # incluir la valoracion de los usuarios de IMSERSO

        # precio
        
        #introduce los campos generados en el hotel
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
        # introduce el hotel generado en la lista de hoteles
        hotels.append(hotel)
        rooms_left -= rooms
        hotels_left -= 1
      
    return(hotels)

#hotel_generator(500)
