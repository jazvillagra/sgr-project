from models.organizacion import Organizacion
class OrganizacionController:
  #Agregar organizacion a empresa

  def agregar_organizacion(self, nombre_organizacion, rubro, sucursales):
    organizacion = Organizacion(nombre_organizacion, rubro, sucursales)
    return organizacion.create()
  #Editar datos de organizacion
  def editar_organizacion(self):
    pass
  #Ver cantidad de sucursales con las que cuenta una organizacion
  def ver_cantidad_de_sucursales(self):
    pass
  def listar_organizaciones(self):
    return Organizacion.getAll(Organizacion)
  def traer_organizacion(self):
    return Organizacion.getOne(Organizacion)