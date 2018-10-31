from reunion_controller import ReunionController
#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class ReunionInformalController(ReunionController):
  def __init__(self, duracion, **kwargs):
    self.duracion= duracion
  def empezar_reunion_informal(self, hora_inicio):
    pass
  def terminar_reunion_informal(self, hora_finalizacion):
    pass
  def cambiar_duracion_reunion_informal(self):
    pass