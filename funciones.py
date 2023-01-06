import random


# Funcion para la generacion de dados
def lanzar_dados():
    dado = random.randint(1, 6)
    return dado


# Funcion para la carga y validacion del puntaje objetivo o puntaje limitec (que no sea menor a 10)
def validar():
    x = int(input("Por favor, ingrese un numero mayor al 10: "))

    # validacion de carga de datos (puntaje limite)
    while x <= 10:
        print()
        print("ups!, valor no valido, ingreselo nuevamente!")
        x = int(input("¡ingrese un valor mayor a mayor 10!: "))
    return x


# Funcion para la carga de apuestas y validacion de esta.
def apostar(nombre):
    print("¡" + nombre + ",", "es hora de apostar!")
    print()
    apuesta = int(input("Ingrese 2 para par 3 para impar: "))
    print()

    # Validacion de apuesta
    while apuesta != 2 and apuesta != 3:
        print("ups, la apuesta ingresdada no es valida")
        apuesta = int(input("Por favor, ingresela nuevamente: "))
        print()

    if apuesta == 2:
        print("muy bien, usted aposto por los pares!!")
    else:
        print("muy bien, usted aposto por los impares!!")

    return apuesta


# Funcion para verificar si la suma de los dados generados es par
def verificar_paridad(dado_1, dado_2, dado_3):
    x = (dado_1 + dado_2 + dado_3) % 2
    if x == 0:
        return True
    return False


# Funcion para la busqueda del menor (entre tres valores)
def menor(dado_1, dado_2, dado_3):
    if dado_1 < dado_2 and dado_1 < dado_3:
        return dado_1
    elif dado_2 < dado_3:
        return dado_2
    else:
        return dado_3


# Funcion para la busqueda del mayor (entre tres valores)
def mayor(dado_1, dado_2, dado_3):
    if dado_1 > dado_2 and dado_1 > dado_3:
        return dado_1
    elif dado_2 > dado_3:
        return dado_2
    else:
        return dado_3


# Funcion para verificar si los tres dados son simultaneamente pare o simultaneamente impares
# y si coinciden con la apuesta. (Sirve para saber si aplicar el doble del puntaje obtenido)
def verificar_multiplicador(dado_1, dado_2, dado_3, es_par):
    if es_par:
        if dado_1 % 2 == 0 and dado_2 % 2 == 0 and dado_3 % 2 == 0:
            return True
        else:
            return False
    elif not es_par:
        if dado_1 % 2 != 0 and dado_2 % 2 != 0 and dado_3 % 2 != 0:
            return True
        else:
            return False


# Funcion para verificar, si el jugador acerto con su apuesta o no. En base a esto se hace
# la asignacion o resta de puntos correspondiente
def puntos_ronda(dado_1, dado_2, dado_3, apuesta, es_par):
    cont_puntos = 0
    if apuesta == 2:
        if es_par:
            cont_puntos += mayor(dado_1, dado_2, dado_3)
        else:
            cont_puntos -= menor(dado_1, dado_2, dado_3)
    else:
        if not es_par:
            cont_puntos += mayor(dado_1, dado_2, dado_3)
        else:
            cont_puntos -= menor(dado_1, dado_2, dado_3)

    # Uso de la funcion verificar_multiplicador
    multiplicador_x_2 = verificar_multiplicador(dado_1, dado_2, dado_3, es_par)

    # Se verifica, dependiendo del resultado de la funcion verificar_multiplicador se
    # duplica o no el puntaje parcial obtenido
    if multiplicador_x_2:
        cont_puntos = cont_puntos * 2
        return cont_puntos

    return cont_puntos


# funcion para ver el puntaje promedio de las jugadas
def puntaje_promedio(jugadas, puntaje=0):

    puntaje_prom = round(puntaje / jugadas, 2)

    return puntaje_prom


# funcion para ver los procentaje de aciertos de cada jugador
def porcentaje_aciertos(jugadas, aciertos=0):

    porcentaje_aciertos = round((aciertos * 100) / jugadas)

    return str(porcentaje_aciertos) + "%"
