from tkinter import Frame, Label, StringVar, Radiobutton, Button, Text, END
from tkinter.messagebox import showinfo
from views.entry import Entry
from controllers.sala_controller import SalaController
#Global variables
global controller
global Entry
entry = Entry()
controller = SalaController()
class SalaView:

# Crea frame para agregar sala
  def vista_agregar_sala_callback(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=400, columnspan=400)
    Label(frame, text="Nombre Sala:", width=20).grid(row=1, column=2)
    nombre_sala = entry.add_entry(frame)
    nombre_sala.grid(row=1, column=3)
    Label(frame, text="Max_ocupantes:", width=20).grid(row=2, column=2)
    max_ocupantes = entry.add_entry(frame)
    max_ocupantes.grid(row=2, column=3)
    Label(frame, text="Estado de sala:", width=20).grid(row=3, column=2)
    var = StringVar()
    var.set(1)
    var.set(Radiobutton(frame, text="Habilitada", variable=var, value="Habilitada").grid(row=3, column=3))
    var.set(Radiobutton(frame, text="Inhabilitada", variable=var, value="Inhabilitada").grid(row=3, column=4))

    guardar_sala_btn = Button(frame, text="Guardar", activeforeground="black", width=20,
                              command=lambda: self.agregar_sala_callback(nombre_sala.get().upper(),
                                                                         int(max_ocupantes.get()), var.get()))
    guardar_sala_btn.grid(row=4, column=2)

  def agregar_sala_callback(self, nombre_sala, max_ocupantes, estado_sala):
    msg_titulo = "Mensaje"
    if controller.agregar_sala(nombre_sala, max_ocupantes, estado_sala):
        showinfo(msg_titulo, "La sala se guardo existosamente")
    else:
        showinfo(msg_titulo, "No se pudo guardar la sala, por favor intente nuevamente")

  def vista_lista_salas_callback(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=200, columnspan=200)
    lista = Text(frame)
    lista_salas = controller.listar_salas()
    count = 0
    for i in lista_salas:
      count+=1
      lista.insert(END, "Nombre sala: "+ i.nombre_sala + "\n")
      lista.insert(END, "Max. ocupantes: "+ str(i.max_ocupantes) + "\n")
      lista.insert(END, "Estado de sala: "+ i.estado_sala + "\n\n")
    lista.grid(row=1, column=2, rowspan=count)
