from abc import ABC, abstractmethod
class Empresa(ABC):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.__nombre = nombre
    self.__rubro = rubro

class Organizacion(Empresa):
  sucursales = []
  def __init__(self, sucursales, **kwargs):
    super().__init__(**kwargs)
    self.sucursales.append(sucursales)