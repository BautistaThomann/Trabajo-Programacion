def juegoBauti():
    import random

    # definir variables
    colores = ["negro", "rojo"]
    numeros = range(0, 5)
    acumulador_pesos = 0
    perdida = 0
    numero_ganador = 0 
    i = 0

    # funcion para imprimir los resultados 
    def imprimir_resultados (numero_ganador, color_ganador, pregunta1, pregunta2):
        if pregunta1 == "SI" and pregunta2 == "SI":
            print(f"Ha salido el número {numero_ganador} y el color {color_ganador}")
        elif pregunta1 == "SI":
            print(f"Ha salido el número {numero_ganador}")
        elif pregunta2 == "SI":
            print(f"Ha salido el color {color_ganador}")
        elif pregunta2 == "NO":
            print(f"Ha salido número {numero_ganador}")
        elif pregunta1 == "NO":
            print(f"Ha salido el color {color_ganador}")


    print("🎰💰 💲 SIMULACIÓN DE RULETA DE CASINO 💲 💰🎰")
    #ejecucion del programa
    while i == 0:
        pregunta1 = str(input("\n¿Desea apostar a números? (INGRESE SI O NO): ")).upper()
        # compara si quiere apostar a numeros
        if pregunta1 == "SI":
            numero_ganador = random.choice(numeros)
            color_ganador = random.choice(colores)
            
            numero_apostar = int(input("Ingrese un número al cual desea apostarle (0 - 4): "))
            if numero_apostar not in numeros:
                print("ERROR, NO SE HAN INGRESADO BIEN LOS DATOS.")
                break
            monto_apostar_numero = int(input(f"¿Cuanto desea apostar al número {numero_apostar}?: "))
            # compara si gana o pierde en numeros
            if numero_apostar == numero_ganador:
                pesos_ganados = monto_apostar_numero * 7
                acumulador_pesos += pesos_ganados
                if acumulador_pesos > 0:
                    acumulador_pesos = acumulador_pesos # variable por si gana en numeros 
                
                elif numero_apostar != numero_ganador:
                    perdida = perdida  # variable por si pierde en numeros
            # compara si quiere apostar a colores
            pregunta2 = str(input("¿Desea apostar a colores? (INGRESE SI O NO): ")).upper()
            
            if pregunta2 == "SI":
                color_apostar = str(input("Ingrese el color a cual desea apostarle: (rojo, negro): ")).lower()
                if color_apostar not in colores:
                    print("ERROR, NO SE HAN INGRESADO BIEN LOS DATOS.")
                    break

                monto_apostar_color = int(input("¿Cuanto desea apostar al color?: "))
                # compara si gana o pierde en numeros
                if color_apostar == color_ganador:
                    pesos_ganados = monto_apostar_color * 5
                    acumulador_pesos += pesos_ganados
                    if acumulador_pesos > 0:
                        acumulador_pesos = acumulador_pesos # variable por si gana en colores 
                
                    elif color_apostar != color_ganador:
                        perdida = perdida  # variable por si pierde en colores
        # compara si quiere o no apostar a colores
        elif pregunta1 == "NO":
            color_ganador = random.choice(colores)
            pregunta2 = str(input("¿Desea apostar a colores? (INGRESE SI O NO): ")).upper()
            if pregunta2 == "SI":
                color_apostar = str(input("Ingrese el color a cual desea apostarle: (rojo, negro): ")).lower()
                if color_apostar not in colores:
                    print("ERROR, NO SE HAN INGRESADO BIEN LOS DATOS.")
                    break

                monto_apostar_color = int(input("¿Cuanto desea apostar al color?: "))
                # compara si gana o pierde en numeros
                if color_apostar == color_ganador:
                    pesos_ganados = monto_apostar_color * 5
                    acumulador_pesos += pesos_ganados
                    if acumulador_pesos > 0:
                        acumulador_pesos = acumulador_pesos # variable por si gana en colores 
                
                    elif color_apostar != color_ganador:
                        perdida = perdida  # variable por si pierde en colores
        # compara si no quiere apostar a nada
        if pregunta1 == "NO" and pregunta2 == "NO":
            print("Esta bien, no hay drama!")
            break
        # muestra cuanto ha ganado e imprime los resultados
        if acumulador_pesos > 0: 
            print(f"Felicitaciones, usted ha ganado ${acumulador_pesos}")

            imprimir_resultados(numero_ganador, color_ganador, pregunta1, pregunta2)
        elif acumulador_pesos == 0:    
            print(f"Mala suerte, usted ha ganado ${perdida}")
            
            imprimir_resultados(numero_ganador, color_ganador, pregunta1, pregunta2)

        i = 1
        # pregunta si desea seguir jugando o no
        pregunta_final = str(input("Desea seguir jugando? (INGRESE SI O NO): ")).upper()

        if pregunta_final == "SI":
            i = 0
            acumulador_pesos = 0
        
        elif pregunta_final == "NO":
            i = 1
            print("Gracias por jugar 😁 !!")

