from reunion import Reunion
#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class ReunionInformal(Reunion):
  def __init__(self, duracion, **kwargs):
      self.duracion= duracion
  def begin_informal_meeting(self, hora_inicio):
      pass
  def finish_informal_meeting(self, duracion):
      pass
