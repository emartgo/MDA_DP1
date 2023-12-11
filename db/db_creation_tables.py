from db_connection import *

# ----------------- tables creation ----------------

# user sql_request() function to create the table users in the database


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
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
sql_request(sql_create_hotels_table)

sql_create_bookings_table = """
    CREATE TABLE bookings (
        id INT AUTO_INCREMENT PRIMARY KEY,
        user_id INT,
        hotel_id INT,
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
        ranking FLOAT,
        FOREIGN KEY (user_id) REFERENCES users(id),
        created_at DATETIME DEFAULT CURRENT_TIMESTAMP
    );
"""
sql_request(sql_create_ranking_table)

end = time.time()

print(f"Time elapsed for tables creation: {round((end - start), 2)} s")
