#! /usr/bin/python3
from datetime import datetime, date, time, timedelta
import os, sys, calendar
from controllers.sala_controller import SalaController
from controllers.reunion_controller import ReunionController
from controllers.organizacion_controller import OrganizacionController
from controllers.sucursal_controller import SucursalController

from mizodb import MiZODB, transaction

# def init_db():
#   db = MiZODB('views/sgr-data.fs')
#   dbroot = db.root
#   modulos= ["organizacion", "sucursal","sala", "reunion_informal", "reunion_formal_unica", "reunion_formal_periodica"]
#   for i in modulos:
#     print("Crearia ", i)
#     try:
#       print("Trying for ", i)
#       if not i in dbroot.keys():
#         db.root[i] = []
#         transaction.commit()
#         print(i, "creado")
#     except KeyError:
#       print("La clave es invalida")
#   db.close()

def welcome():
  #os.system('clear')

  organizacion_controller = OrganizacionController()
  sucursal_controller = SucursalController()
  sala_controller = SalaController()
  organizacion = organizacion_controller.traer_organizacion()
  salas = sala_controller.listar_salas()
  sucursal = sucursal_controller.traer_sucursal()
  print("Organizacion: ", organizacion[0].nombre)
  print ("Bienvenido al SGR de la Sucursal de", sucursal[0].pais, " en la ciudad de ", sucursal[0].ciudad)
  print("Las salas disponibles hasta el momento son: ")
  for i in salas:
    print("- ", i.nombre_sala)
#init_db()
welcome()

def home_menu():

  print("Por favor, seleccione la accion que desea realizar: ")
  print ("\t1 - Agregar sala")
  print ("\t2 - Listar salas")
  print ("\t3 - Agendar reunion")
  print ("\t4 - Listar reuniones del dia de una sala")
  print ("\t5 - Listar reuniones unicas")
  print ("\t6 - Listar reuniones periodicas")
  print ("\t7 - Listar todas las reuniones")
  print ("\t0 - Salir")

####Funcion para imprimir las reuniones en la vista
def mostrar_reuniones(reuniones):
  cont = -1
  #print("Printing values")
  for reu in reuniones:
    cont += 1
    print(cont, " - Detalle: ", reu.detalle)
    print(" Sala en que se realiza: ", reu.sala)
    print(" Fecha registro: ", reu.fecha_registro)
    print(" Agendada para: ", reu.fecha_realizacion)
    print(" Hora inicio: ", reu.hora_inicio, "\n")
  print("-----------")
  return cont


