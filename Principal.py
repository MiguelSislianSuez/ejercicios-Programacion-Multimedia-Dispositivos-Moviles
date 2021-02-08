from random import randrange


def pedir_int(mensaje):
    try:
        op = int(input(mensaje))
    except ValueError:
        op = None
    finally:
        return op



def generar_jugada_crupier(contador_cartas_crupier):
    num = 0
    while num < 15:
        numRand = randrange(1,11)
        num = num + numRand
        contador_cartas_crupier +=1

    return num, contador_cartas_crupier


def escribir_submenu():
    pass


def coger_carta(juego_usuario):
    cartaR = randrange(1,11)
    print("La carta es: ", cartaR)
    juego_usuario += cartaR
    print("Tu jugada suma: ", juego_usuario)
    return juego_usuario


def generar_jugada_usuario(juego_usuario, contador_cartas_usuario):
    juego_usuario = coger_carta(juego_usuario)
    contador_cartas_usuario +=1
    while juego_usuario < 21:
        escribir_submenu()
        pedir_carta = pedir_int("¿Seguir jugando?\n 1. Sí\n 2. No\n Escoja una opción:\n")
        if pedir_carta == 1:
            juego_usuario = coger_carta(juego_usuario)
            contador_cartas_usuario +=1
            print("Ha robado", contador_cartas_usuario, "cartas")

        if pedir_carta == 2:
            break

        else:
            print("Escoja una opción válida: ")
    return juego_usuario, contador_cartas_usuario


if __name__ == '__main__':
        
    while True:
        jugada_usuario = 0
        contador_cartas_usuario = 0
        contador_cartas_crupier = 0

        print("BLACK JACK\n", "1.Modofácil\n", "2.Modo normal\n", "0.Salir\n")
        opcion = pedir_int("Escoja una opción: ")

        if opcion == 0:
            exit(0)
        elif opcion == 1:
            jugada_crupier, contador_cartas_crupier = generar_jugada_crupier(contador_cartas_crupier)#metodo que devuelve un numero y que nos retorna por parametro las jugadas del crupier
            if jugada_crupier <  21:
                print("La jugada del crupier es: ", jugada_crupier, "en", contador_cartas_crupier, "cartas")

            # llamamos al metodo generar jugada usuario que nos devuelve
            jugada_usuario, contador_cartas_usuario = generar_jugada_usuario(jugada_usuario, contador_cartas_usuario)
            if jugada_usuario == 21 and jugada_crupier < jugada_usuario:
                print("HAS GANADO. Has sacado", jugada_usuario, "en", contador_cartas_usuario,"cartas")
            elif jugada_usuario < 21 and jugada_usuario > jugada_crupier or jugada_usuario < 21 and jugada_usuario < jugada_crupier:
                print("HAS GANADO. Has sacado", jugada_usuario, "en", contador_cartas_usuario,"cartas")
            elif jugada_usuario > 21:
                print("Has perdido. Tu jugada es",jugada_usuario,"Es mayor que 21")
            elif jugada_usuario == jugada_crupier:
                if contador_cartas_usuario > contador_cartas_crupier:
                    print("PIERDES!. Has robado", contador_cartas_usuario, "El crupier ha robado", contador_cartas_crupier)
                elif contador_cartas_usuario < contador_cartas_crupier:
                    print("GANAS!!. Has robado", contador_cartas_usuario, "El crupier ha robado", contador_cartas_crupier)

        elif opcion == 2:
            jugada_crupier, contador_cartas_crupier = generar_jugada_crupier(
                contador_cartas_crupier)  # metodo que devuelve un numero y que nos retorna por parametro las jugadas del crupier
            if jugada_crupier < 21:
                print("La jugada del crupier es: ? en", contador_cartas_crupier, "cartas")

            jugada_usuario, contador_cartas_usuario = generar_jugada_usuario(jugada_usuario,contador_cartas_usuario)  # llamamos al metodo generar jugada usuario que nos devuelve
            if jugada_usuario == 21 and jugada_crupier < jugada_usuario:
                print("HAS GANADO. Has sacado", jugada_usuario, "en", contador_cartas_usuario,"cartas y la banca ha sacado", jugada_crupier)
            if jugada_usuario < 21 and jugada_usuario > jugada_crupier or jugada_usuario < 21 and jugada_usuario < jugada_crupier:
                print("HAS GANADO. Has sacado", jugada_usuario, "en", contador_cartas_usuario, "cartas")
            elif jugada_usuario > 21:
                print("Has perdido. Tu jugada es", jugada_usuario, "Es mayor que 21")
            if jugada_usuario == jugada_crupier:
                if contador_cartas_usuario > contador_cartas_crupier:
                    print("PIERDES!. Has robado", contador_cartas_usuario, "El crupier ha robado",
                          contador_cartas_crupier)
                elif contador_cartas_usuario < contador_cartas_crupier:
                    print("GANAS!!. Has robado", contador_cartas_usuario, "El crupier ha robado",
                          contador_cartas_crupier)





