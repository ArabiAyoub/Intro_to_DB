import mysql.connector
from mysql.connector import Error

def create_database(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        print("Database created successfully!")
    except mysql.connector.Error as err:  # Specific exception
        print(f"Error: {err}")
    finally:
        cursor.close()

def main():
    conn = None
    try:
        conn = mysql.connector.connect(
            host='localhost',
            user='root',
            password='your_password'
        )

        if conn.is_connected():
            print('Connected to MySQL server')
            create_database(conn, "CREATE DATABASE IF NOT EXISTS alx_book_store")
        else:
            print('Failed to connect')
    except mysql.connector.Error as e:  # Specific exception
        print(f"Error: {e}")
    finally:
        if conn is not None and conn.is_connected():
            conn.close()
            print('Database connection closed.')

if __name__ == "__main__":
    main()