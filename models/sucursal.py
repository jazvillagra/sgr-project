import transaction
from models.model import Model
class Sucursal(Model):
  salas = []
  clave="sucursal"
  def getClave(self):
    return self.clave

  #Inicializa datos de la sucursal
  def __init__(self, pais, ciudad, direccion, estado, salas):
    self.pais= pais
    self.ciudad= ciudad
    self.direccion= direccion
    self.estado= estado
    self.salas = salas
  def copy(self):
    return Sucursal(self.pais, self.ciudad, self.direccion, self.estado, self.salas)