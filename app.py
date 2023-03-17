import sqlite3
import random
import pywhatkit

conexion = sqlite3.connect('db.sqlite')
cursor = conexion.cursor()

prefijo = "+57"
    
codigo_tel = ['300','301','302','303','304','305','306','307','308','309','310','311','312','313','314','315','316','317','318','319','320','321','322','323','324','325','326','327','328','329']

complemento = random.randint(1000000, 9999999)

numero_celular = prefijo + random.choice(codigo_tel) + str(complemento)

print(numero_celular)

estado = "Usado_bloqueado"
    
cursor.execute("SELECT * FROM telefono WHERE telefono = ?", (numero_celular, ))
telefono_search = cursor.fetchone()

if telefono_search is None:
        
    cursor.execute("INSERT INTO telefono (telefono, estado) VALUES (?, ?)", (numero_celular, estado))

    mensaje = "Hola, mi nombre es David Stiven Mendieta Barajas, soy diseñador grafico, te cuento mi emprendimiento, me dedico a hacer logos para cualquier tipo de negocio, fotomontajes, ilustraciones computarizadas, edicion de video profesional y animaciones 2D, si te interesa adquirir cualquiera de mis servicios, contactame o escribeme al +57 3232012435 para mas informacion" #input("Ingresa tu mensaje a enviar: ")
    hora = int(input("Ingresa la hora: "))
    minuto = int(input("Ingresa el minuto: "))
        
    pywhatkit.sendwhatmsg(numero_celular, mensaje, hora, minuto)
    
else:
    print("El numero telefonico ya esta en la base de datos, intentar nuevamente")      
    
conexion.commit()
conexion.close()