from tkinter import *
from views.sala_view import SalaView
from views.reunion_view import ReunionView
from controllers.sala_controller import SalaController
#
# class VistaSalas(Frame):
#   def __init__(self):
#     ventana_salas = Tk()
#     ventana_salas.title('SGR Project')
#     ventana_salas.geometry("400x200")

global sala_controller
global vista_sala
global vista_reunion
sala_controller = SalaController()
vista_sala = SalaView()
vista_reunion = ReunionView()
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
    agregar_sala_btn.config(comman= lambda: vista_sala.vista_agregar_sala_callback(ventana_principal, frame))
    listar_salas_btn= Button(ventana_principal,text="Listar salas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_salas_btn.grid(row=2, column=1)
    listar_salas_btn.config(comman= lambda: vista_sala.vista_lista_salas_callback(ventana_principal, frame))
    agendar_reu_btn = Button(ventana_principal,text="Agendar reunión", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agendar_reu_btn.config(comman= lambda: vista_reunion.vista_agendar_reunion_callback(ventana_principal, frame))
    agendar_reu_btn.grid(row=3, column=1)
    listar_reu_btn = Button(ventana_principal,text="Listar reuniones", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_reu_btn.grid(row=4, column=1)
    ventana_principal.mainloop()
def main():
  sgr_project = Application()
  return 0

if __name__ == '__main__':
    main()
