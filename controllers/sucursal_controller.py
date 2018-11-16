from models.sucursal import Sucursal
class SucursalController:
  #Agregar Sucursal nueva
  def agregar_sucursal(self, pais, ciudad, direccion, estado, salas):
    sucursal = Sucursal(pais, ciudad, direccion, estado, salas)
    return sucursal
  #Dar baja a sucursal  
  def dar_baja_sucursal(self):
    pass
  #Generar reportes de reuniones realizadas en sucursal
  def generar_reporte_reuniones_sucursal(self):
    pass
  #Listar sucursales
  def listar_sucursales(self):
    return Sucursal.getAll(Sucursal)