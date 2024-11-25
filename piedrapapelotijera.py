import random

print("🎰¡Bienvenido al casino!🎰") 

print("✂️📄🪨 Piedra, papel o tijera 🪨📄✂️")

opciones = ["piedra", "papel", "tijera"]

apuesta = int(input("Ingrese su apuesta: "))
jugador = input("elige: piedra, papel o tijera: ").lower()

maquina = random.choice(opciones)
print(f"la máquina eligió: {maquina}")

if jugador == maquina:
    print(f"empate! no ganas ni pierdes tu apuesta 🤝.")
elif (jugador == "piedra" and maquina == "tijera") or \
     (jugador == "papel" and maquina == "piedra") or \
     (jugador == "tijera" and maquina == "papel"):
    print(f"Ganaste ${apuesta*2}💰!")
else:
    print(f"Perdiste ${apuesta}😢")
    print ("Volve a intentarlo")