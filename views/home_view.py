#! /usr/bin/python3
from datetime import datetime, date, time, timedelta
import os, sys, calendar
from controllers.sala_controller import SalaController
from controllers.reunion_controller import ReunionController
from mizodb import MiZODB, transaction

db = MiZODB('sgr-data.fs')
dbroot = db.root
modulos= ["organizacion", "sucursal","sala", "reunion_informal", "reunion_formal_unica", "reunion_formal_periodica"]
for i in modulos:
  print("Crearia ", i)
  try:
    print("Trying for ", i)
    if not i in dbroot.keys():
      db.root[i] = []
      transaction.commit()
      print(i, "creado")
  except KeyError:
    print("La clave es invalida")
db.close()

def home_menu():
  #os.system('clear')
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
  opcion_menu = input("Inserte una opcion: ")
  #####OPCION 1
  if opcion_menu=="1":
    #Se eligio crear una sala
    nombre_sala= input("Nombre de sala: ")
    try:
      max_ocupantes= int(input("Maximo de ocupantes: "))
    except ValueError:
      max_ocupantes= int(input("Por favor, ingrese un valor entero:"))
    estado_sala = ""
    while not estado_sala:
      estado_sala = input("Estado de la sala: \n1 - Habilitada\n2 - Inhabilitada")
      if estado_sala == "1":
        estado_sala = "Habilitada"
      elif estado_sala == "2":
        estado_sala = "Inhabilitada"
      else:
        print("Por favor, intente nuevamente")
    try:
      print("asg")
      if(sala_controller.agregar_sala(nombre_sala, max_ocupantes, estado_sala)):
        input("Se ha agregado una sala.\nPulsa una tecla para continuar")
    except:
      print("No se pudieron guardar los datos. Por favor intente nuevamente. Error:", sys.exc_info()[0])
      raise
  ######OPCION 2
  elif opcion_menu=="2":
    #Se eligio listar las salas
    salas = sala_controller.listar_salas()
    for i in salas:
      print("\n")
      print("Nombre: ", i.nombre_sala)
      print("Maximo de ocupantes: ", i.max_ocupantes)
      print("Estado: ", i.estado_sala)
    input("\nPulsa una tecla para continuar")
  #####OPCION 3
  elif opcion_menu=="3":
    #Se eligio agendar reunion
      detalle_reunion = input("Detalle de la reunion: ")
      organizador = input("Organizador/a: ")
      organizador_rol = input("Rol del organizador en la empresa: ")
      cant_participantes = int(input("Cantidad de participantes: "))
      sala_reunion = ""
      fecha_realizacion_reunion = input("Fecha de la reunion (yyyy-MM-dd): ")
      fecha_realizacion_reunion = reunion_controller.convertir_a_fecha(fecha_realizacion_reunion)
      lista_reuniones = reunion_controller.listar_reuniones_dia(fecha_realizacion_reunion)
      while not sala_reunion:
        print("Elija una sala de la lista de salas habilitadas:")
        salas_disponibles = sala_controller.listar_salas_disponibles_por_cantidad_participantes(cant_participantes)
        cont = 0
        for i in salas_disponibles:
          print("\n")
          print(cont, " - Nombre: ", i.nombre_sala)
          print("Maximo de ocupantes: ", i.max_ocupantes)
          cont += 1
        sala_reunion = salas_disponibles[int(input("Sala en la que se realiza: \n"))].nombre_sala
        hora_inicio = reunion_controller.convertir_a_horas(input("Hora de inicio (hh:mm): "))
        reuniones_dia_sala = reunion_controller.listar_reuniones_dia_sala(sala_reunion, fecha_realizacion_reunion)
        hora_finalizacion = reunion_controller.convertir_a_horas(input("Hora de finalización (hh:mm): "))
        ####
        ######ACA TE QUEDASTE
        for i in reuniones_dia_sala:
          while hora_inicio == i.hora_inicio or (hora_inicio > i.hora_inicio and hora_inicio < i.hora_finalizacion):
            hora_inicio = input("La sala ", sala_reunion,
                                "está ocupada en el horario seleccionado. Por favor ingrese un horario mayor a las ",
                                i.hora_finalizacion, "hs. o menor a ", i.hora_inicio," hs:")
          while hora_finalizacion > i.hora_inicio:
            hora_finalizacion = input("La reunion debe finalizar antes de las  ", i.hora_inicio, "hs.")
      estado = "PENDIENTE"
      print ("Reunion :\n 1 - Unica\n2 - Periodica")
      opcion_reunion = input("Elija una opcion: ")
      if opcion_reunion=="1":
        try:
          if(reunion_controller.agendar_reunion_unica(detalle_reunion, organizador, organizador_rol, cant_participantes,
                                                sala_reunion, estado, fecha_realizacion_reunion, hora_inicio, hora_finalizacion)):
            input("\nLa reunion se agendo correctamente. Pulse una tecla para continuar.")
        except:
          print("Unexpected error: ", sys.exc_info()[0])
          raise
  elif opcion_menu=="4":
    #Se eligio listar las reuniones en una sala en cierto día

    sala = input("Sala: ")
    fecha = input("Fecha: ")
    reunion_controller.listar_reuniones_dia_sala(sala, fecha)
    input("\nPulsa una tecla para continuar")
  elif opcion_menu=="0":
    break
  else:
    print ("")
    input("No has pulsado ninguna opción correcta.\nPulsa una tecla para continuar")
