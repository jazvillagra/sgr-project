import persistent, transaction, json
from abc import ABC, abstractmethod
class Reunion:
  def __init__(self, detalle, organizador, organizador_rol, cant_participantes, estado, fecha_realizacion):
    self.detalle= detalle
    self.organizador= organizador
    self.organizador_rol= organizador_rol
    self.cant_participantes= cant_participantes
    self.estado= estado
    self.fecha_realizacion= fecha_realizacion
  #Agendar reunion
  def agendar_reunion(self, connection):
    root = connection.root
    if 'reuniones' in connection.root():
      reuniones = json.loads(root.reuniones)
      reunion = json.loads(self.a_json)
      reuniones.append(reunion)
      root.reuniones = json.dumps(reuniones)
    else:
      reunion = json.loads(self.a_json)
      reuniones = [reunion]
      root.reuniones = json.dumps(reuniones)
    transaction.commit()
  #Cancelar reunion
  def cancelar_reunion(self):
    pass
  #Reagendar reunion
  def reagendar_reunion(self):
    pass
  #Convertir string a json
  def a_json(self):
    return "{\"detalle\":\""+self.detalle+"\", \"organizador\":\""+self.organizador+", \"organizador_rol\":\""+self.organizador_rol+", \"cant_participantes\":\""+self.cant_participantes+", \"estado\":\""+self.estado+", \"fecha_realizacion\":\""+self.fecha_realizacion+"}"

#Reunion informal: aquella que comienza en el momento en que se elige la opcion en el menu.
#Dura entre 10 y 30 minutos
class ReunionInformal(Reunion):
  def __init__(self, duracion):
      self.duracion= duracion
  def begin_informal_meeting(self, hora_inicio):
      pass
  def finish_informal_meeting(self, duracion):
      pass

#Reunion formal: toda reunion previamente agendada
#Clase abstracta
class ReunionFormal(ABC, Reunion):
  def __init__(self, fecha_registro, hora_inicio, finish_hour):
    self.fecha_registro= fecha_registro
    self.hora_inicio= hora_inicio
    self.finish_hour= finish_hour

#Reunion formal unica: toda reunion previamente agendada que no se repite en el tiempo.
#Dura mas de 30 minutos y solo tiene fecha de inicio
class ReunionFormalUnica(ReunionFormal):
  def __init__(self):
      self.frecuencia= 1
      pass

#Reunion formal periodica: reunion previamente agendada y que se repite en el tiempo
#Tiene una frecuencia definida, junto con fecha de inicio y de fin
class FormalPeriodicMeeting(ReunionFormal):
  def __init__(self, begin_date, finish_date, frecuencia):
      self.begin_date= begin_date
      self.finish_date= finish_date
      self.frecuencia= frecuencia
  def edit_frequence(self, frecuencia):
      pass
  def change_finish_date(self, finish_date):
      pass
  