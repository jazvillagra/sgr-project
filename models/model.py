from abc import ABC, ABCMeta, abstractmethod, abstractproperty
from ZODB import FileStorage, DB
import json, persistent

class Model(ABC, persistent.Persistent):

  #Propiedad abstracta 
  @property
  @abstractmethod
  def clave(self):
    pass

  @clave.setter
  @abstractmethod
  def clave(self, value):
    self._clave_setter_(value)
  
  @abstractmethod
  def _clave_setter_(self, value):
    pass
  
  @clave.getter
  @abstractmethod
  def clave(self):
    return 
  
  #Retorna todas las instancias del modulo almacenadas en la base de datos
  @abstractmethod
  def getAll(self):
    recursos = self.root[self.clave]
    return recursos
  #Crea una nueva instancia del modulo en la base de datos  
  @abstractmethod
  def create(self):
    recursos = self.root[self.clave]
    idx = len(recursos)
    recursos.append(self)
    return idx
  #Elimina una instancia del modulo en la base de datos
  @abstractmethod
  def delete(self):
    pass
