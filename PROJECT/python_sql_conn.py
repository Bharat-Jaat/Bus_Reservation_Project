import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="12345", database="bharat")
    if conn.is_connected():
        cursor = conn.cursor()
        
        username = input("Enter your username- ")
        name = input("Enter your name- ")
        email = input("Enter your email- ")

        while not email.endswith("@gmail.com") :
            email = input("Enter your full email- ")
        password = input("Enter your password- ")

        
        query = "INSERT INTO users (username, name, email, password) VALUES (%s, %s, %s, %s)"
        values = (username, name, email, password)
        
        cursor.execute(query, values)
        conn.commit()
        
        print(f"User '{username}' has been successfully registered!")
        username = input("Enter username- ")
        name = input("Enter your name- ")
        email = input("Enter your email- ")

        
except Error as e:
    print("Error-", e)

finally:
    if conn.is_connected():
        conn.close()