while True:
  home_menu()
  sala_controller = SalaController()
  reunion_controller = ReunionController()
  opcion_menu = input("Inserte una opcion: ")

  #####OPCION 1
  if opcion_menu=="1":
    #Se eligio crear una sala
    nombre_sala= input("Nombre de sala: ").upper()
    try:
      max_ocupantes= int(input("Maximo de ocupantes: "))
    except ValueError:
      max_ocupantes= int(input("Por favor, ingrese un valor entero:"))
    estado_sala = ""
    while not estado_sala:
      estado_sala = input("Estado de la sala (seleccione una opcion): \n1 - Habilitada\n2 - Inhabilitada\n")
      if estado_sala == "1":
        estado_sala = "Habilitada"
      elif estado_sala == "2":
        estado_sala = "Inhabilitada"
      else:
        estado_sala = input("Solo puede elegir entre las dos opciones anteriores. Por favor, intente nuevamente")
    try:
      if(sala_controller.agregar_sala(nombre_sala, max_ocupantes, estado_sala)):
        print("Se ha agregado una sala.")
        print("--------")
        input("Pulsa una tecla para continuar")
    except:
      print("No se pudieron guardar los datos. Por favor intente nuevamente. Error:", sys.exc_info()[0])
      print("-------")
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
    print("--------")
    input("Pulsa una tecla para continuar")

  #####OPCION 3
  elif opcion_menu=="3":
    #Se eligio agendar reunion
      print("Agendar reunion:")
      detalle_reunion = input("* Detalle de la reunion: ").upper()
      organizador = input("* Organizador/a: ").upper()
      organizador_rol = input("* Rol del organizador en la empresa: ").upper()
      cant_participantes = int(input("* Cantidad de participantes: "))
      fecha_realizacion_reunion = input("* Fecha de la reunion (yyyy-MM-dd): ")
      lista_reuniones = reunion_controller.listar_reuniones_dia(fecha_realizacion_reunion)
      sala_reunion = ""

      while not sala_reunion:
        print("Elija una sala de la lista de salas habilitadas:\n")

        cont = -1
        while cont < 0:
          salas_disponibles = sala_controller.listar_salas_disponibles_por_cantidad_participantes(cant_participantes)
          for i in salas_disponibles:
            cont += 1
            print(cont, "- Nombre: ", i.nombre_sala)
            print("  Maximo de ocupantes: ", i.max_ocupantes)
          if(cont < 0):
            cant_participantes = input("No hay salas disponibles para la cantidad de participantes de la reunion.\nPor favor disminuya la cantidad de participantes: ")

        sala_reunion = salas_disponibles[int(input("\n* Sala en la que se realiza (ingrese un nro correspondiente a una de las opciones anteriores)): \n"))].nombre_sala
        hora_inicio = input("* Hora de inicio (hh:mm): ")
        hora_finalizacion = input("* Hora de finalización (hh:mm): ")

        reuniones_dia_sala = reunion_controller.listar_reuniones_dia_sala(sala_reunion, fecha_realizacion_reunion)

        hora_inicio = reunion_controller.convertir_a_horas(hora_inicio)
        hora_finalizacion = reunion_controller.convertir_a_horas(hora_finalizacion)
        fecha_realizacion_reunion = reunion_controller.convertir_a_fecha(fecha_realizacion_reunion)

        for i in reuniones_dia_sala:
          while hora_inicio == i.hora_inicio or (hora_inicio > i.hora_inicio and hora_inicio < i.hora_finalizacion):
            hora_inicio = input("La sala ", sala_reunion,
                                "está ocupada en el horario seleccionado. Por favor ingrese un horario mayor a las ",
                                i.hora_finalizacion, "hs. o menor a ", i.hora_inicio," hs:")
          while hora_finalizacion > i.hora_inicio:
            hora_finalizacion = input("La reunion debe finalizar antes de las  ", i.hora_inicio, "hs.")

        estado = "Pendiente - Agendada"
        print ("* Reunion :\n1 - Unica\n2 - Periodica")
        opcion_reunion = ""
        while not opcion_reunion:
          opcion_reunion = input("Elija una opcion: ")
          if opcion_reunion == "1":
            try:
              fecha_registro = datetime.now()
              if (reunion_controller.agendar_reunion_unica(detalle_reunion, organizador, organizador_rol, cant_participantes, sala_reunion, estado, fecha_realizacion_reunion, fecha_registro, hora_inicio, hora_finalizacion)):
                input("\nLa reunion se agendo correctamente. Pulse una tecla para continuar.")
            except ValueError or TypeError:
              print("No se pudo registrar la reunion. El error fue: ", sys.exc_info()[0])
              raise
          elif opcion_reunion == "2":
            #####
            ### Este metodo debe mejorarse
            ### No se deberia ingresar la ultima fecha, solo la frecuencia. Como es muy complejo, se dejara el desarrollo de esto para la ultima entrega
            #####
            fecha_inicio = fecha_realizacion_reunion
            fecha_finalizacion = input("Defina la ultima fecha de realizacion (yyyy-MM-dd): ")
            fecha_finalizacion = reunion_controller.convertir_a_fecha(fecha_finalizacion)
            frecuencia = int(input("Frecuencia en dias:"))
            try:
              fecha_registro = datetime.now()
              if (reunion_controller.agendar_reunion_periodica(detalle_reunion, organizador, organizador_rol, cant_participantes,
                                                               sala_reunion, estado, fecha_realizacion_reunion, fecha_registro,
                                                               hora_inicio, hora_finalizacion, fecha_inicio, fecha_finalizacion, frecuencia)):
                input("\nLa reunion se agendo correctamente. Pulse una tecla para continuar.")
            except ValueError or TypeError:
              print("No se pudo registrar la reunion. El error fue: ", sys.exc_info()[0])
              raise
          else:
            opcion_reunion = ""
            print("No es una opcion valida. Por favor intente de nuevo.")
  ######OPCION 4
  elif opcion_menu=="4":
    #Se eligio listar las reuniones en una sala en cierto día
    sala = input("Sala: ")
    fecha = input("Fecha: ")
    reuniones = reunion_controller.listar_reuniones_dia_sala(sala, fecha)
    cont = mostrar_reuniones(reuniones)
    if cont < 0:
      print("No hay reuniones agendadas en ", sala, "para la fecha ", fecha)
    input("\nPulsa una tecla para continuar")
  ######OPCION 5
  elif opcion_menu == "5":
    #Se eligio listar todas las reuniones unicas
    reuniones = reunion_controller.listar_reuniones_unicas();
    cont = mostrar_reuniones(reuniones)
    if cont < 0:
      print("No hay reuniones unicas agendadas")
      input("\nPulse una tecla para continuar.")
  ######OPCION 6
  elif opcion_menu == "6":
    #Se eligio listar todas las reuniones periodicas
    reuniones = reunion_controller.listar_reuniones_periodicas();
    cont = mostrar_reuniones(reuniones)
    if cont < 0:
      print("No hay reuniones unicas agendadas")
      input("\nPulse una tecla para continuar.")
  ######OPCION 7
  elif opcion_menu == "7":
    reuniones = reunion_controller.listar_reuniones();
    cont = mostrar_reuniones(reuniones)
    if cont < 0:
      print("No hay reuniones periodicas agendadas")
      input("\nPulse una tecla para continuar.")

  elif opcion_menu=="0":
    break
  else:
    print ("")
    input("No has pulsado ninguna opción correcta.\nPulsa una tecla para continuar")