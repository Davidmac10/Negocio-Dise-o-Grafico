import sqlite3
import random

conexion = sqlite3.connect('db.sqlite')
cursor = conexion.cursor()

prefijo = "+57"
codigo_tel = ['300','301','302','303','304','305','306','307','308','309','310','311','312','313','314','315','316','317','318','319','320','321','322','323','324','325','326','327','328','329']

complemento = random.randint(1000000, 9999999)

numero_celular = prefijo + random.choice(codigo_tel) + str(complemento)

print(numero_celular)

conexion.commit()
conexion.close()