from abc import ABC, abstractmethod
class Empresa(ABC):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.__nombre = nombre
    self.__rubro = rubro
  @abstractmethod
  def create(self):
    pass
  @abstractmethod
  def update(self):
    pass
  @abstractmethod
  def getAll(self):
    pass
  @abstractmethod
  def getOne(self, nombre):
    pass
  @abstractmethod
  def delete(self, nombre):
    pass