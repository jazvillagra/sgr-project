from abc import ABCMeta, abstractmethod
from ZODB import FileStorage, DB
import json, persistent

class Model(ABCMeta, persistent.Persistent):
  storage = FileStorage.FileStorage("coworking-data.fs")
  db = DB(storage)
  connection = db.open()
  root = connection.root
  tabla = []
  @classmethod
  def getAll(self):
    recursos = self.root[self.tabla]
    return recursos
    
  @classmethod
  def create(self):
    pass
  @classmethod
  def update(self):
    pass
  @classmethod
  def delete(self):
    pass
  @classmethod
  def get_one(self):
    pass