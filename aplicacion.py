import persistent
from ZODB import FileStorage, DB
from mizodb import MiZODB, transaction

db = MiZODB('sgr-data.fs')
dbroot = db.root
modulos= ["empresa", "sucursal","sala", "reunion", "reunion_informal", "reunion_formal", "reunion_formal_unica", "reunion_formal_periodica"]
for i in modulos:
  try:
    print(i)
    if not str(i) in dbroot:
      dbroot[i] = {} 
  except KeyError:
    print("La clave es invalida")
for key in dbroot.keys():
  print(key+':', dbroot[key])

class Aplicacion(persistent.Persistent):
  print("Bienvenido al SGR")
  