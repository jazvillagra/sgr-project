import persistent, datetime
from models.empresa import Organizacion
from models.sucursal import Sucursal
from models.sala import Sala
from models.reunion_formal_unica import ReunionFormalUnica
from models.reunion import Reunion
from mizodb import MiZODB, transaction

db = MiZODB('sgr-data.fs')
dbroot = db.root
modulos= ["empresa", "organizacion", "sucursal","sala", "reunion_informal", "reunion_formal_unica", "reunion_formal_periodica"]
for i in modulos:
  try:
    print(i)
    if not str(i) in dbroot:
      dbroot[i] = {} 
  except KeyError:
    print("La clave es invalida")
for key in dbroot.keys():
  print(key+':', dbroot[key])

class Aplicacion(persistent.Persistent):
  print("Bienvenido al SGR")
  @staticmethod
  def cargar_datos():
    sala1 = Sala("Sala de Reuniones 1", 8, "HABILITADO")
    reunionFormalUnica = ReunionFormalUnica(detalle="Revision de avances", organizador="Juan Perez", organizador_rol="Team Leader",
        cant_participantes= 6, estado="No realizada", fecha_realizacion="2018-11-06", fecha_registro=datetime.datetime.now(), hora_inicio="15:30", hora_finalizacion="17:00")

    sucursal = Sucursal("Paraguay", "Aregua", "Calle 1 casi Calle 2", "HABILITADO", sala1) 
    organizacion = Organizacion(sucursal, nombre="Organizacion1", rubro="Desarrollo")
    dbroot['sala'] = sala1
    dbroot['sucursal'] = sucursal
    dbroot['organizacion'] = organizacion
    dbroot['reunion_formal_unica'] = reunionFormalUnica
    