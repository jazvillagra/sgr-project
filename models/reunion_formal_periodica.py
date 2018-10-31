
from reunion_formal import ReunionFormal
#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class FormalPeriodicMeeting(ReunionFormal):
  def __init__(self, begin_date, finish_date, frecuencia, **kwargs):
      self.begin_date= begin_date
      self.finish_date= finish_date
      self.frecuencia= frecuencia
  def create(self):
    print("Este metodo se encargara de cargar una reunion formal periodica en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la reunion formal periodica en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de reuniones formales periodicas en la base de datos")
  def delete(self, detalle):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el detalle especificado")