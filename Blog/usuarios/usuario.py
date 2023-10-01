import usuarios.Conexion as conexion
import datetime
import hashlib

connect= conexion.conectar()
database = connect[0]
cursor = connect[1]


class Usuario:

    def __init__(self,nombre,apellido,email,password):
        self.nombre =nombre
        self.apellido=apellido
        self.email=email
        self.password=password

    def registrar(self):
        fecha=datetime.datetime.now()
        #Cifrar contraseña
        crifrado=hashlib.sha256()
        crifrado.update(self.password.encode('utf8'))

        #Insetar los valores ala base de datos

        sql="INSERT INTO usuarios VALUES(null,%s,%s,%s,%s,%s)"
        usuario=(self.nombre,self.apellido,self.email,crifrado.hexdigest(),fecha)

        try:

            cursor.execute(sql,usuario)
            database.commit()
            #Una lista con la cantidad de registros modificados y el objeto
            #Con los datos que tenga
            result=[cursor.rowcount,self]

        except:
            result=[0,self]

        return result





    def identificar(self):
       #Consulta para comprobar si existe el usuario
       sql="SELECT * FROM usuarios WHERE email = %s AND password = %s"

       #Cifrar contraseña
       crifrado=hashlib.sha256()
       crifrado.update(self.password.encode('utf8'))  
       #Datos para la consulta 
       usuario=(self.email,crifrado.hexdigest())
       
       #Consulta
       cursor.execute(sql,usuario)
       result=cursor.fetchone()

       return result
       
       
