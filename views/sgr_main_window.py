from tkinter import *
from views import vista_sala



class Application(Frame):
  def __init__(self):
    ventana_principal = Tk()
    ventana_principal.title('SGR Project')
    ventana_principal.geometry("400x200")
    #ventana.resizable(width=FALSE, height=FALSE)
    agregar_sala_btn= Button(ventana_principal,text="Agregar Nueva Sala", relief=RIDGE, activebackground="white", activeforeground="black", width=20, command=self.mostrar_vista_sala).pack()
    agregar_sala_btn.grid(row=1, column=1)
    listar_salas_btn= Button(ventana_principal,text="Listar salas", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_salas_btn.grid(row=2, column=1)
    agendar_reu_btn = Button(ventana_principal,text="Agendar reunión", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    agendar_reu_btn.grid(row=3, column=1)
    listar_reu_btn = Button(ventana_principal,text="Listar reuniones", relief=RIDGE, activebackground="white", activeforeground="black", width=20)
    listar_reu_btn.grid(row=4, column=1)
    ventana_principal.mainloop()

    def mostrar_vista_sala(self):
      vista_sala.mainloop()

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


