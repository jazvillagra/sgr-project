from tkinter import Frame, Label, Button, END, StringVar, Radiobutton
from views.entry import Entry
from tkinter.messagebox import showinfo
from controllers.reunion_controller import ReunionController
from controllers.sala_controller import SalaController
from datetime import datetime, date, time, timedelta
#Global variables
global entry
global reunion_controller
global sala_controller
reunion_controller = ReunionController()
sala_controller = SalaController()
entry = Entry()

class ReunionView:
  def vista_agendar_reunion_callback(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=400, columnspan=400)

    Label(frame, text="Detalle:", width=20).grid(row=1, column=2)
    detalle_reunion = entry.add_entry(frame)
    detalle_reunion.config(width=50)
    detalle_reunion.grid(row=1, column=3, columnspan=3)

    Label(frame, text="Organizador:", width=20).grid(row=2, column=2)
    organizador= entry.add_entry(frame)
    organizador.grid(row=2, column=3, columnspan=3)

    Label(frame, text="Rol del organizador:", width=20).grid(row=3, column=2)
    rol_organizador= entry.add_entry(frame)
    rol_organizador.grid(row=3, column=3, columnspan=3)

    Label(frame, text="Cant. participantes:", width=20).grid(row=4, column=2)
    cant_participantes= entry.add_entry(frame)
    cant_participantes.grid(row=4, column=3, columnspan=3)

    Label(frame, text='Fecha realizacion:', width=20).grid(row=5, column=2)
    dia = entry.add_entry(frame)
    dia.config(width=10)
    dia.insert(END, "DD")
    dia.grid(row=5, column=3)
    mes = entry.add_entry(frame)
    mes.config(width=10)
    mes.insert(END, "MM")
    mes.grid(row=5, column=4)
    anho = entry.add_entry(frame)
    anho.config(width=10)
    anho.grid(row=5, column=5)
    anho.insert(END, "AAAA")
    fecha_realizacion = anho.get() + "-" + mes.get() + "-" + dia.get()
    sgte_btn = Button(frame, text="Siguiente", activeforeground="black", width=20,
                              command=lambda: self.agregar_datos_callback(frame, detalle_reunion.get().upper(), organizador.get().upper(), rol_organizador.get().upper(),
                                                                          int(cant_participantes.get()), fecha_realizacion))
    sgte_btn.grid(row=6, column=2)


  def agregar_datos_callback(self, frame, detalle, organizador, rol_organizador, cant_participantes, fecha_realizacion):
    msg_titulo = "Mensaje"
    sala_reunion = ""
    Label(frame, text='Hora Inicio:', width=20).grid(row=7, column=2)
    hora_init= entry.add_entry(frame)
    hora_init.config(width=10)
    hora_init.insert(END, "HH")
    hora_init.grid(row=7, column=3)
    mins_init = entry.add_entry(frame)
    mins_init.config(width=10)
    mins_init.insert(END, "MM")
    mins_init.grid(row=7, column=4)
    Label(frame, text='Hora Finalización:', width=20).grid(row=8, column=2)
    hora_fin = entry.add_entry(frame)
    hora_fin.config(width=10)
    hora_fin.insert(END, "HH")
    hora_fin.grid(row=8, column=3)
    mins_fin = entry.add_entry(frame)
    mins_fin.config(width=10)
    mins_fin.insert(END, "MM")
    mins_fin.grid(row=8, column=4)
    Label(frame, text="Elegir sala:", width=20).grid(row=9, column=2)
    row_count = 10
    while not sala_reunion:
      cont = -1
      while cont < 0:
        salas_disponibles = sala_controller.listar_salas_disponibles_por_cantidad_participantes(cant_participantes)
        for i in salas_disponibles:
          cont += 1
          var = StringVar()
          var.set(Radiobutton(frame, text=i.nombre_sala, variable=var, value="Habilitada").grid(row=row_count, column=3))
          row_count += 1
        if (cont < 0):
          showinfo(msg_titulo, "No hay salas disponibles para la cantidad de participantes seleccionada.\nPor favor, intente nuevamente")
      hora_inicio = hora_init.get()+":"+mins_init.get()
      hora_finalizacion = hora_fin.get()+":"+mins_fin.get()
      estado_reunion = "Pendiente"
      sala_reunion = var.get()
      agendar_btn = Button(frame, text="Siguiente", activeforeground="black", width=20, command=lambda: self.agendar_reunion_callback(detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, hora_inicio, hora_finalizacion))
      agendar_btn.grid(row=row_count, column=2)

  def agendar_reunion_callback(self, detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, hora_inicio, hora_finalizacion):
    msg_titulo = "Mensaje"
    try:
      fecha_registro = datetime.now()
      if reunion_controller.agendar_reunion_unica(detalle, organizador, rol_organizador, cant_participantes, sala_reunion,
                                               estado_reunion, fecha_realizacion, fecha_registro,
                                               hora_inicio, hora_finalizacion):
        showinfo(msg_titulo, "La sala se guardo existosamente")
    except ValueError or TypeError:
      showinfo(msg_titulo, "No se pudo guardar la sala, por favor intente nuevamente")