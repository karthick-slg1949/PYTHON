import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="karthick")
    mycursor=dbcon.cursor()

    mycursor.execute("select * from employee")
    empdata=mycursor.fetchall()

    for emp in empdata:
        print(emp)

except mysql.connector.DatabaseError as err:
    if err:
        print("Unable to connect the data")

finally:
    dbcon.close()