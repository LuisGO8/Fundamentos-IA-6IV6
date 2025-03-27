from tkinter import *
import pandas as pd


class Login:
    def __init__(self):
        self.window = Tk()
        self.window.title("Inicio de sesión")

        width = 300
        height = 200

        screen_width = self.window.winfo_screenwidth()
        screen_height = self.window.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.window.geometry(f"{width}x{height}+{x}+{y}")

        # Nombre
        Label(self.window, text="Nombre").pack(pady=5)
        self.usuario = StringVar()
        Entry(self.window, textvariable=self.usuario).pack(pady=5)

        # Contraseña
        Label(self.window, text="Contraseña").pack(pady=5)
        self.password = StringVar()
        Entry(self.window, textvariable=self.password, show="*").pack(pady=5)

        # Alerta
        self.alerta = Label(self.window, text="")
        self.alerta.pack(pady=5)

        # Botón
        Button(self.window, text="Iniciar sesión", command=self.inicioSesion).pack(pady=5)

        self.window.mainloop()

    def inicioSesion(self):
        usuario = self.usuario.get().strip().lower()
        contrasena = self.password.get()

        if usuario == 'luis' and contrasena == '1234':
            self.window.destroy()
            print("Inicio de sesión exitoso")
            Consultas()
        else:
            self.alerta.config(text="Usuario o contraseña incorrectos", fg="red")


class Consultas:
    def __init__(self):
        self.newWindow = Tk()
        self.newWindow.title("Consultas usando pandas")
        width = 600
        height = 600

        screen_width = self.newWindow.winfo_screenwidth()
        screen_height = self.newWindow.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.newWindow.geometry(f"{width}x{height}+{x}+{y}")

        self.df = pd.read_csv("Sacramentorealestatetransactions.csv")
        print(self.df)

        # Buscar ciudad
        Label(self.newWindow, text="Buscar ciudad: ").pack(pady=5)
        self.ciudad = StringVar()
        Entry(self.newWindow, textvariable=self.ciudad).pack(pady=5)
        Button(self.newWindow, text="Buscar", command=self.buscarCiudades).pack(pady=5)

        #Boton para buscar para buscar por ciudad = sacramento, menor a 1000





        # Resultados
        self.resultado = Label(self.newWindow, text="", height=20, width=90)
        self.resultado.pack(pady=5)

        self.newWindow.mainloop()


        #Button(self.newWindow, text="Primeros 5 elementos", command=self.mostrar_head).pack(pady=2)





    def buscarCiudades(self):
        ciudad = self.ciudad.get().strip().upper()  
        if ciudad:
            ciudades = self.df[self.df['city'].str.contains(ciudad, na=False)]['city'].unique()
            resultado = "\n".join(ciudades) if len(ciudades) > 0 else "No se encontraron coincidencias"
            self.resultado.config(text=resultado)
        else:
            self.resultado.config(text="Por favor ingrese una ciudad")


"""
def actualizar_resultado(self, texto):
        self.resultado.delete(1.0, END)
        self.resultado.insert(END, texto)
    def mostrar_head(self):
        self.actualizar_resultado(self.df.head().to_string())
"""
    

app = Login()
