# EJERCICIO 1: ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE Y LA EDAD DE UNA PERSONA Y DETERMINAR SI ES MAYOR O MENOR DE EDAD

print("=" * 90)
print("EJERCICIO 1. DETERMINAR SI LA PERSONA ES MAYOR DE EDAD Y CUÁNTOS AÑOS LE FALTAN EN CASO DE QUE NO.")
print("=" * 90)

nombre=input("Ingrese su nombre: ")
edad=int(input("Ingrese su edad: "))

def calcular_faltante_edad():
    global edad
    global faltante_edad
    edad= 18 - edad
    return edad 


if edad <= 0:
    print("Asegurese de colocar un número positivo.")
elif edad < 18:
    print(f"Estimado(a) {nombre}, usted es menor de edad y le faltan {calcular_faltante_edad()} año(s) para cumplir los 18. ")
elif edad >= 18:
    print(f"Estimado(a) {nombre}, usted es mayor de edad con sus correspondientes {edad} años.")

print("=" * 90)



#EJERICIO 2: ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE PROMEDIO FINAL DE UN ESTUDIANTE, EN UNA ESCALA DE 0.0 A 5.0


print("EJERCICIO 2. CLASIFICAR PROMEDIO DE ESTUDIANTE Y APROBARLO O REPROBARLO SEGÚN SU CALIFICACIÓN. ")
print("=" * 90)
nombre_estudiante=input("Ingrese su nombre: ")
nota_final= float(input("Ingrese su calificación final del periodo: "))

def aprobacion():
    global nota_final
    global aprobo_o_reprobo
    if nota_final >= 3:
        aprobo_o_reprobo="aprobado(a)"
    elif nota_final < 3: 
        aprobo_o_reprobo="reprobado(a)"
    return aprobo_o_reprobo

def calcular_desempeño():
    global nota_final
    global desempeño
    if nota_final < 3:
        desempeño= "insuficiente"
    elif 3 < nota_final < 3.5:
        desempeño= "aceptable"
    elif 3.4 < nota_final < 4.5:
        desempeño = "bueno"
    elif 4.4 < nota_final <= 5:
        desempeño="excelente"
    return desempeño

if 0.0 < nota_final <= 5.0:
    print(f"Estudiante {nombre_estudiante}, su nota final fue {nota_final}, de manera que fue {aprobacion()}, y su desempeño se ha caracterizado habiendo sido {calcular_desempeño()}.")
else: print("Por favor ingrese su calificación en una escala de 0 a 5.")

print("=" * 90)

# EJERCICIO 3:  ALGORITMO QUE SOLICITE EL NOMBRE UN CLIENTE Y VALOR TOTAL DE LA COMPRA, Y CALCULAR DESCUENTO SEGUN VALOR 

print("EJERCICO 3. CALCULAR DESCUENTO DE COMPRA SEGÚN SU VALOR.")
print("=" * 90)

nombre_cliente=input("Ingrese el nombre del cliente: ")
valor_compra=float(input("Ingrese el valor de la compra: "))

def calcular_descuento():
    global porcentaje_descuento
    global valor_compra
    global descuento_aplicado
    if valor_compra < 100000:
        descuento_aplicado=0
        porcentaje_descuento="No se aplicó ningún descuento."
    elif 100000 < valor_compra < 300000:
        descuento_aplicado= 0.1
        porcentaje_descuento="10%"
    elif 300000 <= valor_compra < 500000:
        descuento_aplicado=0.15
        porcentaje_descuento="15%"
    elif 500000 <= valor_compra:
        descuento_aplicado=0.2
    return descuento_aplicado

porcentaje_descuento =  calcular_descuento()

def porcentaje_de_descuento():
    global porcentaje_descuento
    if descuento_aplicado <= 0.1:
        porcentaje_descuento="No se aplicó ningún descuento."
    elif descuento_aplicado == 0.1:
        porcentaje_descuento = "10%"
    elif descuento_aplicado == 0.15:
        porcentaje_descuento = "15%"
    elif descuento_aplicado == 0.2:
        porcentaje_descuento = "20%"
    return porcentaje_descuento

