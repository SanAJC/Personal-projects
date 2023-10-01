import usuario 

# Función para mostrar el menú de opciones
def mostrar_menu():
    print("Bienvenido    |     Banco ")
    print("---------------------------")
    print("1. Registrar nuevo usuario")
    print("---------------------------")
    print("2. Autenticar usuario")
    print("---------------------------")
    print("0. Salir")
    print("---------------------------")
    opcion = int(input("Seleccione una opción: "))
    return opcion

# Ciclo principal del programa
while True:
    opcion = mostrar_menu()

    if opcion == 1:
        usuario.registrar_usuario()
    elif opcion == 2:
        usuario_actual = usuario.autenticar_usuario()
        if usuario_actual:
            def mostrar_menu2():
                print("Bienvenido, " + usuario_actual[1])
                print("---------------------------")
                print("1. Retirar dinero")
                print("---------------------------")
                print("2. Depositar dinero")
                print("---------------------------")
                print("3. Consultar saldo")
                print("---------------------------")
                print("4.Tranferir fondo ")
                print("---------------------------")
                print("5.Salir")
                print("---------------------------")
                op = int(input("Seleccione una opción: "))
                return op
            while True:
                op = mostrar_menu2()
                if op == 1:
                    usuario.retirar_dinero(usuario_actual)
                elif op == 2:
                    usuario.depositar_dinero(usuario_actual)
                elif op == 3:
                    usuario.consultar_saldo(usuario_actual)
                elif op == 4:
                    usuario.transferir_saldo(usuario_actual)
                elif op == 5:
                    print("Hasta la proxima")
                    break
                else:
                    print("Opción no válida.")
        else:
            print("Email o contraseña incorrectos.")
    elif opcion == 0:
        print("Hasta la proxima")
        break
    else:
        print("Opción no válida.")


        