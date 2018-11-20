from models.model import Model
class Sala(Model):
  clave = "sala"
  def getClave(self):
    return self.clave
  def __init__(self, nombre_sala, max_ocupantes, estado_sala):
    self.nombre_sala= nombre_sala
    self.max_ocupantes= max_ocupantes
    self.estado_sala= estado_sala
  def copy(self):
    return Sala(self.nombre_sala, self.max_ocupantes, self.estado_sala)