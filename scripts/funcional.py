from cytoolz import *
#Lista de elementos con sus respectivos atributos
lista_salas= [
	{"nombre": "Sala 1", "capacidad":20, "estado":"Habilitada"},
	{"nombre": "Sala 2", "capacidad": 200, "estado": "Inhabilitada"},
	{"nombre": "Sala 3", "capacidad": 45, "estado": "Habilitada"}]
#Lista de keys de los atributos
keys = {"nombre", "capacidad", "estado"}
#Lista salas habilitadas o con nombres
salas = list(map(lambda x: {k:v for k,v in x.items() if (k=="estado" and v=="Habilitada") or k=="nombre" or k=="capacidad"}, lista_salas))
#Se extraen solo los items que tienen estado==habilitada
salas_habilitadas = []
for i in salas:
	for k,v in i.items():
		if k=="estado" and v=="Habilitada":
			salas_habilitadas.append(i)

print(salas_habilitadas)