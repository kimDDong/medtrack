import mysql.connector

db_config = {
    'user': 'root',
    'password': 'root',
    'host': 'localhost',
    'database': 'medical_info'
}

try:
    connection = mysql.connector.connect(**db_config)
    if connection.is_connected():
        print("Successfully connected to the database")
        connection.close()
except mysql.connector.Error as err:
    print(f'Error: {err}')
