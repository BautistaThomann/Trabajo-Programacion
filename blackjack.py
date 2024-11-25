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