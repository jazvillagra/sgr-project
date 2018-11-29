from tkinter import *
from controllers.sala_controller import SalaController
#
# class VistaSalas(Frame):
#   def __init__(self):
#     ventana_salas = Tk()
#     ventana_salas.title('SGR Project')
#     ventana_salas.geometry("400x200")

global sala_controller
sala_controller = SalaController()

class Application(Frame):
  def __init__(self):
    ventana_principal = Tk()
    ventana_principal.title('SGR Project')
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=100)
    agregar_sala_btn= Button(ventana_principal,text="Agregar Nueva Sala", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agregar_sala_btn.grid(row=1, column=1)
    agregar_sala_btn.config(comman= lambda: self.vista_agregar_sala(ventana_principal, frame))
    listar_salas_btn= Button(ventana_principal,text="Listar salas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_salas_btn.grid(row=2, column=1)
    listar_salas_btn.config(comman= lambda: self.vista_lista_salas(ventana_principal, frame))
    agendar_reu_btn = Button(ventana_principal,text="Agendar reunión", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agendar_reu_btn.grid(row=3, column=1)
    listar_reu_btn = Button(ventana_principal,text="Listar reuniones", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_reu_btn.grid(row=4, column=1)
    ventana_principal.mainloop()

  def vista_agregar_sala(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=100)
    Label(frame, text = "Nombre Sala:", width=20).grid(row=1, column=2)
    nombre_sala = Entry(frame, width=20)
    nombre_sala.grid(row=1, column=3)
    Label(frame, text = "Max_ocupantes:", width=20).grid(row=2, column=2)
    max_ocupantes = Entry(frame, width=20)
    max_ocupantes.grid(row=2, column=3)
    Label(frame, text = "Estado de sala:", width=20).grid(row=3, column=2)
    var = IntVar()
    var.set(1)
    var.set(Radiobutton(frame, text="Habilitada", variable=var, value=1).grid(row=3, column=3))
    var.set(Radiobutton(frame, text="Inhabilitada", variable=var, value=2).grid(row=3, column=4))

    guardar_sala_btn = Button(frame, text="Guardar", activeforeground="black", width=20, command= lambda: self.agregar_sala_callback(frame, nombre_sala, max_ocupantes, var))
    guardar_sala_btn.grid(row=4, column=2)

  def vista_lista_salas(self, ventana_principal, frame):
    frame.destroy()
    frame = Frame(ventana_principal)
    frame.grid(row=1, column=2, rowspan=100)
    lista = Text(frame)
    lista_salas= sala_controller.listar_salas()
    count = 0
    for i in lista_salas:
      count+=1
      lista.insert(END, "Nombre sala: "+ i.nombre_sala + "\n")
      lista.insert(END, "Max. ocupantes: "+ str(i.max_ocupantes) + "\n")
      lista.insert(END, "Estado de sala: "+ i.estado_sala + "\n\n")
    lista.grid(row=1, column=2, rowspan=count)

  def agregar_sala_callback(self, frame, nombre_sala, max_ocupantes, var):
    agregado = FALSE
    if var.get() == 1:
      estado_sala = "Habilitada"
    else:
      estado_sala = "Inhabilitada"
    msg = Text(frame)
    if sala_controller.agregar_sala(nombre_sala.get().upper(), int(max_ocupantes.get()), estado_sala):
      msg.insert(END, "La sala se guardo exitosamente")
    else:
      msg.insert(END, "No se pudo guardar la sala, por favor intente nuevamente")
    msg.grid(row=4, column=1)
def main():
  sgr_project = Application()
  return 0

# Mediante el atributo __name__ tenemos acceso al nombre de un
# un módulo. Python utiliza este atributo cuando se ejecuta
# un programa para conocer si el módulo es ejecutado de forma
# independiente (en ese caso __name__ = '__main__') o es 
# importado:
if __name__ == '__main__':
    main()
