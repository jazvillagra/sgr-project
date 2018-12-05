from tkinter import Frame, Text, END, DISABLED
from views.entry import Entry
from controllers.sala_controller import SalaController
#Global variables
global controller
global Entry
entry = Entry()
controller = SalaController()

class ListarSalasView:
  def vista_lista_salas_callback(self, ventana_principal, frame):
    frame.grid_remove()
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=200, columnspan=200)
    frame.config(width=900)
    lista = Text(frame)
    lista_salas = controller.listar_salas()
    count = 0
    for i in lista_salas:
        count += 1
        lista.insert(END, "Nombre sala: " + i.nombre_sala + "\n")
        lista.insert(END, "Max. ocupantes: " + str(i.max_ocupantes) + "\n")
        lista.insert(END, "Estado de sala: " + i.estado_sala + "\n\n")
    lista.config(width=900, state=DISABLED)
    lista.grid(row=1, column=2, rowspan=count)