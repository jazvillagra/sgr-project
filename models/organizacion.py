from models.model import Model
class Organizacion(Model):
  sucursales = []
  clave="organizacion"
  def __init__(self, nombre, rubro, sucursales):
    self.nombre = nombre
    self.rubro = rubro
    self.sucursales.append(sucursales)
