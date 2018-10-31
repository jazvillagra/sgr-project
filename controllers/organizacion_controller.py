class OrganizacionController:
  sucursales = []
  def __init__(self, sucursales, **kwargs):
    super().__init__(**kwargs)
    self.sucursales.append(sucursales)
  #Agregar organizacion a empresa
  def agregar_organizacion(self):
    pass
  #Editar datos de organizacion
  def editar_organizacion(self):
    pass
  def ver_cantidad_de_sucursales(self):
    return len(self.sucursales)
