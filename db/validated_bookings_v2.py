from db_connection import *
import time

start = time.time()
time.sleep(100)

# # Obtener todos los usuarios y sus reservas en una consulta
# sql = """
#     SELECT u.user_id, b.hotel_id, h.rooms, h.name 
#     FROM rankings u
#     INNER JOIN bookings b ON u.user_id = b.user_id
#     INNER JOIN hotels h ON b.hotel_id = h.id
#     WHERE b.validated = '0'
#     ORDER BY u.ranking DESC
# """
# users_bookings = sql_request_test_select(sql)
# print(users_bookings)

# user_register = 0
# for user_id, hotel_id, available_rooms, hotel_name in users_bookings:
#     if user_register != user_id:
#         user_check = False
#     user_register = user_id
#     if available_rooms > 0 and user_check == False:
#         sql_atribute_room = f"UPDATE bookings SET validated = '1' WHERE user_id = '{user_id}' and hotel_id = '{hotel_id}';"
#         sql_request_test(sql_atribute_room)
#         sql_reduce_room = f"UPDATE hotels SET rooms = '{available_rooms - 1}' WHERE id = '{hotel_id}';"
#         sql_request_test(sql_reduce_room)
#         sql_message_user = f"UPDATE users SET message = 'Tu reserva en el hotel {hotel_name} ha sido validada.' WHERE id = '{user_id}';"
#         sql_request_test(sql_message_user)
#         user_check = True
#     else:
#         # sql_message_user = f"UPDATE users SET message = 'NO has conseguido reserva en esta convocatoria' WHERE id = '{user_id}';"
#         # sql_request_test(sql_message_user)
#         pass

sql_users = "SELECT user_id, ranking from rankings ORDER BY ranking DESC;"
users = sql_request_select(sql_users)

user_register = 0
for user in users:
    sql_booking = "SELECT hotels.id, hotels.rooms, hotels.name FROM bookings INNER JOIN hotels on hotels.id = bookings.hotel_id WHERE user_id = " + str(user[0]) + ";"
    bookings = sql_request_select(sql_booking)
    check_message = True
    for booking in bookings:
        available_room = booking[1]
        if available_room > 0:
            check_message = False
            # Atribuimos la habitación
            sql_atribute_room = f"UPDATE bookings SET validated = '1' WHERE user_id = '{user[0]}' and hotel_id = '{booking[0]}';"
            sql_request(sql_atribute_room)
            sql_reduce_room = f"UPDATE hotels SET rooms = '{available_room - 1}' WHERE id = '{booking[0]}';"
            sql_request(sql_reduce_room)
            sql_message_user = f"UPDATE users SET message = 'Tu reserva en el hotel {booking[2]} ha sido validada.' WHERE id = '{user[0]}';"
            sql_request(sql_message_user)
            break
        else:
            pass
    if check_message:
        sql_message_user = f"UPDATE users SET message = 'NO has conseguido reserva en esta convocatoria' WHERE id = '{user[0]}';"
        sql_request(sql_message_user)
  
end = time.time()
print(f"Time elapsed for ranking generator: {round((end - start), 2)} s")