
class Organizacion():
  sucursales = []
  clave="organizacion"
  def __init__(self, nombre, sucursales, **kwargs):
    super().__init__(**kwargs)
    self.nombre = nombre
    self.sucursales.append(sucursales)
