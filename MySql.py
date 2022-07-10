import mysql.connector as connection

mydb= connection.connect(host="localhost",user="devuser",passwd="Logitech1234#" )
cursor= mydb.cursor()
try:
    showdb_query= "SHOW DATABASES"
    cursor.execute(showdb_query)
    a= cursor.fetchall()
    print(a)

    usedb_query= "USE APIDATABASE"
    cursor.execute(usedb_query)
    print(cursor.fetchall())

    showtable_query= "SHOW TABLES"
    cursor.execute(showtable_query)
    print(cursor.fetchall())

    selecttable_query= "SELECT * FROM EMPLOYEE"
    cursor.execute(selecttable_query)
    print(cursor.fetchall())

# Commenting as it is already created
    create_table_query = "CREATE TABLE APIDATABASE.EMPLOYEE1(Emp_ID int(10),Emp_Name varchar(80), Emp_MailID varchar(50), Emp_Sal int(6))"
    cursor.execute(create_table_query)
    print(cursor.fetchall())

    showtable_query= "SHOW TABLES"
    cursor.execute(showtable_query)
    print(cursor.fetchall())



    inserttable_query = "INSERT INTO APIDATABASE.EMPLOYEE1 VALUES(10,'Ravi Ranjan','r@gmail.com',40000)"
    cursor.execute(inserttable_query)
    print(cursor.fetchall())
    mydb.commit()

    selecttable_query= "SELECT * FROM APIDATABASE.EMPLOYEE1"
    cursor.execute(selecttable_query)
    for i in cursor.fetchall():
        print(i)

except Exception as e:
    print(e)

finally:
    mydb.close()