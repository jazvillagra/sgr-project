import persistent, transaction
from persistent.mapping import PersistentMapping
from model import Model
class Reunion(Model, persistent.Persistent):

  def __init__(self, detalle, organizador, organizador_rol, cant_participantes, estado, fecha_realizacion):
    self.detalle = detalle
    self.organizador = organizador
    self.organizador_rol = organizador_rol
    self.cant_participantes = cant_participantes
    self.estado = estado
    self.fecha_realizacion = fecha_realizacion
  #Agendar reunion
  def agendar_reunion(self, detalle, organizador, organizador_rol, cant_participantes, estado, fecha_realizacion):
    pass
  #Cancelar reunion
  def cancelar_reunion(self):
    pass
  #Reagendar reunion
  def reagendar_reunion(self):
    pass