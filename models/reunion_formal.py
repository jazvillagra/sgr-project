from reunion import Reunion
#Reunion formal: toda reunion previamente agendada
class ReunionFormal(Reunion):
  def __init__(self, fecha_registro, hora_inicio, hora_finalizacion, **kwargs):
    super().__init__(**kwargs)
    self.fecha_registro= fecha_registro
    self.hora_inicio= hora_inicio
    self.hora_finalizacion= hora_finalizacion
