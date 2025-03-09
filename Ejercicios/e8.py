"""
Suma de los numeros ingresados hasta que el numero sea 0
"""

from tkinter import * 
from tkinter import ttk

class E8:
    def __init__(self):
        self.window=Tk()
        self.window.title("Suma de numeros")
        self.window.geometry("200x200")
        self.window.config(bg="#afd972")

        self.suma = 0

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese un numero")
        self.infoLabel.grid(row=1, column=1)

        #Numero 
        self.numero = StringVar()
        self.numInput = Entry(self.window, textvariable=self.numero)
        self.numInput.grid(row=2, column=1)

        #Boton
        self.boton = Button(self.window, text="Calcular", command=self.calcular)
        self.boton.grid(row=3, column=1)

        #Resultado
        self.resultadoLabel = Label(self.window, text="Resultado")
        self.resultadoLabel.grid(row=4, column=1)

        self.window.mainloop()

    def calcular(self):
        try:
            numero = int(self.numero.get())
            if numero == 0:
                self.resultadoLabel.config(text=f"Suma final: {self.suma}", fg="red")
            else:
                self.suma += numero
                self.resultadoLabel.config(text=f"Suma: {self.suma}")
        except ValueError:
            self.resultadoLabel.config(text="Numero no valido")
            
app = E8()