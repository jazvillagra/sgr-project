from reunion import Reunion
#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class ReunionInformal(Reunion):

  clave="reunion_informal"
  
  def __init__(self, duracion, **kwargs):
      self.duracion= duracion