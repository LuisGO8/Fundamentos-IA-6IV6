'''
Evaluar el sueldo que recibe un trabajador
Aumento del 15% si es menor a 4,000
Aumento del 8% si es mayor a 4,000
'''

from tkinter import * 
from tkinter import ttk

class E1:
    def __init__(self):
        self.window=Tk()
        self.window.title("Aumento Sueldo")
        self.window.geometry('300x300')
        self.window.config(bg="#48ffe1")
        
        #Texto
        self.infoLabel = Label(self.window, text="Ingrese su sueldo para conoer su aumento")
        self.infoLabel.grid(row=1, column=1, pady=10)

        #Salario
        self.salarioInicial = StringVar()
        self.salarioInput = Entry(self.window, textvariable=self.salarioInicial)
        self.salarioInput.grid(row=2, column=1)

        #Boton 
        self.boton = Button(self.window, text="Calcular aumento", command=self.calcular, bg="#488dff", fg="white")
        self.boton.grid(row=3, column=1)

        #Resultado
        self.resultadoLabel = Label(self.window, text="Aumento")
        self.resultadoLabel.grid(row=4, column=1)

        self.window.mainloop()
    
    def calcular(self):
        try:
            sueldo = float(self.salarioInicial.get())
            if sueldo < 4000:
                aumento = sueldo*0.15
            else:
                aumento = sueldo*0.08
            
            nuevoSueldo = sueldo + aumento
            self.resultadoLabel.config(text=f"Nuevo sueldo: ${nuevoSueldo}", fg="red")
        except ValueError:
            self.resultadoLabel.config(text="Sueldo no valido")


app = E1()