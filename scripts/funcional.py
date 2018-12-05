
import functools


""" Creación de objetos para las pruebas correspondientes """

sala = sala_1(nombre = "Sala 1", = "Bazan",
				cedula = 5244508, direccion = "asdf")
sala = sala_2(nombre = "Selva", apellido = "Barrios",
				cedula = 1234, direccion = "fdsa")
sala = sala_3(nombre = "Miguel", apellido = "Villamayor",
				cedula = 6789, direccion = "asfas")

lista_pacientes = [paciente_1, paciente_2, paciente_3]


for key in lista_pacientes:
    obj = lista_paciente[key]
    lista_pacientes.append(obj)
    return paciente

""" Recibe la cedula, y siempre retornará
los datos de una forma legible al usuario. """

def visualizar_paciente(cedula):
	
	def visualizar_paciente_1():
		return (cedula)

	def visualizar_paciente_2():
		return (cedula)

	def visualizar_paciente_3():
		return (cedula)

	lang_func = {paciente_1: visualizar_paciente_1,
    			paciente_2: visualizar_paciente_2,
    			paciente_3: visualizar_paciente_3}

	return lang_func[cedula]


fun_1 = visualizar_paciente(paciente_1)
fun_2 = visualizar_paciente(paciente_2)
fun_3 = visualizar_paciente(paciente_3)

print("\nLos pacientes en existencia actualmente son: ")
print(fun_1())
print(fun_2())
print(fun_3(), "\n")

def filtrar_pacientes(cedula):
	lista = (paciente for paciente in lista_paciente if paciente.cedula >1000) 

print(list(filter(filtrar_pacientes)))


