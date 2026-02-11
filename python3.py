import time
import random

time.sleep(2)
personaje=input("Elija un personaje: \n 1.- Enano \n 2.- Elfo \n 3.- Humano \n")
personajes=["Enano", "Elfo", "Humano"]
print("Cargando personaje...")
time.sleep(2)   
print("Personaje cargado exitosamente")
ataque=random.randint(10, 20)
defensa=random.randint(5, 15)
vida=random.randint(50, 100)
print("Ataque:", ataque)
print("Defensa:", defensa)
print("Vida:", vida)

def atacar():
    print("Atacando...")
    time.sleep(1)
    daño_oponente=random.randint(1, oponente[3])

    print("Daño al oponente:", daño_oponente)
    oponente[3]=oponente[3]-daño_oponente
def defender():
    print("Defendiendo...")
    time.sleep(1)
    defensa_extra=random.randint(0, 5)
    print("Defensa extra:", defensa_extra)

def generarOponente():
    oponente=["Oponente",0,0,0]
    oponente[0]=random.choice(personajes)
    print("Tu oponente es un", oponente[0])
    oponente[1]=random.randint(10, 20)
    oponente[2]=random.randint(5, 15)
    oponente[3]=random.randint(50, 100)
    return oponente[0]

print("¡Bienvenido al juego de rol!")
print("Tu personaje es un", personajes[int(personaje)-1])
oponente=generarOponente()
print("¡Un", oponente[0], "se acerca a ti!"+" Prepara tu estrategia.")
print("¡Comienza la batalla!")
while vida>0 and oponente[3]>0:
    print("Tu vida: ", vida)
    print("Vida del oponente: ", oponente[3])
    print("¿Qué quieres hacer?")
    print("1.- Atacar")
    print("2.- Defender")
    accion=input("Ingrese una opción: ")
    if accion=="1":
        atacar()
    elif accion=="2":
        defender()
    else:
        print("Opción no válida. El oponente aprovecha tu indecisión y te ataca.")
        time.sleep(1)
        daño=ataque - random.randint(0, defensa)
        print("Daño recibido:", daño)
        vida=vida-daño
if vida<=0:
    print("¡Has sido derrotado por el", oponente[0], "!")
    exit()
else:    print("¡Felicidades! Has derrotado al", oponente[0], "y ganado la batalla.")
