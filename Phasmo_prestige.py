# Un código que te diga tu rol actual y cuántos niveles te  
# faltan para llegar al prestigio que quieres en Phasmophobia

def obtener_nivel(nivel):
    """Valida que el nivel sea mayor que cero y devuelve su valor."""
    if nivel <= 0:
        return print("Nivel invalido")
    return nivel

def obtener_prestigio(prestigio):
    """Calcula cuantos niveles faltan para alcanzar el prestigio deseado."""
    if prestigio <= 0 or prestigio > 20:
        return print("Prestigio invalido")
    return prestigio

def calcular_niveles(nivel, prestigio):
    """Calcula cuantos niveles faltan para alcanzar el prestigio deseado."""
    if obtener_nivel(nivel) and obtener_prestigio(prestigio):
        actual = nivel / 1
        calculo1 = prestigio * 100
        faltante = calculo1 - nivel
        print(f"Tu nivel actual es {actual} y te faltan {faltante} niveles"
              " para prestigio deseado")

LISTA_DE_ROLES = [
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
    (1000, 2000, "Commissioner"),
]

CATEGORIAS = {
    "Principiante": ["Intern", "Recruit"],
    "Intermedio": ["Investigator", "Pbt. Investigator", "Detective"],
    "Avanzado": ["Technician", "Specialist", "Analyst"],
    "Experto": ["Agent", "Operator", "Commissioner"],
}

def roles(nivel):
    """Determina el rol y la categoria del jugador segun su nivel."""
    if not obtener_nivel(nivel):
        return

    rol_encontrado = None
    for minimo, maximo, rol in LISTA_DE_ROLES:
        if minimo <= nivel <= maximo:
            rol_encontrado = rol
            print(f"Tu rol actual es: {rol}")
            break

    if rol_encontrado:
        for categoria, lista in CATEGORIAS.items():
            if rol_encontrado in lista:
                print(f"Estas en la categoria: {categoria}")
                return

def main():
    """Funcion principal que controla la interaccion con el usuario."""
    si = "s"
    while si == "s":
        prestigio_actual = 0
        es_prestigio = input("¿Tienes algun prestigio? (s/n): ").lower()

        if es_prestigio == "s":
            prestigio_actual = int(input("¿Que prestigio tienes (1-20)?: "))
            while not (1 <= prestigio_actual <= 20):
                prestigio_actual = int(input("Prestigio invalido, "
                "ingresar un numero del 1 al 20: "))

        nivel = int(input("Escribe tu nivel actual: "))
        while not (1 <= nivel <= 99):
            nivel = int(input("Nivel invalido, ingresar un "
            "numero del 1 al 99: "))

        nivel_nuevo = (prestigio_actual * 100 + nivel
               if prestigio_actual > 0 else nivel)


        print("Existe prestigio de 1 a 20")
        prestigio_deseado = int(input("Escribe nivel de prestigio deseado: "))

        while not (1 <= prestigio_deseado <= 20):
            prestigio_deseado = int(input("Prestigio invalido, "
            "ingresar un numero del 1 al 20: "))
        
        calcular_niveles(nivel_nuevo, prestigio_deseado)
        roles(nivel_nuevo)
        si = input("¿Quieres calcular otro nivel? (s/n): ").lower()

    print("Gracias por usar :D")

if __name__ == "__main__":
    main()