def aplicar_descuento():
    global valor_compra
    global descuento_aplicado
    global precio_final
    precio_final=valor_compra - (valor_compra * calcular_descuento())
    return precio_final

print(f"""Cliente: {nombre_cliente}
Precio de compra: {valor_compra}
Descuento aplicado: {porcentaje_de_descuento()}
Precio final: {aplicar_descuento()}
""")

print("=" * 90)

# EJERCICIO 4: ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE DE UNA CIUDAD Y LA TEMPERATURA ACTUAL EN GRADOS CELSIUS, Y CLASIFICARLA

print("EJERCICIO 4. RECOMENDAR ABRIGO Y CLASIFICAR CLIMA SEGÚN TEMPERATURA ACTUAL.")
print("=" * 90)

nombre_ciudad=input("Ingrese el nombre de la ciudad: ")
temperatura_actual=float(input("Ingrese la temperatura actual en la ciudad en grados celsius: "))

def definir_temperatura():
    global temperatura_actual
    global grado_temperatura
    if temperatura_actual < 10:
        grado_temperatura="muy fría"
    elif 10 <= temperatura_actual <= 17:
        grado_temperatura="fría"
    elif 18 <= temperatura_actual <= 25:
        grado_temperatura= "templada"
    elif 26 <= temperatura_actual <= 32:
        grado_temperatura = "caliente"
    elif temperatura_actual >= 33:
        grado_temperatura = "muy caliente"
    return grado_temperatura

def recomendar_abrigo():
    global temperatura_actual
    global debe_llevar_abrigo
    if temperatura_actual >= 18:
        debe_llevar_abrigo="no se recomienda"
    else: debe_llevar_abrigo="se recomienda"
    return debe_llevar_abrigo

print(f"En la ciudad de {nombre_ciudad} hace una temperatura {definir_temperatura()} de {temperatura_actual}°, {recomendar_abrigo()} llevar abrigo para este día.")

print("=" * 90)

# EJERCICIO 5: ELABORAR UN ALGORITMO QUE SOLICITE EL NOMBRE DE UN EMPLEADO, LAS HORAS TRABAJADAS DURANTE EL MES Y EL VALOR DE CADA HORA 

print("EJERCICIO 5. SOLICITAR HORAS TRABAJADAS DEL MES DE UN EMPLEADO CON SU PAGO POR HORA Y RESTAR PENSIÓN")
print("=" * 90)

try:
    nombre_empleado=input("Ingrese el nombre del empleado: ")
    precio_hora= float(input("¿A cuánto paga cada hora? "))
    horas_trabajadas=float(input("¿Cúantas horas trabajó? "))
except ValueError:
    print("Asegurese de colocar números enteros positivos.")

def calcular_tarifa():
    global horas_trabajadas
    global extra_pagado
    if horas_trabajadas <= 160:
        extra_pagado=1
    elif horas_trabajadas > 160:
        extra_pagado= 1.25
    return extra_pagado

salario_bruto= horas_trabajadas * (precio_hora * calcular_tarifa())
salario_neto = salario_bruto - (salario_bruto * 0.08)

def calcular_horas_extras():
    global horas_extras
    if horas_trabajadas > 160:
        horas_extras= horas_trabajadas - 160
    else: horas_extras="No trabajó horas extras."
    return horas_extras

if precio_hora < 0:
    print("Por favor ingrese el valor de la hora en números positivos.")
elif horas_trabajadas < 0:
    print("Por favor ingrese las horas en números positivos")
else: print(f"""Nombre del empleado: {nombre_empleado}
Trabajó {horas_trabajadas} horas, con un valor de {precio_hora} c/u.
Horas extras: {calcular_horas_extras()}
Salario bruto: {salario_bruto}
Salario neto: {salario_neto}
""")