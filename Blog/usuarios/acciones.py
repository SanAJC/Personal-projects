
import usuarios.usuario as modelo
import  Notas.acciones 

class Acciones:

    def registro(self):
        print("\n OK!! Vamos a registrarte en el sistema...")
        nombre=input("Cual es tu nombre :")
        apellido = input("Cuales es tu apellido ")
        email = input("Introduce tu email ")
        password=input("Introduce tu contraseña ")
        
        usuario = modelo.Usuario(nombre,apellido,email,password)
        registro = usuario.registrar()

        #Abra registrado al usuario
        if registro[0] >= 1 :
            print(f"Perfecto {registro[1].nombre} te has resgistrado con el email {registro[1].email}")
        else:
            print("No te has registrado correctamente ..")

    def login(self):
        print("Vale!! Identificate en el sistema...")
       
        try:
            email = input("Introduce tu email ")
            password=input("Introduce tu contraseña ")
            

            usuario=modelo.Usuario('','',email,password)
            login=usuario.identificar()

            if email == login[3]:
                print(f"BIENVENIDO {login[1]}, te has registado en el sistema el {login[5]}")
                self.proximasAcciones(login)
        
        except Exception as e :
         print("Login incorerecto")

    def proximasAcciones(self,usuario):
        print("""
        Acciones disponibles :
        -Crear nota (crear)
        -Mostrar tus notas (mostrar)
        -Eliminar notas(eliminar)
        -Salir(salir)
        
        """)

        accion=input("Que quieres hacer : ")
        #Objeto de acciones
        hazEl=Notas.acciones.Acciones()

        if accion=="crear":
            print("Vamos a crear")
            hazEl.crear(usuario)
            self.proximasAcciones(usuario)
        
        elif accion =="mostrar":
            print("Vamos a mostrar ")
            hazEl.mostar(usuario)
            self.proximasAcciones(usuario)

        
        elif accion=="eliminar":
            print("Vas a eliminar")
            hazEl.borrar(usuario)
            self.proximasAcciones(usuario)

        
        elif accion=="salir":
            print("Hasta pronto")
            exit()
