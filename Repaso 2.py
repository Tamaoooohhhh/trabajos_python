#Ejercicio para una empresa de bus los siguientes destinos. Cada vía tiene su propio precio.

#Precio de los tiquetes
Destino_medellin_bogota = 120000
destino_medellin_cali = 1000000
destino_medellin_barranquilla = 150000
destino_medellin_cartagena = 200000

# Se debe solicitar destino, cantidad de ticketes, y según la cantidad de los ticketes va  a decidir cuántos nombres se piden.

# Bucle que reinicia las peticiones para generar una nueva factura
while True:
        try:
            destino_pasajero = int(input(f"""            ==TIQUETE DE BUS===\n        
            Rutas disponibles:

            1. Medellín --> Bogotá / Precio: {Destino_medellin_bogota}
            2. Medellín --> Cali / Precio: {destino_medellin_cali}
            3. Medellín --> Barranquilla / Precio: {destino_medellin_barranquilla}
            4. Medellín --> Cartagena / Precio: {destino_medellin_cartagena}
            5. Salir

            Ingrese su destino: """))

            if destino_pasajero == 1:
                valor_tiquete = Destino_medellin_bogota
                destino = "Bogotá"
            elif destino_pasajero == 2:
                destino = "Cali"
                valor_tiquete = destino_medellin_cali
            elif destino_pasajero == 3:
                destino = "Barranquilla"
                valor_tiquete = destino_medellin_barranquilla
            elif destino_pasajero == 4:
                destino = "Barranquilla"
                valor_tiquete = destino_medellin_cartagena
            elif destino_pasajero == 5:
                print("Saliendo del sistema...")
                break
            else:
                print("\n            Ingresa una opción disponible\n\n")
                break

            if destino_pasajero in range(1,4):
                nombres_pasajeros_restantes = 0
                pasajeros = []
                cantidad_de_tiquetes = int(input("¿Cuántos tiquetes desea adquirir? "))
                total_a_pagar = valor_tiquete * cantidad_de_tiquetes
                for i in range (cantidad_de_tiquetes):

                        global nombre_pasajeros_restantes
                                
                        nombre_pasajeros = input(f"Nombre del pasajero {i + 1}: ")
                        pasajeros.append(nombre_pasajeros)
                        nombres_pasajeros_restantes = cantidad_de_tiquetes - (i + 1)

                print(f"""Destino: {destino}
                Total a pagar: {total_a_pagar}
                Pasajeros: {pasajeros}
                """)

        except ValueError:
            print("Opción no válida")
            break



    









# Calcular total a pagar y debe demostrar el total a pagar, destino, nombre de los pasajeros y total a pagar.