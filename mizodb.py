from ZODB import FileStorage, DB
import transaction
class MiZODB(object):
  def __init__(self, archivo):
    self.storage = FileStorage.FileStorage(archivo)
    self.db = DB(self.storage)
    self.connection = self.db.open()
    self.root = self.connection.root()
  def close(self):
    self.connection.close()
    self.db.close()
    self.storage.close()