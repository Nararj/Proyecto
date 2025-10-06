# Un código que te diga tu rol actual, cuántos niveles te faltan para llegar al prestigio que quieres en Phasmophobia y que rol tendras en ese prestigio.

# Definir una funcion para validar el nivel

def obtener_nivel(nivel):
    if nivel <= 0:
        return print("Nivel invalido")
    return nivel

# Definir una funcion para validar el prestigio

def obtener_prestigio(prestigio):
    if prestigio <= 0 or prestigio > 20:
        return print("Prestigio invalido")
    return prestigio

# Funcion para el calculo de los niveles que te faltan para el prestigio que quieres

def calcular_niveles(nivel, prestigio):
    if obtener_nivel(nivel) and obtener_prestigio(prestigio):
        actual = nivel / 1
        calculo1 = prestigio * 100
        faltante = calculo1 - nivel
        print(f"Tu nivel actual es {actual} y te faltan {faltante} niveles para prestigio deseado")

# Crear lista con roles

lista_de_roles = []
(1, 99, "Intern"),
(100, 199, "Recruit"),
(200, 299, "Investigator"),
(300, 399, "Pbt. Investigator"),
(400, 499, "Detective"),
(500, 599, "Technician"),
(600, 699, "Specialist"),
(700, 799, "Analyst"),
(800, 899, "Agent"),
(900, 999, "Operator"),
(1000, 2000, "Comissioner")

def roles(nivel):
    if obtener_nivel(nivel):
        for minimo, maximo, rol in lista_de_roles:
            if minimo <= nivel <= maximo:
                print(f"Tu rol es {rol}")
                break

# Hacer que el codigo se repita usando while

si = "s"
while si == "s":
    prestigio_actual = 0
    es_prestigio = input("¿Tienes algún prestigio? (s/n): ").lower()

# Definir si ya se tiene un prestigio

    if es_prestigio == "s":
        prestigio_actual = int(input("¿Qué prestigio tienes (1-20)?: "))
        while not (1 <= prestigio_actual <= 20):
            prestigio_actual = int(input("Prestigio inválido, ingresar un número del 1 al 20: "))

    nivel = int(input("Escribe tu nivel actual: "))
    while not (1 <= nivel <= 99):
        nivel = int(input("Nivel inválido, ingresar un número del 1 al 99: "))

# Ajustar el nivel a uno nuevo si ya se tiene prestigio

    nivel_nuevo = ((prestigio_actual ) * 100) + nivel if prestigio_actual > 0 else nivel

    print("Existe prestigio de 1 a 20")
    prestigio_deseado = int(input("Escribe nivel de prestigio deseado: "))

    while not (1 <= prestigio_deseado <= 20):
        prestigio_deseado = int(input("Prestigio inválido, ingresar un número del 1 al 20: "))
    
    calcular_niveles(nivel_nuevo, prestigio_deseado)
    roles(nivel_nuevo)
    si = input("¿Quieres calcular otro nivel? (s/n): ").lower()

print("Gracias por usar :D")
