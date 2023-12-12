from db_connection import *
from user_generator import *
from hotel_generator import *
import pandas as pd
import time


USERS = 2000
# ----------------- users ingestion ----------------
start = time.time()
time.sleep(10)

users = user_generator(USERS)
users_for_sql = ""
for user in users:
    user_set = tuple(user)
    users_for_sql += str(user_set) + ",\n"
users_for_sql = users_for_sql[:-2]
users_for_sql += ";"
sql_insert_users = f"""
INSERT INTO users (dni, nombre, last_name_1, last_name_2, sex, age, state, city, pension, disability_grade, marital_status, first_year_IMSERSO, total_trips, trips_n2_years, canceled_trips_n3, top_trip_last_year, mean_score) 
VALUES """ + users_for_sql
sql_request(sql_insert_users)

# ----------------- hotels ingestion ----------------
hotels = hotel_generator(USERS-500)
hotels_for_sql = ""
for hotel in hotels:
    hotel_set = tuple(hotel)
    hotels_for_sql += str(hotel_set) + ",\n"
    
hotels_for_sql = hotels_for_sql[:-2]
hotels_for_sql += ";"

sql_insert_hotels = f"""
    INSERT INTO hotels (cif, name, state, province, location, stars, phone, email, reduced_mobility, pool, full_board, travel_mod, rooms)
    VALUES """ + hotels_for_sql
sql_request(sql_insert_hotels)

end = time.time()
print(f"Time elapsed for data ingestion: {round((end - start), 2)} s")