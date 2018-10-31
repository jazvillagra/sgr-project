import model
from model import Model
from abc import ABC
class Organizacion(Model):
  sucursales = []
  def __init__(self, nombre, rubro, sucursales):
    self.nombre = nombre
    self.rubro = rubro
    self.sucursales.append(sucursales)

  def create(self):
    print("Este metodo se encargara de cargar la organizacion en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la organizacion en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de organizaciones en la base de datos")
  def getOne(self, nombre):
    print("Este metodo devolvera las entradas de organizaciones con el nombre de la organizacion especificada")
  def delete(self, nombre):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el nombre especificado")
