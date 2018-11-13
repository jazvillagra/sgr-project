from models.organizacion import Organizacion
class OrganizacionController:
  #Agregar organizacion a empresa
  @staticmethod
  def agregar_organizacion(nombre_organizacion, rubro, sucursales):
    organizacion = Organizacion(nombre_organizacion, rubro, sucursales)
    return Organizacion.create(organizacion)
  #Editar datos de organizacion
  def editar_organizacion(self):
    pass
  #Ver cantidad de sucursales con las que cuenta una organizacion
  def ver_cantidad_de_sucursales(self):
    pass
