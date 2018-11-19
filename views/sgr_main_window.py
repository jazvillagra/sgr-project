from tkinter import * 
class Application(Frame):
  def __init__(self):
    ventana_principal = Tk()
    ventana_principal.title('SGR Project')
    ventana_principal.geometry("400x200")
    #ventana.resizable(width=FALSE, height=FALSE)
    widget = Label(text='Bienvenido al SGR!')
    agendar_reu_btn = Button(ventana_principal,text="Agendar reunión", relief=RIDGE, activebackground="white", activeforeground="black")
    agendar_reu_btn.grid(row=1, column=1)
    listar_reu_btn = Button(ventana_principal,text="Listar reuniones", relief=RIDGE, activebackground="white", activeforeground="black")
    listar_reu_btn.grid(row=2, column=1)
    ventana_principal.mainloop()

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


