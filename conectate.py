import mysql.connector

try:
    connection = mysql.connector.connect(host='localhost', database='python-user', user='root', password='')
    cursor = connection.cursor()
    input_data = int(input("Ingrese su legajo: "))
    sql  = "Update users set estado = %s where id = %s "
    val = ("2", input_data)
    cursor.execute(sql, val)
    #cursor.execute(input_data)
    connection.commit()
    print("Record Updated successfully ")
except mysql.connector.Error as error:
    print("Failed to update record to database: {}".format(error))
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("MySQL connection is closed")