from tkinter import*
from tkinter import ttk ,filedialog
from tkinter import messagebox
import conexion
import datetime
import hashlib
from PIL import Image,ImageTk
from pygame import mixer
import os

fecha=datetime.datetime.now()
# 2. Establecer la conexión
conect=conexion.conectar()
database=conect[0]
# 3. Crear un cursor a partir de la conexión
cursor = conect[1] 


ventana_main=Tk()
ventana_main.title("App | Music")
ventana_main.geometry("925x530")
ventana_main.iconbitmap("img\ico.ico")
ventana_main.config(bg="#5C5A5A")
ventana_main.resizable(0,0)


style = ttk.Style(ventana_main)
style.theme_use('clam') 


image=Image.open('img\\avatar.png')
photo=ImageTk.PhotoImage(image)
label_imagen=Label(ventana_main,image=photo)
label_imagen.config(bg="#5C5A5A")

label_imagen.grid(row=0,column=0,padx=10,pady=20)

marco_del_login=Frame(ventana_main,width=350,height=350,bg="#333333")
marco_del_login.grid(row=0,column=1,padx=20,pady=20)

login=Label(marco_del_login,text="INGRESAR",fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333")
login.grid(row=0,column=0,padx=10,pady=5,columnspan=2)

def borrar_marcador_de_posicion(event):
    # Función para borrar el marcador de posición cuando se hace clic en el Entry
    if user.get() == 'Nombre de Usuario':
        user.delete(0, "end")
    if password.get() == 'Contraseña':
        password.delete(0, "end")

user=Entry(marco_del_login,width=25,fg="#54FFE2",border=0,bg="#333333",font=("STF_OBLONGUS",20,"bold"))
user.grid(row=1,column=0,padx=10,pady=10)
user.insert(0,'Nombre de Usuario')
user.bind("<FocusIn>", borrar_marcador_de_posicion)

Frame(marco_del_login,width=295,height=2,bg="black").grid(row=2,column=0,padx=10,pady=0)

password=Entry(marco_del_login,width=25,fg="#54FFE2",border=0,bg="#333333",font=("STF_OBLONGUS",20,"bold"))
password.grid(row=3,column=0,padx=10,pady=10)
password.insert(0,'Contraseña')
password.bind("<FocusIn>", borrar_marcador_de_posicion)

Frame(marco_del_login,width=295,height=2,bg="black").grid(row=4,column=0,padx=10,pady=0)


class Usuario:
    def __init__(self):
        self.registrado = False

    def registrar(self):
        if not self.registrado:
            cifrado = hashlib.sha256()
            cifrado.update(password.get().encode('utf8'))
            # Se registra el nuevo usuario
            consulta = "INSERT INTO usuarios (usuario,password, fecha) VALUES (%s, %s, %s)"
            valores = (user.get(),cifrado.hexdigest(), fecha)
            cursor.execute(consulta, valores)
        
            database.commit()
            
            self.registrado = True
            messagebox.showinfo("Registro exitoso", "Usuario registrado correctamente.")

    def ingresar(self):
        # Se cifra la contraseña ingresada por el usuario para compararla con la de la base de datos
        cifrado = hashlib.sha256()
        cifrado.update(password.get().encode('utf8'))
        contraseña_cifrada = cifrado.hexdigest()
        #Se verifica si ya existe el usuario
        consulta="SELECT * FROM usuarios WHERE password = %s"
        cursor.execute(consulta,(contraseña_cifrada,))
        resultado=cursor.fetchone()
        self.registrado = resultado 
        


        if self.registrado is not None:
            
            # Realiza la consulta SQL para obtener el id del usuario
            consulta = "SELECT id FROM usuarios WHERE usuario = %s"
            cursor.execute(consulta, (user.get(),))

            # Obtiene el resultado de la consulta
            resultado_id = cursor.fetchone()
            resultado_id = resultado_id[0] 
                        
           # Destruir la ventana principal actual
            ventana_main.destroy()

            # Crear una nueva ventana principal limpia
            nueva_ventana_main = Tk()
            nueva_ventana_main.title("App | Music")
            nueva_ventana_main.geometry("925x630")
            nueva_ventana_main.iconbitmap("img\ico.ico")
            nueva_ventana_main.config(bg="#5C5A5A")
            nueva_ventana_main.resizable(0, 0)

            def open_folder():
                path=filedialog.askdirectory()
                if path:
                    os.chdir(path)
                    canciones=os.listdir(path)
                    for cancion in canciones:
                        if cancion.endswith(".mp3"):
                            play_list.insert(END,cancion)
                    
                    # Llamar a la función para guardar la carpeta en la base de datos
                    guardar_carpeta_en_bd(path, resultado_id)

            def guardar_carpeta_en_bd(carpeta, resultado_id):
                # Verificar si la carpeta ya está en la base de datos para evitar duplicados
                consulta = "SELECT * FROM listas_de_reproduccion WHERE nombre = %s AND usuario_id = %s"
                cursor.execute(consulta, (carpeta, resultado_id,))
                resultado = cursor.fetchone()
                
                if not resultado:
                    # Si no se encuentra, se agrega a la base de datos
                    consulta_insertar = "INSERT INTO listas_de_reproduccion (nombre, usuario_id) VALUES (%s, %s)"
                    valores_insertar = (carpeta, resultado_id)
                    cursor.execute(consulta_insertar, valores_insertar)
                    database.commit()
        
            def play ():
                music_name=play_list.get(ACTIVE)
                mixer.music.load(play_list.get(ACTIVE))
                mixer.music.play()
                musica_rep.config(text=music_name[0:-4])

            def playList():
                ventana_play_list=Toplevel(nueva_ventana_main)
                ventana_play_list.title("App | Music")
                ventana_play_list.geometry("525x430")
                ventana_play_list.iconbitmap("img\ico.ico")
                ventana_play_list.config(bg="#5C5A5A")
                ventana_play_list.resizable(0, 0)


                encabezado_1=Label(ventana_play_list,text=" Historial | Tus Carpetas de Musica",fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333")
                encabezado_1.grid(row=0,column=0,padx=10,pady=10,sticky='w')

                marco_playList=Frame(ventana_play_list,width=250,height=150,relief=SOLID,bg="#333333")
                marco_playList.grid(row=1, column=0,padx=10,pady=10 ,sticky='w')

                scroll=Scrollbar(marco_playList)
                play_list=Listbox(marco_playList,width=30,fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
            
                scroll.config(command=play_list.yview)
                scroll.grid(row=0,column=1,padx=5,pady=5,sticky='w')
                play_list.grid(row=0,column=0,padx=5,pady=5,sticky='w')

            
                 # Realiza la consulta SQL para obtener las carpetas del usuario actual
                consulta = "SELECT nombre FROM listas_de_reproduccion WHERE usuario_id = %s"
                cursor.execute(consulta, (resultado_id,))
                carpetas = cursor.fetchall()

                # Inserta las carpetas en la Listbox
                for carpeta in carpetas:
                    play_list.insert(END, carpeta[0])

                


           
            disco_boton = PhotoImage(file='img\\disco.png')
            Button(nueva_ventana_main, image=disco_boton, bg="#5C5A5A", bd=0,command=playList).grid(row=0, column=0, padx=10, pady=20)

            marco_del_login=Frame(nueva_ventana_main,width=350,height=350,bg="#333333")
            marco_del_login.grid(row=0,column=1,padx=20,pady=20)

            encabezado=Label(marco_del_login,text="LISTA DE REPRODUCCION MP3",fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333")
            encabezado.grid(row=0,column=1,padx=200,pady=20)
            
            mixer.init()

            # Crear un Frame para los botones
            botones_frame = Frame(nueva_ventana_main, bg="#5C5A5A")
            botones_frame.grid(row=3, column=0, rowspan=4, padx=5, pady=5, sticky='w')

            play_boton = PhotoImage(file='img\\play.png')
            play_boton = play_boton.subsample(6)
            Button(botones_frame, image=play_boton, bg="#5C5A5A", bd=0,command=play).grid(row=0, column=0, padx=5, pady=5, sticky='w')

            stop_boton = PhotoImage(file='img\\stop.png')
            stop_boton = stop_boton.subsample(6)
            Button(botones_frame, image=stop_boton, bg="#5C5A5A", bd=0,command=mixer.music.stop).grid(row=1, column=0, padx=5, pady=5, sticky='w')

            resume_boton = PhotoImage(file='img\\reanude.png')
            resume_boton = resume_boton.subsample(6)
            Button(botones_frame, image=resume_boton, bg="#5C5A5A", bd=0,command=mixer.music.unpause).grid(row=2, column=0, padx=5, pady=5, sticky='w')

            pause_boton = PhotoImage(file='img\\pause.png')
            pause_boton = pause_boton.subsample(6)
            Button(botones_frame, image=pause_boton, bg="#5C5A5A", bd=0,command=mixer.music.pause).grid(row=3, column=0, padx=5, pady=5, sticky='w')

            # musica
            musica=Frame(nueva_ventana_main, width=250, height=150, bg="#54FFE2",relief=RIDGE)
            musica.grid(row=3, column=1, padx=10, pady=10)

            #boton para agregar carpetas

            open_boton = PhotoImage(file='img\\folder.png')
            open_boton = open_boton.subsample(6)
            Button(musica, image=open_boton, bg="#54FFE2", bd=0,command=open_folder).grid(row=0, column=0, padx=25, pady=25, sticky='w')

            musica_rep=Label(musica,text="",fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333")
            musica_rep.grid(row=0,column=0,padx=25,pady=25, sticky='e')

            scroll=Scrollbar(musica)
            play_list=Listbox(musica,width=50,fg="#54FFE2",font=("STF_OBLONGUS",23,"bold"),bg="#333333",selectbackground="lightblue",cursor="hand2",bd=0,yscrollcommand=scroll.set)
            
            scroll.config(command=play_list.yview)
            scroll.grid(row=1,column=1,padx=5,pady=5,sticky='w')
            play_list.grid(row=1,column=0,padx=5,pady=5,sticky='w')


            






            




            nueva_ventana_main.mainloop()


        else:
            messagebox.showerror("Error", "Debes registrar un usuario primero.")

usuario = Usuario()



button_register=Button(marco_del_login,bg="black",border=1,text="REGISTRAR",fg="#54FFE2",font=("STF_OBLONGUS",15,"bold"),command=usuario.registrar)
button_register.grid(row=5,column=0,padx=5,pady=5,sticky="e")

button_login=Button(marco_del_login,text="INGRESAR",bg="black",border=1,fg="#54FFE2",font=("STF_OBLONGUS",15,"bold"),command=usuario.ingresar)
button_login.grid(row=5,column=0,padx=5,pady=15,sticky="w")



ventana_main.mainloop()


