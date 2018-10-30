import json, transaction, persistent
from coworking import Coworking

class Empresa(Coworking):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro):
    self.nombre= nombre
    self.rubro= rubro

class Organizacion():
  def __init__(self, cant_sucursales):
    self.cant_sucursales= cant_sucursales      

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
  def agregar_sala(self):
    pass
  #Dar baja a sala  
  def dar_baja_sala(self, estado):
    pass
  #Generar reportes de reuniones realizadas en una sala de una sucursal
  def generar_reporte_reuniones_sala(self):
    pass