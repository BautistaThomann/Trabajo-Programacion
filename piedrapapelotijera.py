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