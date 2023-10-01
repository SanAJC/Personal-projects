import mysql.connector

# Conexión a la base de datos
def conectar():
    database = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="TPS",
        port=3306
)
#Realizar consultas en la bd
    cursor = database.cursor()
    return[database,cursor]
