import mysql.connector
try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="karthick")
    mycursor=dbcon.cursor()
    sql_sql='''
           create table employee(
           eid int,
           ename varchar(32),
           esal float,
           eloc varchar(32)
           )

    '''
    mycursor.execute(sql_sql)
    dbcon.commit()
    print("Table created Successfully")


except mysql.connector.DatabaseError as err:
    if err:
        print(err)

finally:
    mycursor.close()
    dbcon.close()