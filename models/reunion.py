import persistent, transaction
from abc import ABC, abstractmethod
from model import Model
class Reunion(ABC, Model):

  def __init__(self, detalle, organizador, organizador_rol, cant_participantes, estado, fecha_realizacion):
    self.detalle = detalle
    self.organizador = organizador
    self.organizador_rol = organizador_rol
    self.cant_participantes = cant_participantes
    self.estado = estado
    self.fecha_realizacion = fecha_realizacion