import calendar
from typing import List, Any

from models.reunion import Reunion
from models.reunion_formal import ReunionFormal
from models.reunion_formal_unica import ReunionFormalUnica
from models.reunion_formal_periodica import ReunionFormalPeriodica
from models.reunion_informal import ReunionInformal
from datetime import datetime, date, time, timedelta
class ReunionController:

  #Agendar reunion
  def agendar_reunion_unica(self, detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion):
    reunion_formal_unica = ReunionFormalUnica(detalle, organizador, organizador_rol, cant_participantes, sala,
                                              estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion)
    return reunion_formal_unica.create()
  #Agendar reunion periodica
  def agendar_reunion_periodica(self, detalle, organizador, organizador_rol, cant_participantes, sala, estado, fecha_realizacion, fecha_registro, hora_inicio, hora_finalizacion, fecha_inicio, fecha_final, frecuencia):
    reunion_formal_periodica = ReunionFormalPeriodica(detalle, organizador, organizador_rol, cant_participantes,
                                                      sala, estado, fecha_realizacion, fecha_registro, hora_inicio,
                                                      hora_finalizacion, fecha_inicio, fecha_final, frecuencia)
    return reunion_formal_periodica.create()
  #Empezar una reunion informal. Esto se implementara con la interfaz grafica (se empieza con un botoncito que llame a esta accion)
  def empezar_reunion_informal(self, duracion):
    reunion_informal = ReunionInformal(duracion)
    return reunion_informal.create()
  #Listar TODAS las reuniones
  def listar_reuniones(self):
    reuniones = ReunionController.listar_reuniones_unicas(self)
    for i in ReunionController.listar_reuniones_periodicas(self):
      reuniones.append(i)
    return reuniones
  #Listar reuniones del dia de una sala
  def listar_reuniones_dia_sala(self, sala, fecha_a_buscar):
    #print("Buscando lista de reuniones segun su fecha")
    reuniones = ReunionController.listar_reuniones_dia(self, fecha_a_buscar)
    reuniones_dia_sala = []
    #print("Buscando por sala: ")
    for i in reuniones:
      if i.sala.upper() == sala.upper():
        reuniones_dia_sala.append(i)
        #print("Reu: ", i.detalle)
    return reuniones_dia_sala
  #Listar reuniones por dia en todas las salas
  def listar_reuniones_dia(self, fecha_a_buscar):
    fecha = ReunionController.convertir_a_fecha(self, fecha_a_buscar)
    reuniones = ReunionFormalUnica.getAll(ReunionFormalUnica)
    reuniones_dia = []
    for i in reuniones:
      #print("Dia a buscar: ", fecha)
      #print("Dia de la instancia: ", i.fecha_realizacion, " entonces: ", i.fecha_realizacion == fecha)
      if i.fecha_realizacion == fecha:
        reuniones_dia.append(i)
    return reuniones_dia
  #Convertir String recibido a formato de fecha
  def convertir_a_fecha(self, cadena_fecha):
    formato_fecha = "%Y-%m-%d"
    #Aqui se toma el string del usuario y se convierte a tipo Datetime con el formato especificado
    fecha= datetime.strptime(cadena_fecha, formato_fecha).date()
    return fecha
  #Convertir String recibido a formato de horas
  def convertir_a_horas(self, cadena_horas):
    formato_hora = "%H:%M"
    hora = datetime.strptime(cadena_horas, formato_hora).time()
    return hora
  #Listar todas las reuniones unicas en el calendario, de todos los dias y todas las salas
  def listar_reuniones_unicas(self):
    return ReunionFormalUnica.getAll(ReunionFormalUnica)
  def listar_reuniones_periodicas(self):
    return ReunionFormalPeriodica.getAll(ReunionFormalPeriodica)

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
  #Terminar una reunion informal.Esto se implementara con la interfaz grafica (se empieza con un botoncito que llame a esta accion)
  def terminar_reunion_informal(self, hora_finalizacion):
    pass
  #Cambiar la duracion de una reunion informal 
  def cambiar_duracion_reunion_informal(self):
    pass