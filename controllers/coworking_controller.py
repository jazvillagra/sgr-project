class CoworkingController:
  empresas = []
  def __init__(self, empresa):
    self.empresas.append(empresa)
  #Debe retornar la cantidad de empresas existentes
  def ver_cantidad_empresas(self):
    return len(self.empresas)