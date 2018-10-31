import json, transaction

from mizodb import MiZODB, transaction
from model import Model
class Sala(Model):
  def __init__(self, nombre_sala, max_ocupantes, estado_sala):
    self.nombre_sala= nombre_sala
    self.max_ocupantes= max_ocupantes
    self.estado_sala= estado_sala
  
  def create(self):
    print("Este metodo se encargara de cargar los datos de la sala en la base de datos")
  def update(self):
    print("Este metodo se encargara de actualizar los datos de la sala en la base de datos")
  def getAll(self):
    print("Este metodo devolvera todas las entradas de salas en la base de datos")
  def delete(self, nombre):
    print("Este metodo eliminara el o los objetos en la base de datos que tengan el nombre especificado")