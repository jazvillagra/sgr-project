import persistent, transaction, json
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
      #Para mantener el indice de las reuniones guardadas, se retorna el tamaño del array
      idx_reuniones = len(reuniones)
    else:
      reunion = json.loads(self.a_json)
      reuniones = [reunion]
      root.reuniones = json.dumps(reuniones)
      #Si todavia no se guardaron reuniones, el indice queda en cero
      idx_reuniones = len(reuniones)
    transaction.commit()
    return idx_reuniones
  #Cancelar reunion
  def cancelar_reunion(self):
    pass
  #Reagendar reunion
  def reagendar_reunion(self):
    pass
  #Convertir string a json
  def a_json(self):
    return "{\"detalle\":\""+self.detalle+"\", \"organizador\":\""+self.organizador+", \"organizador_rol\":\""+self.organizador_rol+", \"cant_participantes\":\""+self.cant_participantes+", \"estado\":\""+self.estado+", \"fecha_realizacion\":\""+self.fecha_realizacion+"}"
