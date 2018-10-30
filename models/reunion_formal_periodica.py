
from reunion_formal import ReunionFormal
#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class FormalPeriodicMeeting(ReunionFormal):
  def __init__(self, begin_date, finish_date, frecuencia):
      self.begin_date= begin_date
      self.finish_date= finish_date
      self.frecuencia= frecuencia
  def edit_frequence(self, frecuencia):
      pass
  def change_finish_date(self, finish_date):
      pass
  