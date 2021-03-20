import mysql.connector

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="oimbaite_ferreteria_milabi")
cursor1=conexion1.cursor()
legajo= int(input("Ingrese su legajo: "))
cursor1.execute("SELECT usuario FROM users WHERE id = %s;", (legajo,))
for tabla in cursor1:
    print(tabla)
conexion1.close() 
