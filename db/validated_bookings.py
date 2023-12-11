from db_connection import *

time.sleep(100)

sql_users = "SELECT user_id, ranking from rankings ORDER BY ranking DESC;"
users = sql_request_select(sql_users)

for user in users:
    sql_booking = "SELECT hotel_id FROM bookings WHERE user_id = " + str(user[0]) + ";"
    bookings = sql_request_select(sql_booking)
    for booking in bookings:
        sql_available_room = "SELECT rooms, name FROM hotels WHERE id = " + str(booking[0]) + ";"
        rooms = sql_request_select(sql_available_room)
        available_room = rooms[0][0]
        if available_room > 0:
            # Atribuimos la habitación
            sql_atribute_room = f"UPDATE bookings SET validated = '1' WHERE user_id = '{user[0]}' and hotel_id = '{booking[0]}';"
            sql_request(sql_atribute_room)
            sql_reduce_room = f"UPDATE hotels SET rooms = '{available_room - 1}' WHERE id = '{booking[0]}';"
            sql_request(sql_reduce_room)
            sql_message_user = f"UPDATE users SET message = 'Tu reserva en el hotel {rooms[0][1]} ha sido validada.' WHERE id = '{user[0]}';"
            sql_request(sql_message_user)
            break
    sql_message_user = f"UPDATE users SET message = 'NO has conseguido reserva en esta convocatoria' WHERE id = '{user[0]}';"
    sql_request(sql_message_user)
