from reunion_formal import ReunionFormal
#Reunion formal unica: toda reunion previamente agendada que no se repite en el tiempo.
#Dura mas de 30 minutos y solo tiene fecha de inicio
class ReunionFormalUnica(ReunionFormal):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.frecuencia= 1
  
  def create(self):
    print("Este metodo se encargara de cargar los datos de la reunion formal unica en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la reunion formal unica en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de reuniones formales unicas en la base de datos")
  def delete(self, detalle):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el detalle especificado")