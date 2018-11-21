from models.reunion_formal import ReunionFormal
#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class ReunionFormalPeriodica(ReunionFormal):
  clave="reunion_formal_periodica"
  def getClave(self):
    return self.clave
  def __init__(self, detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion, fecha_inicio, fecha_finalizacion, frecuencia):
    super().__init__(detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion)
    self.fecha_inicio = fecha_inicio
    self.fecha_finalizacion = fecha_finalizacion
    self.frecuencia = frecuencia
  def copy(self):
    return ReunionFormalPeriodica(self.detalle, self.organizador, self.organizador_rol, self.cant_participantes, self.sala, self.estado, self.fecha_realizacion, self.fecha_registro, self.hora_inicio, self.hora_finalizacion, self.fecha_inicio, self.fecha_finalizacion, self.frecuencia)