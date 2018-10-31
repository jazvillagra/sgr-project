from mizodb import MiZODB, transaction
import persistent

class Model(persistent.Persistent):
  clave = ""
  def getAll(self):
    db = MiZODB('../sgr-data.fs')
    dbroot = db.root
    recursos = dbroot[self.clave]
    db.close()
    return recursos
  def create(self):
    print(self.clave)
    db = MiZODB('../sgr-data.fs')
    dbroot = db.root
    if not self.clave in dbroot.keys():
      dbroot[self.clave] = []
      transaction.commit()
    else:
      recursos = dbroot[self.clave]
      idx = len(recursos)
      recursos[self.clave] = self
    return idx
  def delete(self):
    pass
