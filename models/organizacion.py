from models.model import Model
class Organizacion(Model):
  sucursales = []
  clave="organizacion"
  def getClave(self):
    return self.clave

  def __init__(self, nombre, rubro, sucursales):
    self.nombre = nombre
    self.rubro = rubro
    self.sucursales = sucursales
  def copy(self):
    return Organizacion(self.nombre, self.rubro, self.sucursales)