def juegoJero():
    import random
    # definir mazos
    baraja = [2,3,4,5,6,7,8,9,10,10,10,10,11] * 4
    palos = ["♠", "♥", "♣", "♦",]
    # funcion para sacar el valor de cada mano y el valor de los as's
    def valor_mano(mano):
        valor = 0
        for carta in mano:
            valor += carta[0]
        

        if valor > 21 and 11 in mano:
            mano.remove(11)
            mano.append(1)
            valor = sum(mano)
        return valor
    # funcion para dar las cartas
    def pedir_carta():
        carta = random.choice(baraja)
        baraja.remove(carta)
        palo = random.choice(palos)
        return carta, palo
    # entradas de datos del usuario
    name = str(input("Ingrese su nombre o apodo: "))
    apuesta = int(input("Ingrese el monto que desea apostar: "))
    # almacena la mano 
    mano = [pedir_carta(), pedir_carta()]
    crupier = [pedir_carta(), pedir_carta()]
    # muestro el valor de cada mano
    print(f"{name} tiene: {valor_mano(mano)}  {mano}")
    print(f"El crupier tiene: {crupier[0]} y una carta oculta")
    # compara si la mano es menor a 21 (puntaje)
    while valor_mano(mano) < 21:
        carta = input("¿Pedir otra carta? (si/no): ").upper()
        if carta == "SI":
            nueva_carta = pedir_carta()
            mano.append(nueva_carta)
            print(f"{name} tiene: {valor_mano(mano)} {mano}")
        elif carta == "NO":
            break
        else:
            print("ERROR, ingrese SI o NO") 
    # compara mano crupier
    while valor_mano(crupier) < 17:
        nueva_carta = pedir_carta()
        crupier.append(nueva_carta)

    print(f"El crupier tiene: {valor_mano(crupier)} {crupier}")
    # compara los valores y mostar los posibles resultados
    if valor_mano(mano) > 21:
        print("¡te pasaste! perdiste 😢")
    elif valor_mano(crupier) > 21 and valor_mano(mano) <= 21 :
        print("¡Ganaste! 🤩")
        print("premio:",apuesta*2)
    elif valor_mano(mano) > valor_mano(crupier):
        print("¡Ganaste! 🤩")
        print("premio:",apuesta*2)
    elif valor_mano(mano) < valor_mano(crupier):
        print("¡Perdiste! 😔")
    else:
        print("¡Empate!")

def juegoBruno():
    import random

    print("🎰¡Bienvenido al casino!🎰") 

    print("✂️  📄 🪨  Piedra, papel o tijera 🪨  📄 ✂️")
    # defino las opciones en una lista
    opciones = ["piedra", "papel", "tijera"]
    # entrada de datos del usuario
    nombre = str(input("Ingrese su nombre: "))
    apuesta = int(input("Ingrese su apuesta: "))
    # elije una de las opciones
    jugador = input("elige: piedra, papel o tijera: ").lower()
    # la maquina elige una de las opciones al azar
    maquina = random.choice(opciones)
    print(f"la máquina eligió: {maquina}")
    # compara los opciones y muestra los resultados 
    if jugador == maquina:
        print(f"Empate! no ganas ni pierdes tu apuesta 🤝 mala suerte {nombre}.")
    elif (jugador == "piedra" and maquina == "tijera") or \
        (jugador == "papel" and maquina == "piedra") or \
        (jugador == "tijera" and maquina == "papel"):
        print(f"Ganaste ${apuesta*2}💰 felicitaciones {nombre}!")
    else:
        print(f"Perdiste ${apuesta}😢 mala suerte {nombre}")
        print ("Volve a intentarlo")

controlar = True

while controlar:
    print("\n======================================")
    print("🤑 🤑 💲 💸  CASINO 257  💲 💸 🤑 🤑")
    print("--------------------------------------")
    print("JUEGOS:\nJuego 1: Ruleta casino\nJuego 2: Blackjack\nJuego 3: Pieda, pepel o tijera")
    print("Ingrese 0 para salir")
    print("--------------------------------------")
    opcion_juego = int(input("Ingrese el número del juego: "))

    controlador_menu = True
    
    if opcion_juego == 1:
        while controlador_menu:
            juegoBauti()
            controlador_menu = False

    elif opcion_juego == 2:
        while controlador_menu:
            juegoJero()
            pregunta = str(input("¿Quiere seguir jugando? (SI/NO): ")).upper()
            if pregunta == "NO":
                controlador_menu = False
    elif opcion_juego == 3:
        while controlador_menu:
            juegoBruno()
            pregunta = str(input("¿Quiere seguir jugando? (SI/NO): ")).upper()
            if pregunta == "NO":
                controlador_menu = False
    
    elif opcion_juego == 0:
        controlar = False
        print("Gracias por jugar, espero que la hayas pasado bien!👏 ❤️")