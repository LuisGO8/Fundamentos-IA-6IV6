#Grafico de linea recta

import numpy as np
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import * 

class main: 
    def __init__(self):
        self.window = Tk()
        self.window.title("Grafica de una pendiente")
        
        #Estilos
        bgColor = "#2e3535"
        fontStyle = ("Helvetica Neue", 12)
        txtColor = "#f1f5f5"
        entry = "#b8fcba"
        fontStyleEntry = ("Montserrat", 10)
        width = 300
        height = 260
        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        self.window.geometry(f"{width}x{height}+{x}+{y}")
        self.window.configure(bg=bgColor)

        



        #Variable en X
        Label(self.window, text="Valor en x", font=fontStyle, bg=bgColor, fg=txtColor).pack(pady=5)
        self.x = StringVar()
        Entry(self.window, textvariable=self.x, bg=entry, font=fontStyleEntry).pack(pady=5)

        #Variable en Y
        Label(self.window, text="Valor en Y", font=fontStyle, bg=bgColor, fg=txtColor).pack(pady=5)
        self.y = StringVar()
        Entry(self.window, textvariable=self.y, bg=entry, font=fontStyleEntry).pack(pady=5)
        
        #Pendiente
        Label(self.window, text="Valor de la pendiente", font=fontStyle, bg=bgColor, fg=txtColor).pack(pady=5)
        self.b = StringVar()
        Entry(self.window, textvariable=self.b, bg=entry, font=fontStyleEntry).pack(pady=5)

        #Bóton para graficar
        Button(self.window, text="Graficar", command=self.graficar, font=fontStyle, bg=bgColor, fg=txtColor).pack(pady=5)

        #Alerta para errores
        self.alerta = Label(self.window, text="", font=fontStyle, bg=bgColor)
        self.alerta.pack(pady=5)


        self.window.mainloop()

    


    def graficar(self):
        """
        Grafica de la forma y = mx + b 
        Despejando la pendiente tenemos que m = (y -b)/x
        """
        try:
            valorX = float(self.x.get())
            valorY = float(self.y.get())
            valorb = float(self.b.get())

            m = (valorY - valorb)/valorX
            x = np.linspace(-10, 10, 400)
            y = m * x + valorb


            plt.figure(figsize=(5, 4))
            plt.plot(x, y, label=f"y = {m:.2f}x + {valorb}")
            plt.scatter(valorX, valorY, color='red', zorder=3, label=f"Punto ({valorX}, {valorY})")
            plt.axhline(0, color='black', linewidth=0.5)
            plt.axvline(0, color='black', linewidth=0.5)
            plt.grid(True, linestyle='--', linewidth=0.5)
            plt.legend()
            plt.show()

        except ValueError:
            self.alerta.config(text="Por favor ingrese valores correctos", fg="white")


app = main() 