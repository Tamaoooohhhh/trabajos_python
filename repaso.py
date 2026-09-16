# EJERCICIO: PREGUNTAR NOMBRE DEL PRODUCTO, CANTIDAD, PRECIO. MOSTRAR EL SUBTOTAL, CALCULAR EL IVA DEL 19%, TOTAL A PAGAR. PREGUNTAR SI SE DESEA AÑADIR PROPINA; SI ES ASÍ, SUMAR UN 10%; SI NO, DECIRLE TACAÑO

nombre_producto=input("Ingrese el nombre del producto: ")
cantidad_productos=int(input("¿Cuantós productos adquirió? "))
precio_producto=float(input("¿Cúanto cuesta el producto? "))


valor_subtotal= precio_producto * cantidad_productos
valor_iva= valor_subtotal * 0.19
valor_con_iva= valor_subtotal + (valor_subtotal * 0.19)
valor_con_propina= valor_con_iva + (valor_con_iva * 0.10)
respuesta_positiva= ["sí", "si"] # OTRAS MANERAS DE HACER: propina == "si" or propina == "Si" or propina =="sí"
respuesta_negativa= "no"

propina= input("¿Desea añadir propina? ").lower().strip()
if propina in respuesta_positiva:
    print(f"""PRODUCTO: {nombre_producto} 
x {cantidad_productos} unidades.
PRECIO UNITARIO: {precio_producto}
SUBTOTAL: {valor_subtotal}
IVA 19%: {valor_iva}
¿AÑADIÓ PROPINA? SÍ
VALOR TOTAL: {valor_con_propina} 
""")
elif propina in respuesta_negativa:
    print(f"""PRODUCTO: {nombre_producto} x {cantidad_productos} unidades.
PRECIO UNITARIO: {precio_producto}
SUBTOTAL: {valor_subtotal}
IVA 19%: {valor_iva}
¿AÑADIÓ PROPINA? NO. TACAÑO.
VALOR TOTAL: {valor_con_iva} 
""")
else: print("No se ha efectuado correctamente la factura.")