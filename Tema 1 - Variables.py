# EJERCICIO 1: SOLICITAR EL ANCHO Y LARGO DE UN TERRENO Y CALCULAR SU PERIMETRO

ancho=float(input("Ingrese el ancho del terreno: "))
largo=float(input("Ingrese el largo del terreno: "))   

perimetro= (ancho + largo) * 2 #SUPONIENDO QUE EL TERRENO ES RECTANGULAR
print(f"El perimetro del terreno es: {perimetro}")

# EJERCICIO 2: SOLICITAR TRES NUMEROS Y OBTENER SU PROMEDIO

numero1=float(input("Ingrese el primer número: "))
numero2=float(input("Ingrese el segundo número: "))
numero3=float(input("Ingrese el tercer número: "))

promedio=(numero1 + numero2 + numero3) / 3
print(f"El promedio es {promedio}")

# EJERCICIO 3: SOLICITAR EL NOMBRE Y LA EDAD DE UNA PERSONA Y MOSTRAR UN MENSAJE DE PRESENTACIÓN

nombre=str(input("Ingrese su nombre: "))
edad=(input("Ingrese su edad: "))
print(f"Hola, me llamo {nombre} y tengo {edad} años. ¡Mucho gusto!")

# EJERCICIO 4:  CONVERTIR COP A USD

pesos_col=float(input("¿Cuántos pesos colombianos desea convertir a dólares? "))
usd= pesos_col * 0.00032
print(f"{pesos_col} son {usd} dólares")

# EJERCICIO 5: CONVERTIR SEGUNDOS A MINUTOS Y HORAS

segundos=float(input("Ingrese los segundos que desea convertir: "))
horas= segundos / 3600
minutos= segundos / 60
print(f"{segundos} segundos equivalen a {minutos} minutos y {horas} horas.")

    