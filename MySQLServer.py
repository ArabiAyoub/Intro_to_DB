import mysql.connector
from mysql.connector import Error

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database 'alx_book_store' created successfully!")
    except Error as err:
        print("Error: {}".format(err))
    finally:
        cursor.close()

def main():
    # Connection parameters - adjust as necessary
    config = {
        'host': 'localhost',
        'user': 'root',
        'password': 'your_password'
    }
    
    try:
        # Connect to the MySQL server
        conn = mysql.connector.connect(**config)
        if conn.is_connected():
            print('Connected to MySQL server')
            # Create database if it does not exist
            create_database(conn, "CREATE DATABASE IF NOT EXISTS alx_book_store")
    except Error as e:
        print("Error: {}".format(e))
    finally:
        if conn.is_connected():
            conn.close()
            print('Database connection closed.')

if __name__ == "__main__":
    main()