from tkinter import Frame, Label, Button, END, StringVar, Radiobutton, IntVar, Text
from views.entry import Entry
from tkinter.messagebox import showinfo
from controllers.reunion_controller import ReunionController
from controllers.sala_controller import SalaController
from datetime import datetime, date, time, timedelta
#Global variables
global entry
global reunion_controller
global sala_controller
global msg_titulo
msg_titulo = "Mensaje"
reunion_controller = ReunionController()
sala_controller = SalaController()
entry = Entry()

class ListarReunionesView:
  def listar_reuniones_unicas_callback(self, ventana_principal, frame):
    lista_reuniones = reunion_controller.listar_reuniones_unicas()
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=200, columnspan=200)
    lista = Text(frame)
    count = 0
    for reu in lista_reuniones:
      count += 1
      lista.insert(END, "* Detalle: ", reu.detalle + "\n")
      lista.insert(END, "\t"+"Sala en que se realiza: ", reu.sala + "\n")
      lista.insert(END, "\t"+"Fecha registro: ", str(reu.fecha_registro) + "\n")
      lista.insert(END, "\t"+"Agendada para: ", str(reu.fecha_realizacion) + "\n")
      lista.insert(END, "\t"+"Hora inicio: ", str(reu.hora_inicio) + "\n")
      lista.insert(END, "\t"+"Hora finalizacion: ", str(reu.hora_finalizacion) + "\n")
    lista.grid(row=1, column=2, rowspan=count)

  def listar_reuniones_periodicas_callback(self, ventana_principal, frame):
    lista_reuniones = reunion_controller.listar_reuniones_periodicas()
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=200, columnspan=200)
    lista = Text(frame)
    count = 0
    for reu in lista_reuniones:
      count += 1
      lista.insert(END, "* Detalle: ", reu.detalle + "\n")
      lista.insert(END, "\t"+"Sala en que se realiza: ", reu.sala + "\n")
      lista.insert(END, "\t"+"Fecha registro: ", str(reu.fecha_registro) + "\n")
      lista.insert(END, "\t"+"Agendada para: ", str(reu.fecha_realizacion) + "\n")
      lista.insert(END, "\t"+"Hora inicio: ", str(reu.hora_inicio) + "\n")
      lista.insert(END, "\t"+"Hora finalizacion: ", str(reu.hora_finalizacion) + "\n")
      lista.insert(END, "\t"+"Fecha de finalizacion: ", str(reu.fecha_finalizacion) + "\n")
      lista.insert(END, "\t"+"Frecuencia: ", str(reu.frecuencia) + "\n\n")
    lista.grid(row=1, column=2, rowspan=count)
