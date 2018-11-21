from mizodb import MiZODB
import transaction
import persistent

class Model(persistent.Persistent):
  #getAll
  @staticmethod
  def getAll(self):
    db = MiZODB('sgr-data.fs')
    dbroot = db.root
    recursos = []
    for i in dbroot[self.getClave(self)]:
      recursos.append(i.copy())
    db.close()
    return recursos
  #createObject in DB
  def create(self):
    #print("Clave: ", self.getClave(self))
    db = MiZODB('sgr-data.fs')
    dbroot = db.root
    if not self.getClave() in dbroot.keys():
      print("Creo el slot")
      recursos = []
      recursos.append(self)
      db.root[self.getClave()] = recursos
      transaction.commit()
    else:
      print("Intenta guardar los datos")
      recursos = dbroot[self.getClave()]
      print("Clave: ", self.getClave())
      idx = len(recursos)
      recursos.append(self)
      db.root[self.getClave()] = recursos
      transaction.commit()
    db.close()
    return idx
  # getOne
  @staticmethod
  def getOne(self):
    db = MiZODB('sgr-data.fs')
    dbroot = db.root
    recursos = []
    for i in dbroot[self.getClave(self)]:
      recursos.append(i.copy())
      break
    db.close()
    return recursos
  def delete(self):
    pass
