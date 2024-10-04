import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="karthick")
    mycursor=dbcon.cursor()
    sql_st='''
           insert into employee values(101,"Satheesh",90000,"Silanthagudi")
           '''
    mycursor.execute(sql_st)
    dbcon.commit()
    print("Data Inserted successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    mycursor.close()
    dbcon.close()
