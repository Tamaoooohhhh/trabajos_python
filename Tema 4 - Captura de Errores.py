""" try:
    numero = int(input("Ingrese un número: "))
    print(f"El número ingresado es: {numero}")
except ValueError:
    print(f"El valor no es un número válido.") """

menu = 0

while menu != 3:
    try:
        menu = int(input("""Elija la opción que desea utilizar
    1. Suma
    2. Resta
    3. Salir

    : """))
        
        if menu == 1:
            n1 = int(input("Ingrese el primer número: "))
            n2 = int(input("Ingrese el segundo número que desea sumar: "))
            print (f"{n1} + {n2} = {n1 + n2}")

        elif menu == 2:
                n1 = int(input("Ingrese el primer número: "))
                n2 = int(input("Ingrese el primer número que desea restar: "))
                print (f"{n1} - {n2} = {n1 - n2}")

        else: print("Opción invalida")
    except ValueError: print("Ingrese una opción válida\n")

print("Saliendo...")

print("=" * 70)
print("\n Ejercicio 2: División segura con ZeroDivisionError\n")
print("=" * 70)

try:
     dividendo = float(input("Ingrese el dividento: "))
     divisor = float(input("Ingrese el divisor: "))
     resultado = dividendo / divisor
     print(f"{dividendo} ÷ {divisor} = {resultado}")
except ZeroDivisionError: 
     print("Error: No es posible dividir entre cero.")
except ValueError:
     print("Error: Por favor ingrese únicamente valores númericos.")

print("=" * 70)
print("\n Ejercicio 3: Else y Finally\n")
print("=" * 70)

try:
     edad = int(input("Ingrese su edad: "))
except ValueError:
     print("Ingrese solo números enteros")
else:
     if edad >=18:
          print("Acceso permitido.") 
     else:
        print("Acceso denegado. Debe ser mayor de edad.")
finally: print("Verificación finalizada.")

print("=" * 70)
print("\n Ejercicio 4: Solicitar un dato válido hasta que el usuario lo ingrese correctamente \n")
print("=" * 70)

while True:
     try:
        nota =float(input("Ingrese la nota de 0.0 a 5.0"))
        if nota < 0.0 or nota > 5.0:
            raise ValueError("Error. La nota debe estar entre los valores permitidos.")
        break
     except ValueError as e:
          print(f"{e}. Intente de nuevo.")

print(f"Nota registrada: {nota}")

print("=" * 70)
print("\n Ejercicio 5: Raise - Lanzar una excepción realizada \n")
print("=" * 70)

def calcular_promedio(notas):
     if len(notas)==0:
          raise ValueError("La lista de notas no puede estar vacía")
     return sum(notas) / len (notas)

try:
    n = int(input("¿Cuántas notas va a ingresar? "))
    notas = []
    for i in range(n):
          nota = float(input(f"Nota {i + 1}: "))
          notas.append(nota)
    promedio = calcular_promedio(notas)
    print(f"Promedio: {round(promedio, 2)}")
except ValueError as e:
    print(f"Error: {e}")


    
