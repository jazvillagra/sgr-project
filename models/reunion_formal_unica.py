from models.reunion_formal import ReunionFormal
#Reunion formal unica: toda reunion previamente agendada que no se repite en el tiempo.
#Dura mas de 30 minutos y solo tiene fecha de inicio
class ReunionFormalUnica(ReunionFormal):

  clave = "reunion_formal_unica"
  def getClave(self):
    return self.clave
  def __init__(self,  detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion):
    super().__init__(detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion)
    self.frecuencia= 1
  def copy(self):
    #return ReunionFormalUnica(super.__init__(detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion),self.frecuencia)
    return ReunionFormalUnica(self.detalle, self.organizador, self.organizador_rol, self.cant_participantes, self.sala, self.estado, self.fecha_realizacion, self.fecha_registro, self.hora_inicio, self.hora_finalizacion)