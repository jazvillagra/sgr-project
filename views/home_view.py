#! /usr/bin/python3
import os, sys
from controllers.sala_controller import SalaController
from controllers.reunion_controller import ReunionController
from mizodb import MiZODB, transaction

db = MiZODB('sgr-data.fs')
dbroot = db.root
modulos= ["organizacion", "sucursal","sala", "reunion_informal", "reunion_formal_unica", "reunion_formal_periodica"]
for i in modulos:
  try:
    print(i)
    if not str(i) in dbroot:
      dbroot[i] = []
      transaction.commit()
      db.close()
  except KeyError:
    print("La clave es invalida")


def home_menu():
  os.system('clear')
  print ("Bienvenido al SGR. Por favor, seleccione la accion que desea realizar: ")
  print ("\t1 - Agregar sala")
  print ("\t2 - Listar salas")
  print ("\t3 - Agendar reunion")
  print ("\t4 - Listar reuniones del dia")
  print ("\t0 - Salir")
while True:
  home_menu()
  sala_controller = SalaController()
  reunion_controller = ReunionController()
  opcion_menu = input("Inserte un numero valor: ")
  if opcion_menu=="1":
    #Se eligio crear una sala
    nombre_sala= input("Nombre de sala: ")
    max_ocupantes= int(input("Maximo de ocupantes: "))
    estado_sala= input("Estado de sala(habilitada o inhabilitada): ")
    try:
      if(sala_controller.agregar_sala(nombre_sala, max_ocupantes, estado_sala)):
        input("Se ha agregado una sala.\nPulsa una tecla para continuar")
    except:
      print("Unexpected error:", sys.exc_info()[0])
      raise
  elif opcion_menu=="2":
    sala_controller.listar_salas()
    input("\nPulsa una tecla para continuar")
  elif opcion_menu=="3":
    detalle_reunion = input("Detalle de la reunion: ")
    organizador = input("Organizador/a: ")
    organizador_rol = input("Rol del organizador en la empresa: ")
    cant_participantes = input("Cantidad de participantes: ")
    sala_reunion = input("Sala en la que se realiza: ")
    estado = "PENDIENTE"
    fecha_realizacion_reunion = input("Fecha y hora de la reunion (yyyy-MM-dd hh:mm): ")
    try:
      if(reunion_controller.agendar_reunion(detalle_reunion, organizador, organizador_rol, cant_participantes, sala_reunion, estado, fecha_realizacion_reunion)):
        input("\nLa reunion se agendo correctamente. Pulse una tecla para continuar.")
    except:
      print("Unexpected error: ", sys.exc_info()[0])
      raise  
  elif opcion_menu=="4":
    pass
    input("\nPulsa una tecla para continuar")
  elif opcion_menu=="0":
    break
  else:
    print ("")
    input("No has pulsado ninguna opción correcta.\nPulsa una tecla para continuar")