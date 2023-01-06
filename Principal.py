__author__ = "TP2-G065"

from funciones import *


def principal():
    # Contadores
    cont_jugadas = 0
    puntos_totales_j1 = 0
    puntos_totales_j2 = 0
    rondas_ganadas_j1 = 0
    rondas_ganadas_j2 = 0
    cont_rondas_seguidas_j1 = 0
    cont_rondas_seguidas_j2 = 0
    aciertos_j1 = 0
    aciertos_j2 = 0
    ganador = None

    # Banderas
    fin_del_juego = False
    rondas_seguidas_j1 = False
    rondas_seguidas_j2 = False
    hubo_jugada_empate = False

    # Titulo
    print("■" * 31)
    print("\t!juegos de dos o tres!")
    print("■" * 31)

    print()

    # Carga de datos (nombres de jugadores)
    jugador_1 = input("Ingrese el nombre del Jugador N° 1: ")
    print("\n" + "○" * 35, "\n")
    jugador_2 = input("Ingrese el nombre del Jugador N° 2: ")

    print()

    # Valoricion de instrucciones
    instrucciones = int(input("Si desea ver las instrucciones de juego ingrese 1 CONFIRMAR\n"
                              "de lo contrario ingrese 2 para OMITIR: "))

    print()
    # Validacion de carga de datos de instrocciones
    while instrucciones != 1 and instrucciones != 2:
        print("ups, parece que se equivoco")
        instrucciones = int(input("Si desea ver las instrucciones de juego ingrese 2 para CONFIRMA"
                                  "de lo contrario ingrese 2 para OMITIR: "))

    # En caso de selecionas confirmar, se imprime en pantalla las instrucciones:
    if instrucciones == 1:
        print("■■■■■■■■■■■■■■■■■■■■\n"
              "■ reglas del juego ■\n"
              "■■■■■■■■■■■■■■■■■■■■\n\n"
              
              "1) los jugadores lazan 3 dados y deben apostar por par o impar\n\n"
    
              "2) si la suma de los 3 dados es de la paridad apostada "
              "suma como puntos, el valor del dado mas grande;\n"
              "en caso contrario, resta el dado de menor valor a su puntaje," 
              "pudiendo quedar en negativo.\n\n"
    
              "3) si cada una de los dados corresponde a la paridad elegida entoces"
              " se aplicara un bonus x2, sumando asi el doble de puntos de esa ronda\n"
               
              "4) Se repite la jugada para el segundo jugador con las mismas reglas que el primero.\n\n"
    
              "5) Al terminar el turno de ambos jugadores, verifican si alguno de ellos alcanzó el "
              "puntaje objetivo.\n\nSi no es así, vuelven a jugar ambos (cada uno debe completar su turno) "
              "hasta finalizar el juego.")

        print()

        input("presione enter para continuar")

    print()

    print("Ingrese valor que deben superar para poder ganar!")
    print("↓" * 49)

    puntaje_limite = validar()

    print()

    # inicia el procesamiento del juego
    while not fin_del_juego:
        cont_jugadas += 1

        # Conformacion de turno del primer jugador
        print("■" * 25)
        print("\tTurno de ", jugador_1)
        print("■" * 25)

        input("presione enter para continuar")

        print()

        # Invocacion de funcion para carga de datos de apuesta (jugador 1)
        apuesta_j1 = apostar(jugador_1)

        print()

        input("presione enter para poder lanzar los dados!")

        print()
        # Invocacion de funcion para la generacion de dados (jugador 1)
        dado_1 = lanzar_dados()
        dado_2 = lanzar_dados()
        dado_3 = lanzar_dados()

        print("Sus dados son: \ndado N° 1: ", dado_1, "\ndado N° 2: ", dado_2, "\ndado N° 3: ", dado_3)

        print()

        # Invocacion de funcion para verificar si se trata de dados impares o pares

        es_par_j1 = verificar_paridad(dado_1, dado_2, dado_3)

        # Invocacion de funcion para la determinacion de puntos obtenidos en esta ronda
        puntos_de_ronda_j1 = puntos_ronda(dado_1, dado_2, dado_3, apuesta_j1, es_par_j1)

        # El jugador acerto en su apuesta?
        if puntos_de_ronda_j1 > 0:
            aciertos_j1 += 1

        # Adicion de puntos de ronda a los puntos totales del jugador
        puntos_totales_j1 += puntos_de_ronda_j1

        # Impresion en pantalla de puntos obtenidos hasta el momento (tanto totales como parciales)
        print("Los puntos obtenidos fueron: ", puntos_de_ronda_j1)

        print("Los puntos totales de", jugador_1, "acutalemente son:", puntos_totales_j1)
        
        print()

        input("presione enter para continuar")

        print()

        print("■" * 25)
        print("\tTurno de ", jugador_2)
        print("■" * 25)

        input("presione enter para continuar")

        print()
        # Invocacion de funcion para carga de datos de apuesta (jugador 2)
        apuesta_j2 = apostar(jugador_2)

        input("Presione enter para lanzar dados")

        dado_1_2 = lanzar_dados()
        dado_2_2 = lanzar_dados()
        dado_3_2 = lanzar_dados()

        print("Sus dados son: \nDado N° 1: ", dado_1_2, "\nDado N° 2: ", dado_2_2, "\nDado N° 3: ", dado_3_2)

        print()

        # Invocacion de funcion para verificar si se trata de dados impares o pares
        es_par_j2 = verificar_paridad(dado_1_2, dado_2_2, dado_3_2)

        # Invocacion de funcion para la determinacion de puntos obtenidos en esta ronda
        puntos_de_ronda_j2 = puntos_ronda(dado_1_2, dado_2_2, dado_3_2, apuesta_j2, es_par_j2)

        # El jugador acerto en su apuesta?
        if puntos_de_ronda_j2 > 0:
            aciertos_j2 += 1

        puntos_totales_j2 += puntos_de_ronda_j2

        # Impresion en pantalla de puntos obtenidos hasta el momento (tanto totales como parciales)
        print("Los puntos obtenidos fueron: ", puntos_de_ronda_j2)

        print("Los puntos totales de", jugador_2, "acutalemente son:", puntos_totales_j2)
        
        print()

        input("Presione enter para continuar")

        print()

        # Se evalua si algun jugador gana 3 rondas seguidas
        if puntos_de_ronda_j1 > puntos_de_ronda_j2:
            rondas_ganadas_j1 += 1
            rondas_seguidas_j1 = True
            rondas_seguidas_j2 = False

        elif puntos_de_ronda_j2 > puntos_de_ronda_j1:
            rondas_ganadas_j2 += 1
            rondas_seguidas_j2 = True
            rondas_seguidas_j1 = False

        # Se evalua si hubo alguna ronda con empate
        else:
            hubo_jugada_empate = True

        # Acumulacion de ronda ganadas seguidas de los jugadores
        if rondas_seguidas_j1:
            cont_rondas_seguidas_j1 += 1

        if rondas_seguidas_j2:
            cont_rondas_seguidas_j2 += 1

        # Algun jugador llego al puntaje limite?
        if puntaje_limite < puntos_totales_j1 or puntaje_limite < puntos_totales_j2:

            # Si los jugadores empataron en puntaje:
            if puntos_totales_j1 == puntos_totales_j2:

                # Desempate segun la cantidad de rondas ganadas:
                if rondas_ganadas_j1 < rondas_ganadas_j2:
                    ganador = jugador_1
                elif rondas_ganadas_j1 == rondas_ganadas_j2:
                    ganador = "han empatado"
                else:
                    ganador = jugador_2

            # Si no hubo empate, gano el jugador 1?
            elif puntos_totales_j1 > puntos_totales_j2:
                ganador = jugador_1

            # Si no hubo empate, gano el jugador 2?
            else:
                ganador = jugador_2
            fin_del_juego = True

    # impresion en pantalla de resultados resultados

    # Impresion de ganador o empate
    if puntos_totales_j1 > puntos_totales_j2:
        print("Felicidades", jugador_1, "ganaste con", puntos_totales_j1, "puntos", "y", aciertos_j1, "aciertos")

    elif puntos_totales_j2 > puntos_totales_j2:
        print("Felicidades", jugador_1, "ganaste con", puntos_totales_j2, "puntos", "y", aciertos_j2, "aciertos")

    else:
        print(ganador)

    # Porcentaje de aciertos de ambos jugadores
    por_aciert_jugador_1 = porcentaje_aciertos(cont_jugadas, aciertos_j1)
    por_aciert_jugador_2 = porcentaje_aciertos(cont_jugadas, aciertos_j2)

    print()
    print("el porcentaje de aciertos de", jugador_1, "fue de", por_aciert_jugador_1)
    print("el porcentaje de aciertos de", jugador_2, "fue de", por_aciert_jugador_2)
    print()

    # El ganador tuvo el mayor porcentaje de aciertos?
    if por_aciert_jugador_1 > por_aciert_jugador_2 or por_aciert_jugador_2 > por_aciert_jugador_1:
        if ganador == jugador_1:
            print("El", jugador_1, "gano con el mayor porcentaje de aciertos")
            print()
    else:
        if ganador == jugador_2:
            print("El", jugador_2, "gano con el mayor porcentaje de aciertos")
            print()

    # Hubo algun jugador que gano tres rondas seguidas
    if cont_rondas_seguidas_j1 > 3 or cont_rondas_seguidas_j2 > 3:
        print("Al menos un jugador gano tres rondas seguidas")
        print()

    # Hubo alguna jugada con empate?
    if hubo_jugada_empate:
        print("si hubo al menos una jugada con empate")
        print()

    # Puntaje promedio de jugadas por rondas.
    puntaje_promedio_j1 = puntaje_promedio(cont_jugadas, puntos_totales_j1)
    puntaje_promedio_j2 = puntaje_promedio(cont_jugadas, puntos_totales_j2)

    print("El puntaje promedio obtenido por", jugador_1, "fue:", puntaje_promedio_j1)
    print("El puntaje promedio obretido por", jugador_2, "fue:", puntaje_promedio_j2)

    print()

    # Cantidad total de jugadas (una jugada cada dos turnos)
    print("la cantidad de jugadas realizadas fueron: ", cont_jugadas)


if __name__ == "__main__":
    principal()
