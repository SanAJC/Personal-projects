import pygame
import io
from pygame.locals import MOUSEBUTTONDOWN , MOUSEMOTION, MOUSEBUTTONUP


# inicializar a pygame
pygame.init()

# crear la pantalla
pantalla = pygame.display.set_mode((1160, 640))

# Titulo e Icono
pygame.display.set_caption("Juego Torres de Hanoi")  # titulo
icono = pygame.image.load("img/logo.jpg")  # icono
pygame.display.set_icon(icono)  # icono
Fondo = pygame.image.load("img/fondo.png") # fondo


# funcion fuente_bytes
def fuente_bytes(fuente):
    with open(fuente, "rb") as f:
        ttf_bytes = f.read()
    return io.BytesIO(ttf_bytes)


#-------------------------------------------------------------------#
#Cargar Torres

img_torre=[]


# Carga la imagen bases
img_torre = pygame.image.load("img/torre.png")

#Redimensionar
imagen_redimensionada = pygame.transform.scale(img_torre, (300, 400))

# Posiciones para las tres imágenes
posiciones = [(50, 200), (400, 200), (750, 200)]

#-------------------------------------------------------------------#
# Crear una fuente para el texto
fuente_como_bites = fuente_bytes('SuperMario256.ttf')

fuente= pygame.font.Font(fuente_como_bites, 30)

# Texto "Elija su dificultad"
texto_dificultad = fuente.render("Elija su dificultad", True, (255, 255, 255))

#-------------------------------------------------------------------#

# Movimientos
m=0
texto_movimientos = fuente.render(f"Movimientos : {m}", True, (255, 255, 255))


#-------------------------------------------------------------------#
# Opciones de dificultad
opciones = ["Facil", "Medio", "Dificil"]
opcion_seleccionada=0

#Variables de los discos
img_discos=[]
discos = []  # Lista de discos como objetos con posición y tamaño
activar_disco = None

# Función para cargar los discos
def cargar_discos(num_discos):

    if opcion_seleccionada==0:
        img_discos.clear()  # Limpiar la lista actual de discos
        discos.clear()  # Limpiar la lista de discos
        for i in range(1, num_discos + 1):
            disco_img = pygame.image.load(f"img/disco{i}.png")
            disco_rect = disco_img.get_rect()
            disco_rect.x = 107 -i *10 # Posición inicial en X
            disco_rect.y = 377 + i * 55  # Posición inicial en Y (ajusta según el tamaño de los discos)
            img_discos.append(disco_img)
            discos.append(disco_rect)
    elif opcion_seleccionada==1:
        img_discos.clear()  # Limpiar la lista actual de discos
        discos.clear()  # Limpiar la lista de discos
        for i in range(1, num_discos + 1):
            disco_img = pygame.image.load(f"img/disco{i}.png")
            disco_rect = disco_img.get_rect()
            disco_rect.x = 107 -i *15 # Posición inicial en X
            disco_rect.y = 268 + i * 55  # Posición inicial en Y (ajusta según el tamaño de los discos)
            img_discos.append(disco_img)
            discos.append(disco_rect)
    elif opcion_seleccionada==2:
        img_discos.clear()  # Limpiar la lista actual de discos
        discos.clear()  # Limpiar la lista de discos
        for i in range(1, num_discos + 1):
            disco_img = pygame.image.load(f"img/disco{i}.png")
            disco_rect = disco_img.get_rect()
            disco_rect.x = 107 -i *12 # Posición inicial en X
            disco_rect.y = 213 + i * 55  # Posición inicial en Y (ajusta según el tamaño de los discos)
            img_discos.append(disco_img)
            discos.append(disco_rect)


# Cargar los discos iniciales (opción "Facil")
cargar_discos(2)

#-------------------------------------------------------------------#

#Movimientos_Hanoi
n=0
texto_movimientos_hanoi=fuente.render(f"Movimientos Minimos: {2**n-1}", True, (255, 255, 255))

#-------------------------------------------------------------------#

#Hanoi

# Diccionario de las torres
torres = {0: (50, 200), 1: (400, 200), 2: (750, 200)}

# Lista para rastrear el estado de las torres (los discos que contienen)
estado_torres = [[] for _ in range(3)]  # 3 torres iniciales, todas vacías


def disco_valido(disco, torre):
    # Verifica si el disco es el disco superior de su torre de origen
    for t, discos_en_torre in enumerate(estado_torres):
        if disco in discos_en_torre and discos_en_torre[-1] != disco:
            return False

    # Verifica si la torre de destino está vacía o si su disco superior es más grande que el disco que se está moviendo
    if estado_torres[torre] and estado_torres[torre][-1] < disco:
        return False

    return True


# Variable para el disco activo
disco_activo = None

# Variable para almacenar la posición inicial del disco durante el arrastre
posicion_inicial_disco = None

#-------------------------------------------------------------------#

# Función para mostrar un mensaje
def mostrar_mensaje(texto):
    mensaje = fuente.render(texto, True, (255, 0, 0))
    pantalla.blit(mensaje, (480, 10))
    pygame.display.update()

# Función para verificar si se ha ganado el juego
def verificar_victoria():
    if len(estado_torres[2]) == len(discos):
        mostrar_mensaje("¡Ganaste!")
        return True

