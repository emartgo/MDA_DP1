from db_connection import *

# ----------------- tables creation ----------------

# user sql_request() function to create the table users in the database

# -----------------------------------------------------
import mysql.connector #importo la libreria de sql para que me permita ejecutar comandos de sql
conexion=mysql.connector.connect( #me conecto a la base de datos
    host=
    user=
    password=
    database=
)

cursor= conexion.cursor() #creo un cursor para ejecutar comandos de SQL

#Creo la tabla.
create_table_users= '''
CREATE TABLE users (
id INT users PRIMARY KEY, 
Name VARCHAR,
Last_name_1 VARCHAR,
Last_name_2 VARCHAR, 
Dni INT,
Sex VARCHAR,
Age INT,
Disability BIT, 
State VARCHAR,
City VARCHAR,
Rent INT,
Score INT,
Registration_date DATE,
)
'''

#Ejecuto el comando SQL para que crear la tabla.
cursor.excute(create_table_users)

create_table_bookings= '''
CREATE TABLE BOOKINGS (
id INT bookings PRIMARY KEY,
id users VARCHAR,
id accommodation VARCHAR,
Start_date DATE,
End_date DATE,
Full_board VARCHAR, 
)
'''
create_table_accommodation= '''
CRETAE TABLE ACCOMMODATION (
id INT accommodation PRIMARY KEY
Name VARCHAR
Description VARCHAR
Cif VARCHAR
Phone_number VARCHAR
E-mail VARCHAR
Web 
Stars VARCHAR 
)
'''