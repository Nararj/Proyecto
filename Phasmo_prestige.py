#Un código que te diga tu rol actual, cuántos niveles te faltan para llegar al prestigio que quieres en Phasmophobia y qué rol tendrás en ese prestigio.

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

# Funcion para definir rl rol actual

def roles(nivel):
    if obtener_nivel(nivel):
        if nivel >= 1 and nivel <= 99:
            print("Tu rol es Intern")
        elif nivel <= 199:
            print("Tu rol es Recruit")
        elif nivel <= 299:
            print("Tu rol es Investigator")
        elif nivel <= 399:
            print("Tu rol es Pbt. Investigator")
        elif nivel <= 499:
            print("Tu rol es Detective")
        elif nivel <= 599:
            print("Tu rol es Technician")
        elif nivel <= 699:
            print("Tu rol es Specialist")
        elif nivel <= 799:
            print("Tu rol es Analyst")
        elif nivel <= 899:
            print("Tu rol es Agent")
        elif nivel <= 999:
            print("Tu rol es Operator")
        elif nivel <= 2000:
            print("Tu rol es Comissioner")

# Pedir los datos

nivel = int(input("Escribe tu nivel actual: "))
print("Existe prestigio de 1 a 20")
prestigio = int(input("Escribe nivel de prestigio deseado: "))

calcular_niveles(nivel, prestigio)
roles(nivel)