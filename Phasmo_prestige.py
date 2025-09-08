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

# Pedir los datos

nivel = int(input("Escribe tu nivel actual: "))
print("Existe prestigio de 1 a 20")
prestigio = int(input("Escribe nivel de prestigio deseado: "))

calcular_niveles(nivel, prestigio)
