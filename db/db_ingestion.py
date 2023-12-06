from db_connection import *
from user_generator import *
from hotel_generator import *
import pandas as pd

# ----------------- users ingestion ----------------
check_user = user_generator(1300)
for i in range(len(check_user)):
    user = check_user[i]
    sql_insert = f"""
    INSERT INTO users (dni, nombre, last_name_1, last_name_2, sex, age, state, city, pension, disability_grade, marital_status, first_year_IMSERSO, total_trips, trips_n2_years, canceled_trips_n3, top_trip_last_year, mean_score) 
    VALUES ('{user[0]}', '{user[1]}', '{user[2]}', '{user[3]}', '{user[4]}', {user[5]}, '{user[6]}', '{user[7]}', {user[8]}, {user[9]}, '{user[10]}', {user[11]}, {user[12]}, {user[13]}, {user[14]}, {user[15]}, {user[16]});
    """
    sql_request(sql_insert)

# ----------------- hotels ingestion ----------------
check_hotel = hotel_generator(1500)
print(check_hotel)
for i in range(len(check_hotel)):
    hotel = check_hotel[i]
    sql_insert = f"""
    INSERT INTO hotels (cif, name, state, province, location, stars, phone, email, reduced_mobility, pool, full_board, travel_mod, rooms)
    VALUES ('{hotel[0]}', '{hotel[1]}', '{hotel[2]}', '{hotel[3]}', '{hotel[4]}', {hotel[5]}, '{hotel[6]}', '{hotel[7]}', {hotel[8]}, {hotel[9]}, {hotel[10]}, '{hotel[11]}', {hotel[12]});
    """
    sql_request(sql_insert)
    