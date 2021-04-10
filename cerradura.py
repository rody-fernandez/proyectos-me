import mysql.connector
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(7, GPIO.OUT)  #Rojo 1     - Lila 
GPIO.setup(12, GPIO.OUT) #Rojo 2     - Azul
GPIO.setup(11, GPIO.OUT) #Verde 1    - Verde
GPIO.setup(13, GPIO.OUT) #Verde 2    - Amarillo
GPIO.setup(16, GPIO.OUT) #Amarillo 1 - Naranja
GPIO.setup(15, GPIO.OUT) #Amarillo 2 - Rojo

GPIO.setup(18, GPIO.OUT) #Motor 1    - Marron
GPIO.setup(22, GPIO.OUT) #Motor 2    - Blanco

GPIO.output(7, False) #Rojo 1 - Apagado
GPIO.output(12, False) #Rojo 2 - Apagado
GPIO.output(16, False) #Amarillo 1 - Apagado
GPIO.output(15, False) #Amarillo 2 - Apagado
GPIO.output(11, True) #Verde 1 - Encendido
GPIO.output(13, True) #Verde 2 - Encendido

GPIO.output(18, True) #Motor 1 - Apagado
GPIO.output(22, True) #Motor 2 - Apagado

cerradura = 0
estado = 0

while True:
    try:
        connection = mysql.connector.connect(host='localhost', database='python_user', user='rody', password='123456')
        cursor = connection.cursor()
        legajo = int(input("Ingrese su legajo: "))
        if cerradura == 0 and estado == 0:
            sql  = "Update users set estado = %s where estado = 0 and id = %s"
            val = ("1", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print(f"Bienvenido {legajo}")
            GPIO.output(7, True) #Rojo 1 - Encendido
            GPIO.output(12, True) #Rojo 2 - Encendido
            #GPIO.output(18, True) #Motor 1 - Encendido
            time.sleep(1)
            GPIO.output(11, False) #Verde 1 - Apagado
            GPIO.output(13, False) #Verde 2 - Apagado
            cerradura = 1
            estado = int(legajo)
        elif cerradura == 1 and estado == legajo:
            sql  = "Update users set estado = %s where estado = 1 and id = %s"
            val = ("0", legajo)
            cursor.execute(sql, val)
            connection.commit()
            print("Libre")
            GPIO.output(11, True) #Verde 1 - Encendido
            GPIO.output(13, True) #Verde 2 - Encendido
            #GPIO.output(22, True) #Motor 2 - Encendido
            time.sleep(1)
            GPIO.output(7, False) #Rojo 1 - Apagado
            GPIO.output(12, False) #Rojo 2 - Apagado
            cerradura = 1
            cerradura = 0
            estado = 0
        else:
            if cerradura == 1 and estado != 0:
                GPIO.output(15, True)
                GPIO.output(16, True)
                time.sleep(1)
                GPIO.output(15, False)
                GPIO.output(16, False)
                time.sleep(1)
                GPIO.output(15, True)
                GPIO.output(16, True)
                time.sleep(1)
                GPIO.output(15, False)
                GPIO.output(16, False)
                time.sleep(1)
                print (f"Perdon! Esta ocupado por {estado}")
    except mysql.connector.Error as error:
        print("Failed to update record to database: {}".format(error))
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()   
    
