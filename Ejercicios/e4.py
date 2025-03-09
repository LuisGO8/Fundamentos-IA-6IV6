"""
Mostrar numeros menores a 10
"""

from tkinter import * 
from tkinter import ttk

class E4:
    def __init__(self):
        self.window=Tk()
        self.window.title("Numero menor a 10")
        self.window.geometry("200x200")
        self.window.config(bg="#f4ffb0")

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese un numero menor a 10")
        self.infoLabel.grid(row=1, column=1)

        #Numero 
        self.numero = StringVar()
        self.numInput = Entry(self.window, textvariable=self.numero)
        self.numInput.grid(row=2, column=1)
        self.numInput.bind("<KeyRelease>", self.verificar)

        #Resultado
        self.resultadoLabel = Label(self.window, text="Esperando numero...")
        self.resultadoLabel.grid(row=3, column=1)

        self.window.mainloop()

    def verificar(self, event=None):
        try:
            numero = int(self.numero.get())
            if numero<10:
                self.resultadoLabel.config(text=f"Correcto: {numero}", fg="green")
            else:
                self.resultadoLabel.config(text=f"Incorrecto: {numero} numero mayor a 10", fg="red")
        except ValueError:
            if self.numero.get() == "":
                self.resultadoLabel.config(text="Esperando numero...", fg="black")
            else:
                self.resultadoLabel.config(text="Número no válido", fg="red")

app = E4()