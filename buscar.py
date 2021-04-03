import mysql.connector
estado = 1
conexion1=mysql.connector.connect(host="localhost", user="root", passwd="", database="python-user")
cursor1=conexion1.cursor()
legajo= int(input("Ingrese su legajo: "))
#cursor1.execute("SELECT name FROM users WHERE id = %s;", (legajo,))
cursor1.execute("""
    UPDATE users 
    SET estado = 1 
    WHERE id = 2;
""")
#for tabla in cursor1:
print(legajo)
#conexion1.close() 
