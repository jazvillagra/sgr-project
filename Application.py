import sched, time, persistent, coworking
from ZODB import FileStorage, DB

storage = FileStorage.FileStorage("coworking-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root

class Application(persistent.Persistent):
  print("Bienvenido al SGR")
  print("Por favor, elija la sucursal a la cual desea acceder: ")
  
