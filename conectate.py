import mysql.connector
cerradura = 0
estado = 0

while True:
    try:
        connection = mysql.connector.connect(host='localhost', database='python-user', user='root', password='')
        cursor = connection.cursor()
        legajo = int(input("Ingrese su legajo: "))
        if cerradura == 0 and estado == 0:
            sql  = "Update users set estado = %s where estado = 0 and id = %s"
            val = ("1", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print(f"Bienvenido {legajo}")
            cerradura = 1
            estado = int(legajo)
        elif  cerradura == 1 and estado == legajo:
            sql  = "Update users set estado = %s where estado = 1 and id = %s"
            val = ("0", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print(f"Hasta Luego! {legajo}")
            cerradura = 0
            estado = 0
        else:
            if cerradura == 1 and estado != 0:
                print("Perdon! Esta ocupado")
                  
    except mysql.connector.Error as error:
            print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")