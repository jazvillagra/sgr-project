from tkinter import Frame, Label, Button, END, StringVar, Radiobutton, IntVar, Text, DISABLED
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

class AgendarReunionView:
  def vista_agendar_reunion_callback(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=400, columnspan=400)
    frame.config(width=900)

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

    sgte_btn = Button(frame, text="Siguiente", activeforeground="black", width=20,
                              command=lambda: self.agregar_datos_callback(ventana_principal, frame, detalle_reunion.get().upper(), organizador.get().upper(), rol_organizador.get().upper(),
                                                                          int(cant_participantes.get()), anho.get() + "-" + mes.get() + "-" + dia.get()))
    sgte_btn.grid(row=6, column=2)


  def agregar_datos_callback(self, ventana, frame, detalle, organizador, rol_organizador, cant_participantes, fecha_realizacion):
    frame.grid_remove()
    frame.destroy()
    frame = Frame(ventana)
    frame.grid(row=1, column=2, rowspan=400, columnspan=400)
    frame.config(width=900)
    sala_reunion = ""
    Label(frame, text='Hora Inicio:', width=20).grid(row=1, column=2)
    hora_init= entry.add_entry(frame)
    hora_init.config(width=10)
    hora_init.insert(END, "HH")
    hora_init.grid(row=1, column=3)
    mins_init = entry.add_entry(frame)
    mins_init.config(width=10)
    mins_init.insert(END, "MM")
    mins_init.grid(row=1, column=4)
    Label(frame, text='Hora Finalización:', width=20).grid(row=2, column=2)
    hora_fin = entry.add_entry(frame)
    hora_fin.config(width=10)
    hora_fin.insert(END, "HH")
    hora_fin.grid(row=2, column=3)
    mins_fin = entry.add_entry(frame)
    mins_fin.config(width=10)
    mins_fin.insert(END, "MM")
    mins_fin.grid(row=2, column=4)
    Label(frame, text="Salas disponibles:", width=20).grid(row=3, column=2)
    row_count = 10
    cont = -1
    lista_salas = Text(frame)
    while cont < 0:
      salas_disponibles = sala_controller.listar_salas_disponibles_por_cantidad_participantes(cant_participantes)
      for i in salas_disponibles:
        cont += 1
        lista_salas.insert(END,"* "+i.nombre_sala+"\n")
        row_count += 1
      if (cont < 0):
        showinfo(msg_titulo, "No hay salas disponibles para la cantidad de participantes seleccionada.\nPor favor, intente nuevamente")
        cont+=1
        self.vista_agendar_reunion_callback(ventana, frame)
      else:
        lista_salas.config(width=20, state=DISABLED)
        lista_salas.grid(row=row_count, column=3)
        row_count+=2
    row_count += 1
    Label(frame, text="Elegir sala: ").grid(row=row_count, column=2)
    sala_reunion = entry.add_entry(frame)
    sala_reunion.grid(row=row_count, column=3)
    row_count += 1
    estado_reunion = "Pendiente"
    sgte_btn = Button(frame, text="Siguiente", activeforeground="black", width=20, command=lambda: self.sel_tipo_reu_callback(ventana, frame, detalle, organizador, rol_organizador, cant_participantes, sala_reunion.get(), estado_reunion, fecha_realizacion, hora_init.get()+":"+mins_init.get(), hora_fin.get()+":"+mins_fin.get()))
    sgte_btn.grid(row=row_count, column=2)

  def sel_tipo_reu_callback(self, ventana, frame, detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, hora_inicio, hora_finalizacion):
    print("Sala:", sala_reunion)
    frame.grid_remove()
    frame.destroy()
    frame = Frame(ventana)
    frame.grid(row=1, column=2, rowspan=400, columnspan=400)
    frame.config(width=900)
    Label(frame, text="Tipo de reunión:", width=20).grid(row=1, column=2)
    var = IntVar()
    var.set(1)
    var.set(Radiobutton(frame, text="Única", variable=var, value=1).grid(row=1, column=3))
    var.set(Radiobutton(frame, text="Periodica", variable=var, value=2).grid(row=1, column=4))
    sgte_btn = Button(frame, text="Siguiente", activeforeground="black", width=20, command=lambda: self.agendar_callback(frame, detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, hora_inicio, hora_finalizacion, int(var.get())))
    sgte_btn.grid(row=2, column=2)
  def agendar_callback(self, frame, detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, hora_inicio, hora_finalizacion, tipo):
    fecha_registro = datetime.now()
    if tipo == 1:
      self.agendar_reunion_unica_callback(detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion)
    elif tipo == 2:
      Label(frame, text="Ultima fecha de realización: ", width=30).grid(row=3, column=2)
      dia = entry.add_entry(frame)
      dia.config(width=10)
      dia.insert(END, "DD")
      dia.grid(row=3, column=3)
      mes = entry.add_entry(frame)
      mes.config(width=10)
      mes.insert(END, "MM")
      mes.grid(row=3, column=4)
      anho = entry.add_entry(frame)
      anho.config(width=10)
      anho.grid(row=3, column=5)
      anho.insert(END, "AAAA")
      Label(frame, text="Frecuencia (dias):", width=30).grid(row=4, column=2)
      frecuencia = entry.add_entry(frame)
      frecuencia.grid(row=4, column=3)

      agendar_reunion_btn = Button(frame, text="Agendar", activeforeground="black", width=20, command=lambda: self.agendar_reunion_periodica_callback(detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion, anho.get() + "-" + mes.get() + "-" + dia.get(), int(frecuencia.get())))
      agendar_reunion_btn.grid(row=6, column=2)


  def agendar_reunion_unica_callback(self, detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion):
    if reunion_controller.agendar_reunion_unica(detalle, organizador, rol_organizador, cant_participantes, sala_reunion,
                                                estado_reunion, fecha_realizacion, fecha_registro,
                                                hora_inicio, hora_finalizacion):
      showinfo(msg_titulo, "La reunion se guardo existosamente")

  def agendar_reunion_periodica_callback(self,detalle, organizador, rol_organizador, cant_participantes, sala_reunion, estado_reunion, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion, fecha_finalizacion, frecuencia):
    print("Detalle: ", detalle)
    print("\nOrganizador: ", organizador)
    print("\nRol: ", rol_organizador)
    print("\nCant part: ", cant_participantes)
    print("\nSala: ", sala_reunion)
    print("\nEstado reu: ", estado_reunion)
    print("\nFecha realizacion: ", fecha_realizacion)
    print("\nFecha registro: ", fecha_registro)
    print("\nHora inicio: ", hora_inicio)
    print("\nHora inicio: ", hora_finalizacion)
    print("\nHora inicio: ", fecha_finalizacion)
    print("\nHora inicio: ", frecuencia)
    if reunion_controller.agendar_reunion_periodica(detalle, organizador, rol_organizador, cant_participantes, sala_reunion,
                                                estado_reunion, fecha_realizacion, fecha_registro,
                                                hora_inicio, hora_finalizacion, fecha_realizacion, fecha_finalizacion, frecuencia):
      showinfo(msg_titulo, "La reunion se guardo existosamente")