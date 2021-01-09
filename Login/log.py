import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

pantalla=Tk()
pantalla.geometry("300x380")
pantalla.title("bienvenidos")
pantalla.iconbitmap("fci.ico")

image=PhotoImage(file="fci.gif")
image=image.subsample(2,2)
label=Label(image=image)
label.pack()

Label(text="Acceso al Sistema", bg="navy", fg="white", width=300, heigth=3, font=("Calibri", 15)).pack()
Label(text="").pack()

print("hola mundo")

pantalla.mainloop()
