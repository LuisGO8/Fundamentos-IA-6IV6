from tkinter import *

from tkinter import ttk

window = Tk()

window.title("Aplicación")

window.geometry('600x600')

window.config(bg = 'beige')

frame=Frame()

frame.pack()

frame.config(width="400",height="400")

frame.config(bg = 'red')

frame.config(bd=35)

frame.config(relief='groove')

#frame.config(relief='sunken')

frame.config(cursor='pirate')

#label=Label(frame,text="Hola alumnos de Python",fg="blue",font=("Comic Sans MS",10))

#ubicar el lugar

#label.place(x=100,y=200)

miimagen=PhotoImage(file="a.gif")

label=Label(frame,image=miimagen).place(x=10,y=30)

window.mainloop()



#def_init_(self) guuarda como constructor (es el this del java)