import json, transaction
from coworking import Coworking

class Empresa(Coworking):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.nombre= nombre
    self.rubro= rubro

class Organizacion():
  #Inicializa datos de la organizacion
  def __init__(self, cant_sucursales):
    self.cant_sucursales= cant_sucursales
  #Agregar organizacion
  def agregar_organizacion(self, connection):
    pass

class Sucursal():
  #Inicializa datos de la sucursal
  def __init__(self, pais, ciudad, direccion, salas, estado):
    self.pais= pais
    self.ciudad= ciudad
    self.direccion= direccion
    self.salas= salas
    self.estado= estado
  #Agregar Sucursal nueva
  def agregar_sucursal(self, connection):
    root = connection.root
    if 'sucursales' in connection.root():
      sucursales = json.loads(root.sucursales)
      sucursal = json.loads(self.a_json)
      sucursales.append(sucursal)
      root.sucursales = json.dumps(sucursales)
    else:
      sucursal = json.loads(self.a_json)
      sucursales = [sucursal]
      root.sucursales = json.dumps(sucursales)
    transaction.commit()
  #Dar baja a sucursal  
  def dar_baja_sucursal(self, estado):
    pass
  #Generar reportes de reuniones realizadas en sucursal
  def generar_reporte_reuniones_sucursal(self):
    pass
  #Listar sucursales
  def listar_sucursales(self, connection):
    pass
  def a_json(self):
    return "{\"pais\": \""+self.pais+"\", \"ciudad\": \""+self.ciudad+"\", \"direccion\": \""+self.direccion+"\", \"salas\": \""+self.salas+"\", \"estado\": \""+self.estado+"\"}"

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
    else:
      sala = json.loads(self.a_json)
      salas = [sala]
      root.salas = json.dumps(salas)
    transaction.commit()
    pass
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
