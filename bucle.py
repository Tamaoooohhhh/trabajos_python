import random

numero_secreto = random.randint(1, 5)
intentos =  4

for i in range(intentos):
    numero = int(input("Intenta adivinar el número secreto: "))
    
    if numero == numero_secreto:
        print("¡Felicidades, has adivinado!")
        break
    else: print(f"Te quedan {intentos - (i + 1)} intentos.")
                #i vale 0 al empezar, la formula queda:
                # 3 (intentos) - (0 + 1)
                # 3 - (1 +1)
                # 3 - (2 + 1)
    intentos_restantes = intentos - (i + 1)     
    if intentos_restantes == 0:
        print(f"Se te han acabado los intentos. El número secreto era {numero_secreto}")

    if numero < numero_secreto:
        print("Te faltó")
    elif numero > numero_secreto: 
        print("Te pasaste")
        
                