from models.reunion import Reunion
#Reunion formal: toda reunion previamente agendada
class ReunionFormal(Reunion):
  clave = "reunion_formal"
  def getClave(self):
    return self.clave
  def __init__(self, detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion):
    super().__init__(detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion)
    self.fecha_registro= fecha_registro
    self.hora_inicio= hora_inicio
    self.hora_finalizacion= hora_finalizacion
  def copy(self):
    #return ReunionFormal(super().__init__(self.detalle, self.organizador, self.organizador_rol, self.cant_participantes, self.sala, self.estado, self.fecha_realizacion), self.fecha_registro, self.hora_inicio, self.hora_finalizacion)
    return ReunionFormal(self.detalle, self.organizador, self.organizador_rol, self.cant_participantes, self.sala, self.estado, self.fecha_realizacion, self.fecha_registro, self.hora_inicio, self.hora_finalizacion)