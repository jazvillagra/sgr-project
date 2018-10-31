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
    db = MiZODB('../sgr-data.fs')
    dbroot = db.root
    recursos = dbroot[self.clave]
    idx = len(recursos)
    recursos.append(self)
    return idx

  
  def delete(self):
    pass
