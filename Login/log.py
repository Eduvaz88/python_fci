import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql

def menu_pantalla():
    global pantalla
    pantalla=Tk()
    pantalla.geometry("300x380")
    pantalla.title("bienvenidos")
    pantalla.iconbitmap("fci.ico")

    image=PhotoImage(file="fci.gif")
    image=image.subsample(2,2)
    label=Label(image=image)
    label.pack()

    Label(text="Acceso al Sistema", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(text="").pack()

    Button(text="Iniciar Sesion", height="3", width="30", command=inicio_sesion).pack()
    Label(text="").pack()

    Button(text="Registrar", height="3", width="30").pack()

    pantalla.mainloop()

def inicio_sesion():
    global pantalla1
    pantalla1 = Toplevel(pantalla)
    pantalla1.geometry("400x250")
    pantalla1.title("Inicio de sesion")
    pantalla1.iconbitmap("fci.ico")

    Label(pantalla1, text="Por favor ingrese usuario y contraseña", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla1, text="").pack()

    global nombreusuario_verify
    global contraseniousuario_verify

    nombreusuario_verify=StringVar()
    contraseniousuario_verify=StringVar()

    global nombreusuario_entry
    global contraseniousuario_entry

    Label(pantalla1, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla1, textvariable=nombreusuario_verify)
    nombreusuario_entry.pack()
    Label(pantalla1).pack()

    Label(pantalla1, text="Contraseña").pack()
    contraseniousuario_entry = Entry(pantalla1, textvariable=contraseniousuario_verify)
    contraseniousuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar sesion").pack()

menu_pantalla()
