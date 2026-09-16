# OPERACIONES ARITMETICAS
# DECIDÍ REALIZAR UNA CALCULADORA COMPLETA COMO PARTE DE ESTE EJERCICIO

resultado = 0
def suma():
    global resultado
    numero1 = float(input("Primer número a sumar: ")); 
    numero2 = float(input("Segundo número a sumar: "));
    resultado = numero1 + numero2;
    return resultado

def resta():
    global resultado
    numero1 = float(input("Primer número a restar: ")); 
    numero2 = float(input("Segundo número a restar: "));
    resultado = numero1 - numero2;
    return resultado 

def multiplicacion():
    global resultado
    numero1 = float(input("Primer número a multiplicar: ")); 
    numero2 = float(input("Segundo número a multiplicar: "));
    resultado = numero1 * numero2;
    return resultado

def division():
    global resultado
    numero1 = float(input("Primer número a dividir: ")); 
    numero2 = float(input("Segundo número a dividir: "));
    resultado = numero1 + numero2;
    return resultado

def division_entera():
    global resultado
    while True: 
        try:
            numero1 = int(input("Primer número a dividir enteramente: ")); 
            numero2 = int(input("Segundo número a dividir enteramente: "));
            resultado = numero1 // numero2;
            return resultado    
        except ValueError:
            print("Error. Ingrese un número entero.")

def potencia():
    global resultado   
    numero1= float(input("Ingrese el primer número: "))
    numero2= float(input("Ingrese el número al que desea potenciarlo: "))
    resultado = numero1 ** numero2
    return resultado

def sacar_porcentaje():
    global resultado
    numero1= float(input("Ingrese el número al que desea sacar su porcentaje: "))
    numero2= float(input("Ingrese el porcentaje que desea obtener: "))
    resultado= numero1 * numero2 / 100


operacion = input("""¡Bienvenido a la calculadora de python!
Operaciones:
1. Suma
2. Resta
3. Multiplicación
4. División
5. División entera
6. Potencia
7. Obtener porcentaje
0. Salir

Ingresa el número del tipo de operación que deseas realizar: """)


if operacion == "1":
    suma()
    print(f"El resultado de la suma es: {resultado}");
elif operacion == "2":
    resta()
    print(f"El resultado de la resta es: {resultado}")
elif operacion == "3":
    multiplicacion()
    print(f"El resultado de la multiplicación es: {resultado}")
elif operacion == "4":
    division()
    print(f"El resultado de la división es: ")
elif operacion == "5":
    division_entera()
    print(f"El resultado de la división entera es: {resultado}")
elif operacion == "6":
    potencia()
    print(f"El resultado de la potencia es: {resultado}")
elif operacion == "7":
    sacar_porcentaje()
    print(f"La cantidad obtenida es: {resultado}")
elif operacion=="0":
    print("Saliste de la calculadora. Ok, bye")
else: print("Está bien.")


