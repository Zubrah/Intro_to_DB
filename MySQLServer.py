import mysql.connector

# Connect to MySQL server
try:
    connection = mysql.connector.connect(
        host="localhost",
        user="your_username",
        password="your_password"
    )

    # Create cursor object
    cursor = connection.cursor()

    # Create the database if it doesn't exist
    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    # Commit changes
    connection.commit()

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as error:
    print("Error while connecting to MySQL", error)

finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
