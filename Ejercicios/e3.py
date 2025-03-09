"""
Descuento del 15% en octube
Mes e importe
"""
from tkinter import * 
from tkinter import ttk

class E3:
    def __init__(self):
        self.window=Tk()
        self.window.title("Importe por mes")
        self.window.geometry("400x200")
        self.window.config(bg="#c0ffb0")

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese el mes e importe de la compra")
        self.infoLabel.grid(row=1, column=1)

        #Mes 
        self.mes = StringVar()
        self.mesLabel = Label(self.window, text="Ingrese el mes")
        self.mesLabel.grid(row=2, column=0)
        self.mesInput = Entry(self.window, textvariable=self.mes)
        self.mesInput.grid(row=2, column=1)

        #Importe
        self.importe = StringVar()
        self.importeLabel = Label(self.window, text="Importe")
        self.importeLabel.grid(row=3, column=0)
        self.imorteInput = Entry(self.window, textvariable=self.importe)
        self.imorteInput.grid(row=3, column=1)

        #Boton 
        self.boton = Button(self.window, text="Calcular Total", command=self.calcular)
        self.boton.grid(row=4, column=1)

        #Cantidad a pagar 
        self.totalLabel = Label(self.window, text="Total")
        self.totalLabel.grid(row=5, column=1)

        self.window.mainloop()
    
    def calcular(self):
        try:
            importe = float(self.importe.get())
            mes = self.mes.get().strip().lower()
            if mes== "octubre":
                total= importe*0.85
            else:
                total = importe
            
            self.totalLabel.config(text=f"Debe pagar: ${total}", fg="red")
        except ValueError:
            self.totalLabel.config("Por favor ingrese un valor")

app = E3()