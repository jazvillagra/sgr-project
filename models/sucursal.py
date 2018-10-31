import json, transaction
from model import Model
class Sucursal(Model):
  salas = []
  clave="sucursal"

  #Inicializa datos de la sucursal
  def __init__(self, pais, ciudad, direccion, estado, salas):
    self.pais= pais
    self.ciudad= ciudad
    self.direccion= direccion
    self.estado= estado
    self.salas.append(salas)