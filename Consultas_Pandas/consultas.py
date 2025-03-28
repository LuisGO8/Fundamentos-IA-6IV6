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

        Label(self.window, text="Nombre").pack(pady=5)
        self.usuario = StringVar()
        Entry(self.window, textvariable=self.usuario).pack(pady=5)

        Label(self.window, text="Contraseña").pack(pady=5)
        self.password = StringVar()
        Entry(self.window, textvariable=self.password, show="*").pack(pady=5)

        self.alerta = Label(self.window, text="")
        self.alerta.pack(pady=5)

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
        width = 1300
        height = 600

        screen_width = self.newWindow.winfo_screenwidth()
        screen_height = self.newWindow.winfo_screenheight()
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2

        self.newWindow.geometry(f"{width}x{height}+{x}+{y}")

        self.df = pd.read_csv("Sacramentorealestatetransactions.csv")
        print(self.df)


        Button(self.newWindow, text="Residenciales con 3 camas, menores a 60 000", command=self.consulta1).pack(pady=5)
        Button(self.newWindow, text="Sacramento, 2 baños, condominio", command=self.consulta2).pack(pady=5)
        Button(self.newWindow, text="Elk Grove, 4 camas, más de 80 000", command=self.consulta3).pack(pady=5)
        Button(self.newWindow, text="Casas grandes, más de 2000 sqft", command=self.consulta4).pack(pady=5)
        Button(self.newWindow, text="Propiedades vendidas en 2008", command=self.consulta5).pack(pady=5)
        Button(self.newWindow, text="Zip 95838, más de 2 baños", command=self.consulta6).pack(pady=5)
        Button(self.newWindow, text="Casas en Rancho Cordova", command=self.consulta7).pack(pady=5)
        Button(self.newWindow, text="Menos de 100 000 y más de 2 camas", command=self.consulta8).pack(pady=5)
        Button(self.newWindow, text="Departamentos en zip 95670", command=self.consulta9).pack(pady=5)
        Button(self.newWindow, text="Más de 3 baños y precio superior a 500 000", command=self.consulta10).pack(pady=5)


        #Resultado
        self.resultado = Text(self.newWindow, height=20, width=180)
        self.resultado.pack(pady=5)




        self.newWindow.mainloop()





    def actualizar_resultado(self, texto):
        self.resultado.delete(1.0, END)
        self.resultado.insert(END, texto)

    def consulta1(self):
        resultado = self.df.query("type == 'Residential' and beds >= 3 and price < 60000")
        self.actualizar_resultado(resultado.to_string())

    def consulta2(self):
        resultado = self.df.query("type == 'Condo' and baths >= 2 and city == 'SACRAMENTO'")
        self.actualizar_resultado(resultado.to_string())

    def consulta3(self):
        resultado = self.df.query("price > 80000 and beds >= 4 and city == 'ELK GROVE'")
        self.actualizar_resultado(resultado.to_string())

    def consulta4(self):
        resultado = self.df.query("sq__ft > 2000")
        self.actualizar_resultado(resultado.to_string())

    def consulta5(self):
        resultado = self.df[self.df['sale_date'].str.contains("2008")] 
        self.actualizar_resultado(resultado.to_string())

    def consulta6(self):
        resultado = self.df.query("zip == 95838 and baths > 2")
        self.actualizar_resultado(resultado.to_string())

    def consulta7(self):
        resultado = self.df.query("city == 'RANCHO CORDOVA'")
        self.actualizar_resultado(resultado.to_string())

    def consulta8(self):
        resultado = self.df.query("price < 100000 and beds > 2")
        self.actualizar_resultado(resultado.to_string())

    def consulta9(self):
        resultado = self.df.query("zip == 95670 and type == 'Condo'")
        self.actualizar_resultado(resultado.to_string())

    def consulta10(self):
        resultado = self.df.query("baths > 3 and price > 500000")
        self.actualizar_resultado(resultado.to_string())


app = Login()
