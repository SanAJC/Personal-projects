#Importamos Tkinter
from tkinter import *
from tkinter import ttk
from Operaciones import *
#Denifimos la ventana de tkinter
ventana_main= Tk()

ventana_main.title("Calculadora")
ventana_main.geometry("+500+80")
ventana_main.resizable(False,False)
ventana_main.iconbitmap('img\Calculadora.ico')
 

estilos=ttk.Style()
estilos.theme_use('clam')
estilos.configure('mainframe.TFrame', background="#DBDBDB")

#Definimos el frame principal
mainfram=ttk.Frame(ventana_main,style="mainframe.TFrame")
mainfram.grid(column=0,row=0,sticky=(N,E,S,W))  

#Estilos del label1
estilos_label_1=ttk.Style()
estilos_label_1.configure('Label1.TLabel',font="arial 15",anchor="e")

valor_entrada_1=StringVar()
valor_entrada_2=StringVar()

label_valor_entrada_1=ttk.Label(mainfram,textvariable=valor_entrada_1,style="Label1.TLabel")
label_valor_entrada_1.grid(column=0,row=0,columnspan=4,sticky=(N,E,S,W))

#Estilos del label1
estilos_label_2=ttk.Style()
estilos_label_2.configure('Label2.TLabel',font="arial 40",anchor="e")

label_valor_entrada_2=ttk.Label(mainfram,textvariable=valor_entrada_2,style="Label2.TLabel")
label_valor_entrada_2.grid(column=0,row=1,columnspan=4,sticky=(N,E,S,W))


#Estilos de los botones

estilos_botones_numericos=ttk.Style()
estilos_botones_numericos.configure('Botones_numericos.TButton',font="arial 22",width=5,background="#FFFFFF",relief="flat")

estilos_botones_borrar=ttk.Style()
estilos_botones_borrar.configure('Botones_borrar.TButton',font="arial 22",width=5,background="#CECECE",relief="flat")
estilos_botones_borrar.map('Botones_borrar.TButton',foreground=[('active','#FF0000')])#Cuando de pase el cursor sobre los widgets de borrar camibiara al color rojo


estilos_botones_restantes=ttk.Style()
estilos_botones_restantes.configure('Botones_restantes.TButton',font="arial 22",width=5,background="#CECECE",relief="flat")

estilo_boton_igual=ttk.Style()
estilo_boton_igual.configure('Boton_igual.TButton',font="arial 22",width=5,background="#ff7801",relief="flat")

#Los botones numericos

buttom0=ttk.Button(mainfram,text="0" , style="Botones_numericos.TButton", command=lambda:ingresarValores('0',valor_entrada_2,valor_entrada_1))
buttom1=ttk.Button(mainfram,text="1",style="Botones_numericos.TButton", command=lambda:ingresarValores('1',valor_entrada_2,valor_entrada_1))
buttom2=ttk.Button(mainfram,text="2",style="Botones_numericos.TButton", command=lambda:ingresarValores('2',valor_entrada_2,valor_entrada_1))
buttom3=ttk.Button(mainfram,text="3",style="Botones_numericos.TButton", command=lambda:ingresarValores('3',valor_entrada_2,valor_entrada_1))
buttom4=ttk.Button(mainfram,text="4",style="Botones_numericos.TButton", command=lambda:ingresarValores('4',valor_entrada_2,valor_entrada_1))
buttom5=ttk.Button(mainfram,text="5",style="Botones_numericos.TButton", command=lambda:ingresarValores('5',valor_entrada_2,valor_entrada_1))
buttom6=ttk.Button(mainfram,text="6",style="Botones_numericos.TButton", command=lambda:ingresarValores('6',valor_entrada_2,valor_entrada_1))
buttom7=ttk.Button(mainfram,text="7",style="Botones_numericos.TButton", command=lambda:ingresarValores('7',valor_entrada_2,valor_entrada_1))
buttom8=ttk.Button(mainfram,text="8",style="Botones_numericos.TButton", command=lambda:ingresarValores('8',valor_entrada_2,valor_entrada_1))
buttom9=ttk.Button(mainfram,text="9",style="Botones_numericos.TButton", command=lambda:ingresarValores('9',valor_entrada_2,valor_entrada_1))

#Botones simbolos

