'''
Parque de diversiones
Personas menores a 10 años descuento del 25 %
Costo del boleto 50 soles
Cuanto paga un niño
Y cuanto un No niño

'''

from tkinter import * 
from tkinter import ttk

class E2:
    def __init__(self):
        self.window=Tk()
        self.window.title("Boletos")
        self.window.geometry("600x200")
        self.window.config(bg="#faffb0")

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese la cantidad de boletos y edad para conocer cuanto va a pagar")
        self.infoLabel.grid(row=1, column=1)

        #Cantidad de boletos 
        self.cantidadBoletos = StringVar()
        self.boletosLabel = Label(self.window, text="Cantidad de boletos")
        self.boletosLabel.grid(row=2, column=0)
        self.boletosInput = Entry(self.window, textvariable=self.cantidadBoletos)
        self.boletosInput.grid(row=2, column=1)

        #Edad
        self.edad = StringVar()
        self.edadLabel = Label(self.window, text="Edad")
        self.edadLabel.grid(row=3, column=0)
        self.edadInput = Entry(self.window, textvariable=self.edad)
        self.edadInput.grid(row=3, column=1)

        #Boton 
        self.boton = Button(self.window, text="Calcular Total", command=self.calcular)
        self.boton.grid(row=4, column=1)

        #Cantidad a pagar 
        self.totalLabel = Label(self.window, text="Total")
        self.totalLabel.grid(row=5, column=1)

        self.window.mainloop()
    
    def calcular(self):
        try:
            edad = int(self.edad.get())
            cantidadBoletos = int(self.cantidadBoletos.get())
            if edad<10:
                total= cantidadBoletos*50*0.75
            else:
                total = cantidadBoletos*50
            
            self.totalLabel.config(text=f"Debe pagar: ${total}", fg="red")
        except ValueError:
            self.totalLabel.config("Por favor ingrese un valor")


app = E2()