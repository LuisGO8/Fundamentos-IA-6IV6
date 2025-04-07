import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import *
from tkinter import *

class Gauss():
    def __init__(self):
        self.window = Tk()
        self.window.title("Distribución Normal")
        self.window.geometry('300x150')
        self.window.config(bg="#ebc9b7")

        Label(self.window, text="Datos a generar", font=("Sans-serif", 12), bg="#ebc9b7").pack(pady=10)
        
        self.entry = Entry(self.window, font=("Sans-serif", 12))
        self.entry.pack(pady=5)
        
        # Botón
        self.btnGraficar = Button(self.window, text="Graficar", command=self.graficar, font=("Sans-serif", 12), bg="#ebc9b7")
        self.btnGraficar.pack(pady=10)

        # Alerta para errores
        self.alerta = Label(self.window, text="", font=("Sans-serif", 10), bg="#ebc9b7")
        self.alerta.pack(pady=5)

        self.window.mainloop()
        
    def graficar(self):
        try:
            totalDatos = int(self.entry.get())
            if totalDatos <= 0:
                self.alerta.config(text="El número debe ser mayor a 0", fg="red")
                return
        except ValueError:
            self.alerta.config(text="Por favor ingrese valores correctos", fg="red")
            return
        
        self.alerta.config(text="", fg="red")

        # Parámetros de la distribución normal
        media = 0
        desviacion = 1
        
        # Generar los datos aleatorios con distribución normal
        data = np.random.normal(media, desviacion, totalDatos)

        # Histograma
        plt.figure(figsize=(10, 6))
        plt.hist(data, bins=30, density=True, alpha=0.6, color='skyblue', edgecolor='black')

        # Curva de Gauss
        xmin, xmax = plt.xlim()
        x = np.linspace(xmin, xmax, 100)
        p = norm.pdf(x, media, desviacion)
        plt.plot(x, p, 'k', linewidth=2)

        plt.title('Distribución Normal (Gaussiana)', fontsize=16)
        plt.xlabel('Valor', fontsize=12)
        plt.ylabel('Densidad', fontsize=12)
        plt.grid(True, linestyle='--', alpha=0.7)
        
        plt.tight_layout()
        plt.show()

app = Gauss()