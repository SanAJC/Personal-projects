"""

Proyecto-Python y Mysql:

-Abrir asistente
-Login o registro
-Si eligimos registro , creara un usuario en la base de datos
-Si eligimos login , identifica al usuario y nos preguntara
-Crear nota,mostrar notas , borrarlas.

""" 
from usuarios import acciones

print("""
ACCIONES DISPONIBLES:
 -registro
 -login
""") 
hazEl=acciones.Acciones()

accion = input("Que deseas realizar: ")

if accion=="registro":
    hazEl.registro()
    
elif accion =="login":
    hazEl.login()
    

