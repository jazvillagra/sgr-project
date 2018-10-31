import empresa 
import sched, time, persistent, transaction
from ZODB import FileStorage, DB
from ZODB.scripts import analyze

storage = FileStorage.FileStorage("coworking-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root

class Application(persistent.Persistent):
  print("Bienvenido al SGR")

# Insercion de prueba
surcursal = empresa.Sucursal("py","Asuncion","calle falsa 123", "hetaiteorekopea","iiiwenooooiiimbaejajaiiiiwenoooo")
sucursal.agregar_sucursal()
print("Insertado")

# Reconexion y muestra de datos insertados (pakebea ke no e vola)
connection.close()
db = DB(storage)
connection = db.open()
root = connection.root
print("Datos en BD: ", root.sucursales)

