import tkinter
from tkinter import*
from tkinter import messagebox
import pymysql
import pymysql.cursors


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

    Button(text="Registrar", height="3", width="30", command=registrar).pack()

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
    contraseniousuario_entry = Entry(pantalla1, show="*", textvariable=contraseniousuario_verify)
    contraseniousuario_entry.pack()
    Label(pantalla1).pack()

    Button(pantalla1, text="Iniciar sesion", command=validacion_datos).pack()

def registrar():
    global pantalla2
    pantalla2 = Toplevel(pantalla)
    pantalla2.geometry("400x250")
    pantalla2.title("Registro")
    pantalla2.iconbitmap("fci.ico")

    global nombreusuario_entry
    global contrasena_entry

    nombreusuario_entry=StringVar()
    contrasena_entry=StringVar()

    Label(pantalla2, text="Ingrese usuario y contrasenia", bg="navy", fg="white", width="300", height="3", font=("Calibri", 15)).pack()
    Label(pantalla2, text="").pack()

    Label(pantalla2, text="Usuario").pack()
    nombreusuario_entry = Entry(pantalla2)
    nombreusuario_entry.pack()
    Label(pantalla2).pack()

    Label(pantalla2, text="Contrasena").pack()
    contrasena_entry = Entry(pantalla2, show="*")
    contrasena_entry.pack()
    Label(pantalla2).pack()

    Button(pantalla2, text="Registrar", command=inserta_datos).pack()


def inserta_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="db_proyecto"
        )

    fcursor=bd.cursor()

    sql="INSERT INTO login (usuario,contrasena) VALUES ('{0}','{1}')".format(nombreusuario_entry.get(), contrasena_entry.get())

    try:
            fcursor.execute(sql)
            bd.commit()
            messagebox.showinfo(message="Registro exitoso!", title="Aviso")

    except:
            bd.rollback()
            messagebox.showinfo(message="No registrado", title="Aviso")

    bd.close()

def validacion_datos():
    bd=pymysql.connect(
        host="localhost",
        user="root",
        passwd="",
        db="db_proyecto"
        )

    fcursor=bd.cursor()

    fcursor.execute("SELECT contrasena FROM login WHERE usuario='"+nombreusuario_verify.get()+"' and contrasena='"+contraseniousuario_verify.get()+"'")

    if fcursor.fetchall():
        messagebox.showinfo(title="Los datos son:", message="Correctos")
    else:
         messagebox.showinfo(title="Los datos son:", message="Correctos")

    bd.close()
menu_pantalla()
