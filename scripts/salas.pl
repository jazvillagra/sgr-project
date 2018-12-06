nombre_de_sala(sala1).
nombre_de_sala(sala2).
nombre_de_sala(sala3).
nombre_de_sala(sala4).

capacidad_de_sala(sala1, 15).
capacidad_de_sala(sala2, 200).
capacidad_de_sala(sala3, 35).
capacidad_de_sala(sala4, 60).

estado_de_sala(sala1, habilitada).
estado_de_sala(sala2, inhabilitada).
estado_de_sala(sala3, habilitada).
estado_de_sala(sala4, habilitada).

% Sala(nombre_de_sala, capacidad_de_sala, estado_de_sala)%
sala(nombre, capacidad, estado):-
    nombre_de_sala(nombre),
    capacidad_de_sala(nombre, capacidad),
    estado_de_sala(nombre, estado).


% Cuantas salas habilitadas hay: %

salas_habilitadas:-
	write("Salas habilitadas: "),
	listar_salas_habilitadas.

listar_salas_habilitadas:-
    esta_habilitada(Nombre),
    write(Nombre).

esta_habilitada(Nombre) :- estado_de_sala(Nombre, habilitada).

