from reunion_formal import ReunionFormal
#Reunion formal unica: toda reunion previamente agendada que no se repite en el tiempo.
#Dura mas de 30 minutos y solo tiene fecha de inicio
class ReunionFormalUnica(ReunionFormal):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.frecuencia= 1