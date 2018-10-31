from reunion import Reunion
#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class ReunionInformal(Reunion):
  def __init__(self, duracion, **kwargs):
      self.duracion= duracion
  
  def create(self):
    print("Este metodo se encargara de cargar los datos de la reunion informal en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la reunion informal en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de reuniones informales en la base de datos")
  def delete(self, detalle):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el detalle especificado")