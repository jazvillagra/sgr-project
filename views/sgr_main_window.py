from tkinter import *
from views.crear_sala_view import CrearSalaView
from views.listar_salas_view import ListarSalasView
from views.agendar_reunion_view import AgendarReunionView
from views.listar_reuniones_view import ListarReunionesView
#Globales
global crear_sala_view
global agendar_reunion_view
global listar_salas_view
global listar_reuniones_view
crear_sala_view = CrearSalaView()
agendar_reunion_view = AgendarReunionView()
listar_salas_view = ListarSalasView()
listar_reuniones_view = ListarReunionesView()

class Application(Frame):
  #metodo para crear una ventana. Recibe como parametros el titulo y el tamaño de la misma
  def crear_nueva_ventana(self, titulo, tam):
    ventana = Tk()
    height=str(tam//2)
    width=str(tam)
    size=width+"x"+height
    ventana.title(titulo)
    ventana.geometry(size)
    return ventana
  #inicializacion de vista principal
  def __init__(self):
    titulo_principal = "SGR Project"
    tam = 1000
    ventana_principal = self.crear_nueva_ventana(titulo_principal, tam)
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=100)
    agregar_sala_btn= Button(ventana_principal,text="Agregar Nueva Sala", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agregar_sala_btn.grid(row=1, column=1)
    agregar_sala_btn.config(comman= lambda: crear_sala_view.vista_agregar_sala_callback(ventana_principal, frame))
    listar_salas_btn= Button(ventana_principal,text="Listar salas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_salas_btn.grid(row=2, column=1)
    listar_salas_btn.config(comman= lambda: listar_salas_view.vista_lista_salas_callback(ventana_principal, frame))
    agendar_reu_btn = Button(ventana_principal,text="Agendar reunión", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agendar_reu_btn.config(comman= lambda: agendar_reunion_view.vista_agendar_reunion_callback(ventana_principal, frame))
    agendar_reu_btn.grid(row=3, column=1)
    listar_reu_unicas_btn = Button(ventana_principal,text="Listar reuniones unicas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_reu_unicas_btn.config(comman=lambda: listar_reuniones_view.listar_reuniones_unicas_callback(ventana_principal, frame))
    listar_reu_unicas_btn.grid(row=4, column=1)
    listar_reu_periodicas_btn = Button(ventana_principal,text="Listar reuniones periodicas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_reu_periodicas_btn.grid(row=5, column=1)
    listar_reu_periodicas_btn.config(comman=lambda: listar_reuniones_view.listar_reuniones_periodicas_callback(ventana_principal, frame))
    ventana_principal.mainloop()
def main():
  sgr_project = Application()
  return 0

if __name__ == '__main__':
    main()