# Función para mostrar un mensaje
def mostrar_mensaje_reinicio(texto):
    mensaje = fuente.render(texto, True, (255, 0, 0))
    pantalla.blit(mensaje, (380, 50))
    pygame.display.update()


def comenzar_juego_de_nuevo():
    global m , estado_torres, discos
    m = 0
    cargar_discos(n)
    # Restablece los estados de las torres
    estado_torres = [[] for _ in range(3)]  # 3 torres iniciales, todas vacías
    
    
    

#-------------------------------------------------------------------#
#Ejecucion 
se_ejecuta = True
opcion_reinicio = 0

while se_ejecuta:

    pantalla.blit(Fondo, (-370,-100))
    
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            se_ejecuta = False
        elif evento.type == MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            if opcion_seleccionada == 0 or opcion_seleccionada == 1 or opcion_seleccionada == 2:
                for i, disco_rect in enumerate(discos):
                    if disco_rect.collidepoint(x, y):
                        disco_activo = i
                        posicion_inicial_disco = disco_rect.topleft

            if x >= 380 and x<= 660 and y >=50 and y <= 70 :
                opcion_reinicio = 1
                

            if 10 <= x <= 200:
                if 60 <= y <= 90:
                    # Opción "Facil" seleccionada
                    opcion_seleccionada=0
                    cargar_discos(2)  
                    n=2
                    m=0 
                    # Actualiza el texto de movimientos
                    texto_movimientos = fuente.render(f"Movimientos : {m}", True, (255, 255, 255))
                    
                elif 90 <= y <= 120:
                    # Opción "Medio" seleccionada
                    opcion_seleccionada=1
                    cargar_discos(4)
                    n=4
                    m=0
                    # Actualiza el texto de movimientos
                    texto_movimientos = fuente.render(f"Movimientos : {m}", True, (255, 255, 255))
                    
                elif 120 <= y <= 150:
                    # Opción "Dificil" seleccionada
                    opcion_seleccionada = 2
                    cargar_discos(5)
                    n=5
                    m=0
                    # Actualiza el texto de movimientos
                    texto_movimientos = fuente.render(f"Movimientos : {m}", True, (255, 255, 255))
        elif evento.type == MOUSEMOTION:
            if disco_activo is not None:
                x, y = pygame.mouse.get_pos()
                # Actualiza la posición del disco con la posición del mouse
                discos[disco_activo].topleft = (x, y)
                
        elif evento.type == MOUSEBUTTONUP:
            if disco_activo is not None:
                x, y = pygame.mouse.get_pos()
                disco_rect = discos[disco_activo]
                # Verifica si el disco se soltó en una torre válida
                for torre, (tx, ty) in torres.items():
                    if tx <= x <= tx + imagen_redimensionada.get_width() and ty <= y <= ty + imagen_redimensionada.get_height():
                        if disco_valido(disco_activo, torre):
                            for t, discos_en_torre in enumerate(estado_torres):
                                if disco_activo in discos_en_torre:
                                    discos_en_torre.remove(disco_activo)
                            # Mueve el disco a la torre válida
                            estado_torres[torre].append(disco_activo)
                            # Calcula la nueva posición y del disco
                            y_nueva = ty -55 + imagen_redimensionada.get_height() - (len(estado_torres[torre]) *55) # 55 es la altura de cada disco
                            # Actualiza la posición del disco
                            discos[disco_activo].topleft = (tx, y_nueva)
                            # Calcula la nueva posición x del disco
                            x_nueva = tx + (imagen_redimensionada.get_width() - disco_rect.width) / 2
                            # Actualiza la posición del disco
                            discos[disco_activo].topleft = (x_nueva, y_nueva)
                            
                        else:
                            # Devuelve el disco a su posición inicial
                            disco_rect.topleft = posicion_inicial_disco
                disco_activo = None
                m+=1
                # Actualiza el texto de movimientos
                texto_movimientos = fuente.render(f"Movimientos : {m}", True, (255, 255, 255))
                

     # Dibuja la imagen en las tres posiciones
    for pos in posiciones:
        pantalla.blit(imagen_redimensionada, pos)

    # Dibujar el texto "Elija su dificultad" en la parte superior izquierda
    pantalla.blit(texto_dificultad, (10, 10))

    # Dibujar las opciones de dificultad
    for i, opcion in enumerate(opciones):
        color = (255, 255, 255) if i == opcion_seleccionada else (200, 200, 200)
        texto_opcion = fuente.render(opcion, True, color)
        pantalla.blit(texto_opcion, (10, 60 + i * 30))

    #Dibujar movimientos
    pantalla.blit(texto_movimientos,(840,10))
    
    #Dibujar los movimineto recomendados
    pantalla.blit(texto_movimientos_hanoi,(682,40))
    # Actualizar el texto de movimientos Hanoi
    texto_movimientos_hanoi = fuente.render(f"Movimientos Minimos: {2**n-1}", True, (255, 255, 255))

    #Dibujar discos
    for i in range(len(discos)):
        pantalla.blit(img_discos[i], discos[i])

    # Verifica si se ha ganado el juego
    if verificar_victoria() == True:
        mostrar_mensaje_reinicio("Volver a jugar")
        if opcion_reinicio == 1:
            comenzar_juego_de_nuevo()
            opcion_reinicio = 0  # Restablece la variable de reinicio
        

    pygame.display.update()

