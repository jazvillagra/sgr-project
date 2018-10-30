import json, transaction
class Sala:
  def __init__(self, nombre_sala, max_ocupantes, estado_sala):
    self.nombre_sala= nombre_sala
    self.max_ocupantes= max_ocupantes
    self.estado_sala= estado_sala
  #Agregar sala nueva
  def agregar_sala(self, connection):
    root = connection.root
    if 'salas' in connection.root():
      salas = json.loads(root.salas)
      sala = json.loads(self.a_json)
      salas.append(sala)
      root.salas = json.dumps(sala)
      #Para mantener el indice al agregar nuevas salas, se devuelve el tamaño de la lista/array
      idx_salas= len(salas)
    else:
      sala = json.loads(self.a_json)
      salas = [sala]
      root.salas = json.dumps(salas)
      #Si todavia no existen salas, el indice se mantiene en cero
      idx_salas = 0
    transaction.commit()
    return idx_salas
    
  #Dar baja a sala  
  def dar_baja_sala(self, estado):
    pass
  #Generar reportes de reuniones realizadas en una sala de una sucursal
  def generar_reporte_reuniones_sala(self):
    pass
  #Listar salas de una sucursal
  def listar_salas(self):
    pass
  def a_json(self):
    return "{\"nombre_sala\": \""+self.nombre_sala+"\", \"max_ocupantes\": \""+self.max_ocupantes+"\", \"estado_sala\": \""+self.estado_sala+"}"
