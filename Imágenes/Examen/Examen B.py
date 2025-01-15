from tkinter import *
from tkinter import messagebox
import random
ventana = Tk()

#Operaciones
numrandom = random.randint(1,49)
dinero = numrandom *2

#Ventana

ventana.geometry('550x350')
ventana.title("Examen B")

#Etiqueta

num1= random.randint(1,49)
num2= random.randint(1,49)
num3= random.randint(1,49)
num4= random.randint(1,49)
num5= random.randint(1,49)
num6= random.randint(1,49)

etiqueta = Label(ventana, text="LOTERÍA PRIMITIVA", font=("arial Bold", 15))
etiqueta.grid(column=0,row=0)

etiqueta = Label(ventana, text="Introduce el número de apuestas:", font=("arial Bold", 15))
etiqueta.grid(column=0,row=1)

cajaTexto =Entry(ventana, width=10)
cajaTexto.grid(column=0,row=2)

etiqueta = Label(ventana, text= num1, font=("arial Bold", 36))
etiqueta.grid(column=0,row=30)

etiqueta = Label(ventana, text= num2, font=("arial Bold", 36))
etiqueta.grid(column=1,row=30)

etiqueta = Label(ventana, text= num3, font=("arial Bold", 36))
etiqueta.grid(column=2,row=30)

etiqueta = Label(ventana, text= num4, font=("arial Bold", 36))
etiqueta.grid(column=3,row=30)

etiqueta = Label(ventana, text= num5, font=("arial Bold", 36))
etiqueta.grid(column=4,row=30)

etiqueta = Label(ventana, text= num6, font=("arial Bold", 36))
etiqueta.grid(column=5,row=30)


def clicked():

    messagebox.showinfo("Primitiva", "El precio es {} €")

boton = Button(ventana, text="Calcular", command=clicked)
boton.grid(column=0,row=5)

ventana.mainloop()
#Operación



