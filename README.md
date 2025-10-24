# Proyecto
- Un código que te diga tu rol actual y cuántos niveles te faltan para llegar al prestigio que quieres en Phasmophobia
- Lo encuentro interesante porque cuando yo intenté buscar esta información no me apareció ningún dato y sería más fácil para los jugadores saber esta información si ya existe algo que te la diga.

**ALGORTIMO**

*ENTRADAS*
 
 - Nivel actual (número entero)
 - Que prestigio quieres llegar (número entero)

*ALGORITMO*

	1.- Se pide al usuario el nivel actual y prestigio deseado
	2.- Asignar valores y rol a cada prestigio
	3.- Dependiendo del rol deseado
		3.1.- Restar el nivel actual al nivel de prestigio
	4.- Devolver la cantidad de niveles faltantes, rol y prestigio actuales
	
*SALIDAS*

 - Rol actual (texto)
 - Cuanto te falta para el prestigio deseado (número entero)
 - Nivel y prestigio actuales (número entero)