buttom_borrar=ttk.Button(mainfram,text=chr(9003),style="Botones_borrar.TButton",command=lambda:borrar(valor_entrada_2)) 
buttom_borrar_todo=ttk.Button(mainfram,text="C",style="Botones_borrar.TButton",command=lambda:borrar_todo(valor_entrada_1,valor_entrada_2))
buttom_parentesis_1=ttk.Button(mainfram,text="(",style="Botones_restantes.TButton", command=lambda:parentesis1('(',valor_entrada_2,valor_entrada_1))
buttom_parentesis_2=ttk.Button(mainfram,text=")",style="Botones_restantes.TButton", command=lambda:parentesis2(')',valor_entrada_2,valor_entrada_1))
buttom_punto=ttk.Button(mainfram,text=".",style="Botones_restantes.TButton", command=lambda:ingresarValores('.',valor_entrada_2,valor_entrada_1))

#Botones Operaciones matematicas 

buttom_division=ttk.Button(mainfram,text=chr(247),style="Botones_restantes.TButton",command=lambda:division('/',valor_entrada_2,valor_entrada_1))
buttom_multiplicacion=ttk.Button(mainfram,text="*",style="Botones_restantes.TButton",command=lambda:multiplicacion('*',valor_entrada_2,valor_entrada_1))
buttom_resta=ttk.Button(mainfram,text="-",style="Botones_restantes.TButton",command=lambda:resta('-',valor_entrada_2,valor_entrada_1))
buttom_suma=ttk.Button(mainfram,text="+",style="Botones_restantes.TButton",command=lambda:suma('+',valor_entrada_2,valor_entrada_1))
buttom_raiz=ttk.Button(mainfram,text="√",style="Botones_restantes.TButton",command=lambda:raizCuadrada('√',valor_entrada_2,valor_entrada_1))
buttom_potencia=ttk.Button(mainfram,text="^",style="Botones_restantes.TButton",command=lambda:exponente('^',valor_entrada_2,valor_entrada_1))
buttom_igual=ttk.Button(mainfram,text="=",style="Boton_igual.TButton",command=lambda:igual('=',valor_entrada_2,valor_entrada_1))
buttom_signos=ttk.Button(mainfram,text="+/-",style="Botones_restantes.TButton",command=lambda:signos('+/-',valor_entrada_2,valor_entrada_1))
#Mostrar los botones en la pantalla

buttom_parentesis_1.grid(column=0,row=2,sticky=(N,E,S,W))
buttom_parentesis_2.grid(column=1,row=2,sticky=(N,E,S,W))
buttom_borrar_todo.grid(column=2,row=2,sticky=(N,E,S,W))
buttom_borrar.grid(column=3,row=2,sticky=(N,E,S,W))

buttom_suma.grid(column=0,row=3,sticky=(N,E,S,W))
buttom_resta.grid(column=1,row=3,sticky=(N,E,S,W))
buttom_multiplicacion.grid(column=2,row=3,sticky=(N,E,S,W))
buttom_division.grid(column=3,row=3,sticky=(N,E,S,W))

buttom7.grid(column=0,row=4,sticky=(N,E,S,W))
buttom8.grid(column=1,row=4,sticky=(N,E,S,W))
buttom9.grid(column=2,row=4,sticky=(N,E,S,W))
buttom_potencia.grid(column=3,row=4,sticky=(N,E,S,W))

buttom4.grid(column=0,row=5,sticky=(N,E,S,W))
buttom5.grid(column=1,row=5,sticky=(N,E,S,W))
buttom6.grid(column=2,row=5,sticky=(N,E,S,W))
buttom_raiz.grid(column=3,row=5,sticky=(N,E,S,W))

buttom1.grid(column=0,row=6,sticky=(N,E,S,W))
buttom2.grid(column=1,row=6,sticky=(N,E,S,W))
buttom3.grid(column=2,row=6,sticky=(N,E,S,W))
buttom_punto.grid(column=3,row=6,sticky=(N,E,S,W))

buttom_signos.grid(column=0,row=7,sticky=(N,E,S,W))
buttom0.grid(column=1,row=7,sticky=(N,E,S,W))
buttom_igual.grid(column=2,row=7,columnspan=2,sticky=(N,E,S,W))

# Itera a través de todos los widgets secundarios (children) del frame 'mainfram'.
for child in mainfram.winfo_children():
    child.grid_configure(ipady=10,padx=1,pady=1)

ventana_main.mainloop()