from tkinter import*
from tkinter import ttk
from tkinter.ttk import Separator
from tkinter import messagebox

ventana=Tk()

ventana.title("Conversor de Unidades")
ventana.geometry("600x400")
ventana.resizable(False,False)
ventana.iconbitmap('img\logo.ico')
ventana.config(bg="gray")


estilos=ttk.Style()
estilos.theme_use('clam')

# Lista de unidades de medida de tiempo con signos
unidades_tiempo = ["Unidades","Segundo (s)", "Minuto (min)", "Hora (h)", "Día (d)", "Semana (sem)", "Mes (meses)", "Año (años)"]

unidades_de_tiempo_en_segundos = ["",1, 60, 3600, 86400, 604800, 2419200, 29030400]


def convertir():
    try:
        op_1= menu1.get()
        op_2 =menu2.get()
        entrada=float(num_1.get())

        pos_op_1=unidades_tiempo.index(op_1)
        pos_op_2=unidades_tiempo.index(op_2)
        calculo=(unidades_de_tiempo_en_segundos[pos_op_1]/unidades_de_tiempo_en_segundos[pos_op_2]) * entrada

        resultado['text']=str(format(calculo))

    except ValueError:
        resultado['text'] = "Solo numeros rey"

def borrar():
    num_1.delete(0,END)
    resultado['text'] = ""



encabezado=Label(ventana,text="Convertidor de Unidades")
encabezado.config(fg="white",bg="black",font=("Comic Sans MS",20),padx=10,pady=10)
encabezado.grid(row=0,column=0,padx=120,pady=20)

marco=Frame(ventana,width=250,height=250)
marco.config(bg="black",relief=SOLID,
    padx=10,
    pady=10,
    borderwidth=2,)
marco.grid(row=1,column=0,padx=10,pady=10)

resultado=Label(marco,text="Salida")
resultado.config(fg="white",bg="gray",font=("Comic Sans MS",20),padx=10,pady=10)
resultado.grid(row=2,column=1,padx=10,pady=10)

num_1=Entry(marco,font=('Calibri,20'),justify=CENTER,bg="gray")
num_1.grid(row=2,column=0,padx=10,pady=20)
num_1.insert(END,1)

menu1=ttk.Combobox(marco,values=unidades_tiempo,justify='center',font=('Calibri,20'), state='readonly')
menu1.grid(row=3,column=0,padx=10,pady=20)
menu1.current(0)

menu2=ttk.Combobox(marco,values=unidades_tiempo,justify='center',font=('Calibri,20'), state='readonly')
menu2.grid(row=3,column=1,padx=10,pady=20)
menu2.current(1)

boton1=Button(marco,text="BORRAR",fg="white",bg="gray",font=("Comic Sans MS",20),command=borrar)
boton1.grid(row=4,column=0,padx=10,pady=10)

boton2=Button(marco,text="CONVERTIR",fg="white",bg="gray",font=("Comic Sans MS",20),command=convertir)
boton2.grid(row=4,column=1,padx=10,pady=10)

ventana.mainloop()