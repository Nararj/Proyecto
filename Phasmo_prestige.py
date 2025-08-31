#Un código que te diga tu rol actual, cuántos niveles te faltan para llegar al prestigio que quieres en Phasmophobia y qué rol tendrás en ese prestigio.

# Pedir nivel y prestigio deseado
nivel = int(input("Escribe tu nivel actual: "))
print("Existe prestigio de 1 a 20")
prestigio = int(input("Escribe nivel de prestigio deseado: "))
if prestigio  <= 0 or prestigio > 20:
        print("Prestigio invalido")
else:

# Calculo para nivel actual
    actual = nivel / 1

# Calcular cantidad de niveles para prestigio deseado
    calculo1 = prestigio * 100
    faltante = calculo1 - nivel

    print(f"Tu nivel actual es {actual} y te faltan {faltante} niveles para prestigio deseado")
