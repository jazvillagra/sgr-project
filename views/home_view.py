#! /usr/bin/python3
import os
from controllers.sala_controller import SalaController
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
  except KeyError:
    print("La clave es invalida")


def home_menu():
  os.system('clear')
  print ("Bienvenido al SGR. Por favor, seleccione la accion que desea realizar: ")
  print ("\t1 - Agregar sala")
  print ("\t2 - Listar salas")
  print ("\t3 - Iniciar reunion informal")
  print ("\t0 - Salir")
while True:
  home_menu()
  opcion_menu = input("Inserte un numero valor: ")
  if opcion_menu=="1":
    #Se eligio crear una sala
    nombre_sala= input("Nombre de sala: ")
    max_ocupantes= int(input("Maximo de ocupantes: "))
    estado_sala= input("Estado de sala(habilitada o inhabilitada): ")
    SalaController.agregar_sala(nombre_sala, max_ocupantes, estado_sala)
    input("Se ha agregado una sala.\nPulsa una tecla para continuar")
  elif opcion_menu=="2":
#    SalaController.listar_salas()
    input("Esta funcion se implementara muy pronto\nPulsa una tecla para continuar")
  elif opcion_menu=="3":
    input("Esta funcion se implementara muy pronto\nPulsa una tecla para continuar")
  elif opcion_menu=="0":
    break
  else:
    print ("")
    input("No has pulsado ninguna opción correcta.\nPulsa una tecla para continuar")