from abc import ABC, abstractmethod
class Empresa(ABC):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.__nombre = nombre
    self.__rubro = rubro
  
  def create(self):
    print("Este metodo se encargara de cargar la empresa en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la empresa en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de empresas en la base de datos")
  def getOne(self, nombre):
    print("Este metodo devolvera las entradas con el nombre de la empresa especificada")
  def delete(self, nombre):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el nombre especificado")