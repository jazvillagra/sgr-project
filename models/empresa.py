from abc import ABCMeta, abstractmethod
class Empresa(ABCMeta):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.nombre= nombre
    self.rubro= rubro
