
import Notas.nota as modelo

class Acciones:

    def crear (self,usuario):
        print(f"\n OK {usuario[1]} Vamos a crear una nueva nota..")
        titulo=input("Introduce el titulo de tu nota ")
        descripcion=input("Empieza a llenar tu nota ")

        nota=modelo.nota(usuario[0],titulo,descripcion)
        guardar = nota.guardar()

        if guardar[0]>= 1:
            print(f"\n Perfecto se ha guardado la nota : {nota.titulo}")

        else:
            print("\n No se a podido guardar ..") 
    
    def mostar(self,usuario):

        print(f"\n Listo {usuario[1]}..Aqui tienes tus notas  ")

        nota=modelo.nota(usuario[0])

        notas=nota.listar()

        for nota in notas:
            print("\n*********************")
            print(nota[2])
            print(nota[3])
            print("*********************")

    def borrar(self,usuario):
        print(f"Listo {usuario[1]}  Vamos a borar notas")

        titulo=input("Introduce el titulo de la nota que deseas borrar : ")

        nota=modelo.nota(usuario[0],titulo)

        eliminar = nota.eliminar(usuario)

        if eliminar[0]>=1:
            print(f"Hemos borrado la nota : {nota.titulo}")
        else:
            print("No se pudo borrar la nota ")


        






