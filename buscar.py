import mysql.connector
estado = 1
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="python-user")
cursor1=conexion1.cursor()
legajo= int(input("Ingrese su nro: "))
cursor1.execute("SELECT name FROM users WHERE id = %s;", (legajo,))

#for tabla in cursor1:
print(table)
#conexion1.close() 
