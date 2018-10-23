import persistent, transaction

class Coworking(persistent.Persistent):
  pass

class Empresa(Coworking):
  pass

class Sucursal(Empresa):
    def agregar_sucursal(self):
      pass
