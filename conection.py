import mysql.connector
variableID = 0

conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="python-user")
cursor1=conexion1.cursor()
variableID = int(input("Ingrese su legajo: "))
cursor1.execute(cursor1,"select * from users"+"WHERE ID=" + variableID.get(),(consultaparametrizada))
for tabla in cursor1:
    print(tabla)
conexion1.close()   

#UPDATE users SET estado=1 where

#if legajo == este:
print (tabla)