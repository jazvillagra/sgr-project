from reunion import Reunion
#Reunion formal: toda reunion previamente agendada
#Clase abstracta
class ReunionFormal(Reunion):
  def __init__(self, fecha_registro, hora_inicio, finish_hour):
    self.fecha_registro= fecha_registro
    self.hora_inicio= hora_inicio
    self.finish_hour= finish_hour
