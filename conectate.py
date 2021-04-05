import mysql.connector
cerradura = 0

while True:
    try:
        connection = mysql.connector.connect(host='localhosst', database='python-user', user='root', password='')
        cursor = connection.cursor()
        if cerradura == 0:
            legajo = int(input("Ingrese su legajo: "))
            sql  = "Update users set estado = %s where estado = 1 and id = %s"
            val = ("0", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print("OCUPADO")
            cerradura = 1
        else:
            legajo = int(input("Ingrese su legajo: "))
            sql  = "Update users set estado = %s where estado = 0 and id = %s"
            val = ("1", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print("LIBRE")
            cerradura = 0
    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")