# import mysql.connector
# from mysql.connector import Error

# conn = mysql.connector .connect (host="localhost", password="12345", user="root", database="bharat")

# if conn.is_connected():
#     cursor = conn.cursor()
#     print("Connected")

# try:
#     query = f"insert into try values (3, 'Mayank', 12);"

#     cursor.execute(query)
#     print("inserted")

#     conn.commit()

# except Error as e:
#     print(e)

# cursor.close()
# conn.close()
# print("DB closed")

import mysql.connector
from mysql.connector import Error

try:
    conn = mysql.connector.connect(host="localhost", user="root", password="12345", db="bharat")

    if conn.is_connected():
        cursor = conn.cursor()

    a = input("What do you want to do??? \n----x----x----x----x----x----x---- \nSelect '1' or '2' or '3' or '4' \n1)Make a table \n2)Insert into table \n3)Update in table \n4)Delete in table \n\nYour Choice-")

    while a not in "1234":
            a = input("Invalid operation selected, \nselect a valid one- ")

    if a == "1":
        tname = input("Enter your table name- ")
        Colnum= int(input("Enter the number of columns for your table- "))

        for i in (1,Colnum):
            colname = input(f"Enter your column {i}- ")
            while not colname:
                colname = input(f"You have to give your column a name, \nName for column {i}- ")

            dtype = int(input("Your data will be \n(1)int, \n(2)char ,\n(3)varchar \nYour choice- "))
            if dtype == 1:
                dtype = "int"
            elif dtype == 2:
                dtype = "char"
            elif dtype == 3:
                dtype = "varchat"
            while not dtype:
                dtype = input(f"You have to give your column a Datatype, \nDatatype for column {i}- ")

            limit = input(f"Limit for column {i}- ")
            while not limit:
                limit = input(f"You have to give your column a Limit, \nLimit for column {i}- ")

                if not dtype:
                    dtype = input(f"You have to give your column a data type, \nData type for column {i}- ")
                if not limit:
                    colname = input(f"You have to give your column a limit, \nLimit for column {i}- ")

            if i == 1:
                cursor.execute(f"create table {tname} ({colname} {dtype}({limit}))")
                print("executed")

            if i > 1:
                print("append karna hai")

            # cursor.execute("")
        print("Ok till now")

    # elif a == "2":

    #     print("Insert into table")

    # elif a == "3":

    #     print("Update in table")

    # elif a == "4":        

    #     print("Delete in table")

    # cursor.execute("update try set name={} where S_No={} ")
    # print("Executed")

    # conn.commit()


except Error as e:
    print(f"Erron: {e}")
