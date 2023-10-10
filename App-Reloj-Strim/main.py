from tkinter import *
from tkinter import ttk
import time
from PIL import Image,ImageTk

ventana_main=Tk()
ventana_main.title("App | Reloj")
ventana_main.iconbitmap('img/reloj.ico')
ventana_main.resizable(0,0)
ventana_main.geometry("550x500")
ventana_main.config(bg="black")

estilos=ttk.Style()
estilos.theme_use('clam')


reloj_label=Label(ventana_main)
hora_local_label=Label(ventana_main,text="HORA LOCAL")

image=Image.open('img\\mundo.png')
photo=ImageTk.PhotoImage(image)
label_imagen=Label(ventana_main,image=photo)

image_1=Image.open('img\\colombia.png')
photo_1=ImageTk.PhotoImage(image_1)
label_imagen_1=Label(ventana_main,image=photo_1)

def reloj():

    hora_local_label.config(font=('Digital-7 Mono',40),fg="#0004FF",bd=40,bg="black")
    hora_local_label.grid(row=0,column=0,padx=100,pady=10,columnspan=2)

    label_imagen.grid(row=1,column=0,padx=10,pady=10,sticky="e")
    label_imagen.config(bg="black")

    label_imagen_1.grid(row=1,column=1,padx=10,pady=10,sticky="w")
    label_imagen_1.config(bg="black")


    reloj_label.config(font=('Digital-7 Mono',48),fg="#0004FF",bd=40,bg="black")
    reloj_label.grid(row=2,column=0,padx=100,pady=10,columnspan=2)
    tiempo_reloj=time.strftime('%H:%M:%S')
    reloj_label.config(text=tiempo_reloj)
    reloj_label.after(200,reloj)



    #Ocultamos la otra pantalla
    cronometro_label.grid_remove()

cronometro_label=Label(ventana_main)
cronometro=Label(ventana_main,text="CRONOMETRO")
def cronometro():
    
    
    pass




menu=Menu(ventana_main)
ventana_main.config(menu=menu)

menu.add_command(label="RELOJ",command=reloj())
menu.add_command(label="CRONOMETRO")

ventana_main.mainloop()