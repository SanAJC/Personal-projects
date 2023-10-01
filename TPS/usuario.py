
import conexion 
import hashlib
import datetime

fecha=datetime.datetime.now()

# 2. Establecer la conexión
conect=conexion.conectar()
database=conect[0]
# 3. Crear un cursor a partir de la conexión
cursor = conect[1] 






# Funcion para registrar un nuevo usuario
def registrar_usuario():
    print("Registro de nuevo usuario")
    nombre = input("Ingrese su nombre: ")
    apellido = input("Ingrese su apellido: ")
    email = (input("Ingrese su email: "))
    password = input("Ingrese su contraseña: ")
    saldo = ""
    cifrado = hashlib.sha256()
    cifrado.update(password.encode('utf8'))
   
    # Se verifica si ya existe un usuario con el mismo email
    consulta = "SELECT * FROM usuarios WHERE email = %s "
   
    cursor.execute(consulta, (email,))
    resultado = cursor.fetchone()
    

    if resultado:
        print("El email ingresado ya existe.")
    else:
        # Se registra el nuevo usuario
        consulta = "INSERT INTO usuarios (nombre, apellido, email, password, fecha, saldo) VALUES (%s, %s, %s, %s, %s, %s)"
        valores = (nombre, apellido, email, cifrado.hexdigest(), fecha, saldo)
        cursor.execute(consulta, valores)
        
        database.commit()
        print(f"Usuario registrado exitosamente. El {fecha}")
# Función para autenticar un usuario
def autenticar_usuario():
    print("Autenticación de usuario")
    email = input("Ingrese su email: ")
    password = input("Ingrese su contraseña: ")
    cifrado = hashlib.sha256()
    cifrado.update(password.encode('utf8'))
    
    # Se verifica si existe un usuario con el email y contraseña ingresados
    consulta = "SELECT * FROM usuarios WHERE email = %s AND password = %s"
    usuario = (email ,cifrado.hexdigest())

    cursor.execute(consulta, usuario)
    resultado = cursor.fetchone()
    if resultado:
        return resultado
    else:
        print("Email o contraseña incorrectos.")
        return None

# Función para retirar dinero de una cuenta
def retirar_dinero(usuarios):
    print("Retiro de dinero")
    monto = float(input("Ingrese el monto a retirar: "))
    if monto > usuarios[5]:
        print("Saldo insuficiente.")
    else:
        nuevo_saldo = usuarios[5] - monto
        
        # Se actualiza el saldo del usuario
        consulta = "UPDATE usuarios SET saldo = %s WHERE id = %s"
        valores = (nuevo_saldo, usuarios[0])
        cursor.execute(consulta, valores)
        database.commit()
        print(f"Retiro exitoso. Nuevo saldo: $ {nuevo_saldo} | {fecha}")

# Función para depositar dinero en una cuenta
def depositar_dinero(usuario):
    print("Depósito de dinero")
    monto = float(input("Ingrese el monto a depositar: "))
    
    nuevo_saldo = usuario[5]+ monto
    
    # Se actualiza el saldo del usuario
    consulta = "UPDATE usuarios SET saldo = %s WHERE id = %s"
    valores = (nuevo_saldo, usuario[0])
    cursor.execute(consulta, valores)
    database.commit()
    print(f"Depósito exitoso. Nuevo saldo: ${nuevo_saldo} | {fecha}")

# Función para consultar el saldo de una cuenta
def consultar_saldo(usuario):
    print("Consulta de saldo")
    print("Su saldo actual es de: $" + str(usuario[5]))


def transferir_saldo(usuario_origen):
    print("Transferencia de saldo")
    monto = float(input("Ingrese el monto a transferir: "))
    email=input("Ingresa el email del destinatario: ")
    # Verificar si el usuario origen tiene suficiente saldo
    if monto > usuario_origen[5]:
        print("Saldo insuficiente.")
    else:
        # Obtener el objeto usuario del destinatario
        consulta = "SELECT * FROM usuarios WHERE email = %s"
        cursor.execute(consulta, (email,))
        usuario_destino = cursor.fetchone()
        
        if usuario_destino:
            # Actualizar el saldo del usuario origen
            nuevo_saldo_origen = usuario_origen[5] - monto
            consulta = "UPDATE usuarios SET saldo = %s WHERE id = %s"
            valores = (nuevo_saldo_origen, usuario_origen[0])
            cursor.execute(consulta, valores)

            # Actualizar el saldo del usuario destino
            nuevo_saldo_destino = usuario_destino[5] + monto
            consulta = "UPDATE usuarios SET saldo = %s WHERE id = %s"
            valores = (nuevo_saldo_destino, usuario_destino[0])
            cursor.execute(consulta, valores)

            database.commit()
            print(f"Transferencia exitosa. Nuevo saldo usuario origen: ${nuevo_saldo_origen} | Nuevo saldo usuario destino: ${nuevo_saldo_destino} | {fecha}")
        else:
            print("El email del destinatario no está registrado.")



