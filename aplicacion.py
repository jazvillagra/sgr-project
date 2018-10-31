import persistent
from ZODB import FileStorage, DB

storage = FileStorage.FileStorage("coworking-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root
print("Root connection assigned")
modulos= ["empresa", "sucursal","sala", "reunion", "reunion_informal", "reunion_formal", "reunion_formal_unica", "reunion_formal_periodica"]
for i in modulos:
  try:
    print(i)
    if not root.has_key(i):
      root[i] = {}
  except KeyError:
    print("La clave es invalida")

class Aplicacion(persistent.Persistent):
  print("Bienvenido al SGR")
  