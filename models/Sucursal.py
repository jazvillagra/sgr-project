import json, transaction

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
      #Para mantener el indice al crear nuevas sucursales, se retorna el largo de la lista/array
      idx_sucursales = len(sucursales)
    else:
      sucursal = json.loads(self.a_json)
      sucursales = [sucursal]
      root.sucursales = json.dumps(sucursales)
      #Si todavia no existen sucursales, se mantiene el indice en cero
      idx_sucursales = 0
    transaction.commit()
    return idx_sucursales

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

