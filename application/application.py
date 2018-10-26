import sched, time, persistent
from ZODB import FileStorage, DB

storage = FileStorage.FileStorage("coworking-data.fs")
db = DB(storage)
connection = db.open()
root = connection.root

class Application(persistent.Persistent):
  print("Bienvenido al SGR")
  