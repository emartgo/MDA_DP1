from db_connection import *
from db_connection import *

import mysql.connector #importo la libreria de sql para que me permita ejecutar comandos de sql
conexion=mysql.connector.connect( #me conecto a la base de datos
    host=
    user=
    password=
    database=
)

# ----------------- tables creation ----------------
sql_users = """
CREATE TABLE users (
id INT users PRIMARY KEY, 
name VARCHAR,
last_name_1 VARCHAR(200),
last_name_2 VARCHAR(200), 
dni VARCHAR(10),
sex VARCHAR(200),
age INT,
disability BIT, 
state VARCHAR(200),
city VARCHAR(200),
pension FLOAT
civil_status VARCHAR(200) 
rent INT,
score INT,
registration_date DATETIME,
total_trips_imserso INT,
trips_2_year INT,
)
"""
sql_request(sql_users) 


sql_bookings= '''
CREATE TABLE bookings (
id INT bookings PRIMARY KEY,
id users VARCHAR(200),
id accommodation VARCHAR(200),
start_date DATE,
end_date DATE,
full_board VARCHAR(200), 
)
'''
sql_request(sql_bookings)

sql_accommodations='''
CRETAE TABLE accommodations (
id INT accommodation PRIMARY KEY
name VARCHAR(200),
description VARCHAR(200),
cif VARCHAR(10)
phone_number INT
e-mail VARCHAR(20)
web VARCHAR(200)
stars VARCHAR(5)
)
'''
sql_request(sql_accommodations)