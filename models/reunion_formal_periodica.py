from models.reunion_formal import ReunionFormal
#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class ReunionFormalPeriodica(ReunionFormal):
  clave="reunion_formal_periodica"
  def __init__(self, fecha_inicio, fecha_finalizacion, frecuencia, **kwargs):
      self.fehca_inicio= fecha_inicio
      self.fecha_finalizacion= fecha_finalizacion
      self.frecuencia= frecuencia
 