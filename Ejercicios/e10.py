"""
Mostrar el nombre
Monto por trabajar horas normales 
Monto por trabajar horas extra (50% extra del pago normal)
Bonificación por hijo del 5% del pago por hora
Pago total
"""

from tkinter import *

class E10:
    def __init__(self):
        self.window = Tk()
        self.window.title("Pago total")
        self.window.geometry("350x300")

        # Texto
        self.infoLabel = Label(self.window, text="Conozca su pago total")
        self.infoLabel.grid(row=1, column=1, pady=10)

        # Pago por hora
        self.pagoHora = StringVar()
        Label(self.window, text="Pago por hora").grid(row=2, column=1)
        self.pagoInput = Entry(self.window, textvariable=self.pagoHora)
        self.pagoInput.grid(row=2, column=2)

        # Monto por horas normales 
        self.horasNormales = StringVar()
        Label(self.window, text="Cantidad de horas normales").grid(row=3, column=1)
        self.horasInput = Entry(self.window, textvariable=self.horasNormales)
        self.horasInput.grid(row=3, column=2)

        # Monto por horas extra
        self.horasExtra = StringVar()
        Label(self.window, text="Cantidad de horas extra").grid(row=4, column=1)
        self.horasEInput = Entry(self.window, textvariable=self.horasExtra)
        self.horasEInput.grid(row=4, column=2)

        # Cantidad de hijos
        self.numHijos = StringVar()
        Label(self.window, text="Número de hijos").grid(row=5, column=1)
        self.hijosInput = Entry(self.window, textvariable=self.numHijos)
        self.hijosInput.grid(row=5, column=2)

        # Botón 
        self.boton = Button(self.window, text="Calcular pago total", command=self.calcular)
        self.boton.grid(row=6, column=2, pady=10)

        # Salario total
        self.pagoLabel = Label(self.window, text="Pago total: -")
        self.pagoLabel.grid(row=7, column=2, pady=10)

        self.window.mainloop()

    def calcular(self):
        try:
            pagoHora = float(self.pagoHora.get())
            horasN = int(self.horasNormales.get())
            horasE = int(self.horasExtra.get())
            hijos = int(self.numHijos.get())

            if pagoHora > 0 and horasN >= 0 and horasE >= 0 and hijos >= 0:
                total = (pagoHora * horasN) + (pagoHora * horasE * 1.5) + (pagoHora * hijos * 0.05)
                self.pagoLabel.config(text=f"Pago total: {total}")
            else:
                self.pagoLabel.config(text="Ingrese valores positivos")

        except ValueError:
            self.pagoLabel.config(text="Ingrese valores numéricos válidos", fg="red")

app = E10()
