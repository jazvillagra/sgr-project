from models.sala import Sala
from mizodb import MiZODB
class SalaController:
  #Agregar sala nueva
  @staticmethod
  def agregar_sala(nombre_sala, max_ocupantes, estado_sala):
    sala = Sala(nombre_sala, max_ocupantes, estado_sala)
    return sala.create()
  #Dar baja a sala  
  def dar_baja_sala(self):
    pass
  #Generar reportes de reuniones realizadas en una sala de una sucursal
  def generar_reporte_reuniones_sala(self):
    pass
  #Listar salas de una sucursal
  def listar_salas(self):
    return Sala.getAll(Sala)