nombre = "Mateo"
edad = 17
ciudad_nacimiento = "Medellín"
tiene_deudas = True

def consulta_deudas(): #FUNCIÓN PARA DEVOLVER LA RESPUESTA DE SI POSEE O NO DEUDAS A PARTIR DEL BOOLEAN
    if tiene_deudas == True: return "Sí tiene deudas."; 
    else: return "No tiene deudas";

# PRINT UTILIZANDO SALTOS DE LINEA Y COMILLA POR CADA CONSULTA, SIN LLAMAR A LAS VARIABLES

print("Nombre: Mateo\n"
 "Edad: 17\n"
 "Ciudad de nacimiento: Medellín\n"
 "¿Tiene deudas?: Sí\n"  )

 # PRINT DE VARIAS LINEAS UTILIZANDO F-STRING CON TRES COMILLAS, UTILIZANDO LAS VARIABLES

print(f"""Nombre: {nombre}.
Edad: {edad}.
Ciudad de nacimiento: {ciudad_nacimiento}.
¿Tiene deudas? {consulta_deudas()}""") #LLAMADO A LA FUNCIÓN PARA LA CONSULTA DE EXISTENCIA DE DEUDA



