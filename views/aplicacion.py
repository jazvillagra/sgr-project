import persistent
from ZODB import FileStorage, DB

storage = FileStorage.FileStorage("coworking-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root
modulos = ["empresa", "sucursal","sala", "reunion", "reunion_informal", "reunion_formal", "reunion_formal_unica", "reunion_formal_periodica"]
for item in modulos:
  if not root.has_key(item):
    root[item] = {}

class Aplicacion(persistent.Persistent):
  print("Bienvenido al SGR")
  