import transaction
from model import Model
class Sucursal(Model):
  salas = []
  #Inicializa datos de la sucursal
  def __init__(self, pais, ciudad, direccion, estado, salas):
    self.pais= pais
    self.ciudad= ciudad
    self.direccion= direccion
    self.estado= estado
    self.salas.append(salas)
   
  def create(self):
    print("Este metodo se encargara de cargar los datos de la sucursal en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la sucursal en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de sucursales en la base de datos")
