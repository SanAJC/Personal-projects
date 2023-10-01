import math

def ingresarValores(tecla,valor_entrada_2,valor_entrada_1):
    if tecla >= '0' and tecla <= '9' or tecla=='.' :
        valor_entrada_2.set(valor_entrada_2.get()+str(tecla) )
        


def resta(tecla,valor_entrada_2,valor_entrada_1):
    if ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla=='-':
        valor_entrada_1.set(valor_entrada_2.get()+'-')


    valor_entrada_2.set('') 


def suma(tecla,valor_entrada_2,valor_entrada_1):
    if ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla=='+':
        valor_entrada_1.set(valor_entrada_2.get()+'+')


    valor_entrada_2.set('')


def multiplicacion (tecla, valor_entrada_2, valor_entrada_1):
    if ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla=='*':
        valor_entrada_1.set(valor_entrada_2.get()+'*')

    valor_entrada_2.set('')



def division(tecla,valor_entrada_2,valor_entrada_1):
    if ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla=='/':
        valor_entrada_1.set(valor_entrada_2.get()+'/')

    valor_entrada_2.set('')



def raizCuadrada(tecla,valor_entrada_2, valor_entrada_1):

    if ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla=='√':


        if valor_entrada_2.get==False:
            valor_entrada_2.set('√'+valor_entrada_2.get())
              
        else:
            valor_entrada_2.set(valor_entrada_2.get()+'√')
            
def exponente(tecla, valor_entrada_2, valor_entrada_1):
    if  ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla == '^':
        valor_entrada_1.set(valor_entrada_2.get() + '^')

    valor_entrada_2.set('')

def parentesis1(tecla, valor_entrada_2, valor_entrada_1):
    if  ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla == '(':
        if valor_entrada_2.get==False:
            valor_entrada_2.set('('+valor_entrada_2.get())
              
        else:
            valor_entrada_2.set(valor_entrada_2.get()+'(')

def parentesis2(tecla, valor_entrada_2, valor_entrada_1):
    if  ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla == ')':
        if valor_entrada_2.get==False:
            valor_entrada_2.set(')'+valor_entrada_2.get())
              
        else:
            valor_entrada_2.set(valor_entrada_2.get()+')')

def signos(tecla,valor_entrada_2,valor_entrada_1):
    if  ingresarValores(tecla,valor_entrada_1,valor_entrada_2)==True or tecla == '+/-':
        if valor_entrada_2.get() == '':
            valor_entrada_2.set('-')




def igual(tecla,valor_entrada_2,valor_entrada_1):

    if tecla=='=':
        
        if '+' in valor_entrada_1.get():        
            valor_entrada_1.set(valor_entrada_1.get()+valor_entrada_2.get())
            resultado = eval(valor_entrada_1.get())
            valor_entrada_2.set(resultado)

        elif '-' in valor_entrada_1.get():
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            resultado=eval(valor_entrada_1.get())
            valor_entrada_2.set(resultado)

        elif '*'in valor_entrada_1.get():
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            resultado=eval(valor_entrada_1.get())
            valor_entrada_2.set(resultado)

        elif '/' in valor_entrada_1.get():
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            resultado=eval(valor_entrada_1.get())
            valor_entrada_2.set(resultado)

        elif '√' in  valor_entrada_2.get() :
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            numero = float(valor_entrada_1.get().replace('√',''))

            resultado=math.sqrt(numero)
            valor_entrada_2.set(resultado)

        elif '^' in valor_entrada_1.get() :
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            numero=(valor_entrada_1.get().replace("^","**"))
            resultado=eval(numero)

            valor_entrada_2.set(resultado)

        elif '(' in valor_entrada_2.get() or ')' in valor_entrada_2.get() :
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            numero=(valor_entrada_1.get().replace("(","").replace(")","*"))
            resultado=eval(numero)

            valor_entrada_2.set(resultado) 
            
        elif '-'  in valor_entrada_2.get():
            valor_entrada_1.set(valor_entrada_1.get()+ valor_entrada_2.get())
            resultado=eval(valor_entrada_1.get())
            valor_entrada_2.set(resultado)




def borrar(valor_entrada_2):
    inicio=0
    final=len(valor_entrada_2.get())

    valor_entrada_2.set(valor_entrada_2.get()[inicio:final-1]) 

def borrar_todo(valor_entrada_1,valor_entrada_2):
    valor_entrada_1.set("")
    valor_entrada_2.set("")
    
