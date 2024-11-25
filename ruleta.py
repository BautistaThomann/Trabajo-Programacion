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