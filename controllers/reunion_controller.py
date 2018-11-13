from models.reunion import Reunion
from models.reunion_formal import ReunionFormal
from models.reunion_formal_periodica import ReunionFormalPeriodica
from models.reunion_informal import ReunionInformal
class ReunionController:

  #Agendar reunion
  def agendar_reunion(self, detalle, organizador, organizador_rol, cant_participantes, estado, fecha_realizacion):
    pass
  #Cancelar reunion
  def cancelar_reunion(self):
    pass
  #Reagendar reunion
  def reagendar_reunion(self):
    pass
  #Cambiar frecuencia de reunion formal periodica
  def cambiar_frecuencia_reunion_formal_periodica(self, frecuencia):
    pass
  #Cambiar fecha de finalizacion de las repeticiones de una reunion
  def cambiar_fecha_finalizacion_reunion_formal_periodica(self, fecha_finalizacion):
    pass
  #Empezar una reunion informal. Esto se implementara con la interfaz grafica (se empieza con un botoncito que llame a esta accion)
  def empezar_reunion_informal(self, hora_inicio):
    pass
  #Terminar una reunion informal.Esto se implementara con la interfaz grafica (se empieza con un botoncito que llame a esta accion)
  def terminar_reunion_informal(self, hora_finalizacion):
    pass
  #Cambiar la duracion de una reunion informal 
  def cambiar_duracion_reunion_informal(self):
    pass