from reunion_formal_controller import ReunionFormalController
#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class ReunionFormalPeriodicaController(ReunionFormalController):
  def __init__(self, fecha_inicio, fecha_finalizacion, frecuencia, **kwargs):
      self.fecha_inicio= fecha_inicio
      self.fecha_finalizacion= fecha_finalizacion
      self.frecuencia= frecuencia
  def cambiar_frecuencia(self, frecuencia):
      pass
  def cambiar_fecha_finalizacion(self, fecha_finalizacion):
      pass
  