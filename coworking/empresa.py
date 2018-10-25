from coworking import Coworking

class Empresa(Coworking):
  #Inicializa datos de empresa
  def __init__(self, nombre, rubro, cant_sucursales):
    self.nombre= nombre
    self.rubro= rubro
    self.cant_sucursales= cant_sucursales

class Sucursal():
      #Inicializa datos de la sucursal
  def __init__(self, pais, ciudad, direccion, salas, estado):
    self.pais= pais
    self.ciudad= ciudad
    self.salas= salas
    self.estado= estado

  #Agregar Sucursal nueva
  def agregar_sucursal(self):
    pass
  #Dar baja a sucursal  
  def dar_baja_sucursal(self, estado):
    pass
  #Generar reportes de reuniones realizadas en sucursal
  def generar_reporte_reuniones_sucursal(self):
    pass

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