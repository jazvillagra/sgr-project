import persistent, transaction

class Coworking(persistent.Persistent):
  pass

class Empresa(Coworking):
  pass

class Sucursal(Empresa):
    
    def agregar_sucursal(self):
      pass
    
    def editar_sucursal(self, pais, ciudad, direccion, salas, estado):
      pass
    
    def dar_baja_sucursal(self, estado):
      pass
    
    def generar_reporte_reuniones_sucursal(self):
      pass