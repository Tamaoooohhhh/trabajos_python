numero = int(input("Ingrese el número que desea multiplicar: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")

numero_entero=int(input("Ingrese un número entero positivo: "))

suma = 0
for i in range(1, numero_entero + 1):
    suma = suma + i

print(i)
print(f"La suma de los primeros {numero_entero} numeros naturales es {suma}")

for i in range(10):
    print(f"{i} - Hola pe")