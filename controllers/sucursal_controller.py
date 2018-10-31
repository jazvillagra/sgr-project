import json, transaction
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
  #Agregar Sucursal nueva
  def agregar_sucursal(self):
    pass
  #Dar baja a sucursal  
  def dar_baja_sucursal(self):
    pass
  #Generar reportes de reuniones realizadas en sucursal
  def generar_reporte_reuniones_sucursal(self):
    pass
  #Listar sucursales
  def listar_sucursales(self):
    pass