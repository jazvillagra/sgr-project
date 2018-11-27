from tkinter import *
from controllers import *
class VistaSala(Frame):

    ventana_principal = Tk()
    ventana_principal.title('SGR Project')
    ventana_principal.geometry("400x200")
    agregar_sala_btn = Button(ventana_principal, text="Salir", command= ventana_principal.quit())