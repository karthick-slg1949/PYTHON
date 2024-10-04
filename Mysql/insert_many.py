import mysql.connector

try:
    dbcon=mysql.connector.connect(
        host="localhost",user="root",password="root",database="karthick")
    mycursor=dbcon.cursor()
    sql_st='''
           insert into employee(eid,ename,esal,eloc) values(%s,%s,%s,%s)
           '''
    data=[(102,"Navin",88000,"Silanthagudi"),
          (103,"Dinesh",70000,"Silanthagudi"),
          (104,"Vikram",100000,"Silanthagudi"),
          (105,"Rahul",40000,"Silanthagudi")
          ]
    mycursor.executemany(sql_st,data)
    dbcon.commit()
    print("Data Inserted successfully")
except mysql.connector.DatabaseError as err:
    if err:
        print(err)
finally:
    mycursor.close()
    dbcon.close()
