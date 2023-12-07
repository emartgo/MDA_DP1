from db_connection import *
import time

# ----------------- tables creation ----------------
start = time.time()

sql_create_users_table = """
    CREATE TABLE users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        dni VARCHAR(12),
        nombre VARCHAR(255),
        last_name_1 VARCHAR(255),
        last_name_2 VARCHAR(255),
        sex VARCHAR(20),
        age INT,
        state VARCHAR(255),
        city VARCHAR(255),
        pension FLOAT,
        disability_grade INT,
        marital_status VARCHAR(255),
        first_year_IMSERSO INT,
        total_trips INT,
        trips_n2_years INT,
        canceled_trips_n3 INT,
        top_trip_last_year INT,
        mean_score FLOAT,
        message VARCHAR(500) DEFAULT NULL,
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
sql_request(sql_create_users_table)

sql_create_ponderacion_table = """
    CREATE TABLE ponderaciones (
        id INT AUTO_INCREMENT PRIMARY KEY,
        description VARCHAR(255),
        weight FLOAT
    );
"""
sql_request(sql_create_ponderacion_table)

sql_create_hotels_table = """
    CREATE TABLE hotels (
        id INT AUTO_INCREMENT PRIMARY KEY,
        cif VARCHAR(255),
        name VARCHAR(255),
        state VARCHAR(255),
        province VARCHAR(255),
        location VARCHAR(255),
        stars INT,
        phone VARCHAR(255),
        email VARCHAR(255),
        reduced_mobility BOOLEAN,
        pool BOOLEAN,
        full_board BOOLEAN,
        travel_mod VARCHAR(255),
        rooms INT,
        transportation BOOLEAN,
        initial_date DATE,
        final_date DATE,
        first_year_IMSERSO INT,
        mean_score FLOAT,
        price FLOAT   
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP

    );
"""
sql_request(sql_create_hotels_table)

sql_create_bookings_table = """
    CREATE TABLE bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        hotel_id INT,
        validated BOOLEAN DEFAULT FALSE,
        FOREIGN KEY (user_id) REFERENCES users(id),
        FOREIGN KEY (hotel_id) REFERENCES hotels(id),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
sql_request(sql_create_bookings_table)

sql_create_ranking_table = """
    CREATE TABLE rankings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        ranking INT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
sql_request(sql_create_ranking_table)

end = time.time()
print(f"Time elapsed for tables creation: {round((end - start), 2)} s")