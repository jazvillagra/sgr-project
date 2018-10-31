import json, transaction
from mizodb import MiZODB, transaction
from model import Model
class Sala(Model):
  clave="sala"
  def __init__(self, nombre_sala, max_ocupantes, estado_sala):
    self.nombre_sala= nombre_sala
    self.max_ocupantes= max_ocupantes
    self.estado_sala= estado_sala
  
  