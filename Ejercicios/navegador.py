from tkinter import *

class Navegador:
    def __init__(self):
        self.window = Tk()
        self.window.title("Menu de ejercicios")
        self.window.geometry("400x500")

        Label(self.window, text="Selecciona una opcion", font=("Arial", 14, "bold")).grid(row=1, column=1)

        ejercicios = [
            ("Ejercicio 1", E1),
            ("Ejercicio 2", E2),
            ("Ejercicio 3", E3),
            ("Ejercicio 4", E4),
            ("Ejercicio 5", E5),
            ("Ejercicio 6", E6),
            ("Ejercicio 7", E7),
            ("Ejercicio 8", E8),
            ("Ejercicio 9", E9),
            ("Ejercicio 10", E10)
        ]

        for i, (texto, clase) in enumerate(ejercicios, start=2):
            Button(self.window, text=texto, command=lambda c=clase: c()).grid(row=i, column=1, pady=5)



        self.window.mainloop()


class E1:
    def __init__(self):
        self.window=Toplevel()
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

class E2:
    def __init__(self):
        self.window=Toplevel()
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

class E3:
    def __init__(self):
        self.window=Toplevel()
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

class E4:
    def __init__(self):
        self.window=Toplevel()
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

class E5:
    def __init__(self):
        self.window=Toplevel()
        self.window.title("Numero menor a 10")
        self.window.geometry("200x200")
        self.window.config(bg="#f4ffb0")

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese un numero entre 0 y 20")
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
            if 0<numero<20:
                self.resultadoLabel.config(text=f"Correcto: {numero}", fg="green")
            else:
                self.resultadoLabel.config(text=f"Incorrecto: {numero} fuera del rango", fg="red")
        except ValueError:
            if self.numero.get() == "":
                self.resultadoLabel.config(text="Esperando numero...", fg="black")
            else:
                self.resultadoLabel.config(text="Número no válido", fg="red")

class E6:
    def __init__(self):
        self.window=Toplevel()
        self.window.title("Numero menor a 10")
        self.window.geometry("200x200")
        self.window.config(bg="#f4ffb0")

        self.intentosIncorrectos = 0

        #Texto
        self.infoLabel = Label(self.window, text="Ingrese un numero entre 0 y 20")
        self.infoLabel.grid(row=1, column=1)

        #Numero 
        self.numero = StringVar()
        self.numInput = Entry(self.window, textvariable=self.numero)
        self.numInput.grid(row=2, column=1)
        self.numInput.bind("<KeyRelease>", self.verificar)

        #Resultado
        self.resultadoLabel = Label(self.window, text="Esperando numero...")
        self.resultadoLabel.grid(row=3, column=1)

        #Cantidad de intentos 
        self.intentosLabel = Label(self.window, text="Cantidad de intentos...")
        self.intentosLabel.grid(row=4, column=1)

        self.window.mainloop()


    def verificar(self, event=None):
        try:
            numero = int(self.numero.get())
            if 0<numero<20:
                self.resultadoLabel.config(text=f"Correcto: {numero}", fg="green")
            else:
                self.resultadoLabel.config(text=f"Incorrecto: {numero} fuera del rango", fg="red")
                self.intentosIncorrectos +=1
                self.intentosLabel.config(text=f"Cantidad de intentos {self.intentosIncorrectos}")
                self.numInput.delete(0, END)
        except ValueError:
            if self.numero.get() == "":
                self.resultadoLabel.config(text="Esperando numero...", fg="black")
            else:
                self.resultadoLabel.config(text="Número no válido", fg="red")
                self.numInput.delete(0, END)

class E7:
    def __init__(self):
        self.window=Toplevel()
        self.window.title("Calculo de n numeros")
        self.window.geometry("200x200")
        self.window.config(bg="#b0b7ff")

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
            suma = sum(range(1, numero+1))
            self.resultadoLabel.config(text=f"Resultado {suma}", fg="red")
        except ValueError:
            self.resultadoLabel.config(text="Numero no valido")

class E8:
    def __init__(self):
        self.window=Toplevel()
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
                self.numInput.config(state=DISABLED)
                self.resultadoLabel.config(text=f"Suma final: {self.suma}", fg="red")
            else:
                self.suma += numero
                self.resultadoLabel.config(text=f"Suma {self.suma}")
        except ValueError:
            self.resultadoLabel.config(text="Numero no valido")

class E9:
    def __init__(self):
        self.window=Toplevel()
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
            self.suma += numero
            if self.suma > 100:
                self.numInput.config(state=DISABLED)
                self.resultadoLabel.config(text=f"Suma final: {self.suma}", fg="red")
            else:
                self.resultadoLabel.config(text=f"Suma {self.suma}")
        except ValueError:
            self.resultadoLabel.config(text="Numero no valido")
    
class E10:
    def __init__(self):
        self.window = Toplevel()
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



app = Navegador()

