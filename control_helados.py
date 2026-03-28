
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#La familia de Pepito ha celebrado sus cumpleaños desde el
#primer año de vida, y en el año 2026 cumplirá 6 años, por lo que
#nuevamente organizarán una fiesta con familiares y amigos. Los padres
#del niño son muy cuidadosos con sus finanzas y llevan un control
#detallado de sus gastos.
#El año anterior tuvieron un inconveniente con el presupuesto destinado
#a la compra de helados, ya que no lograron llevar un registro exacto.
#Para evitar que esto vuelva a ocurrir, le han solicitado desarrollar un
#programa que permita gestionar la compra y el control del dinero disponible.

#Requisitos del programa
#1. Entrada inicial:
#- Solicitar la cantidad de dinero disponible para realizar la compra de helados.
#2. Proceso de compra:
#- El usuario podrá comprar la cantidad de helados que desee, siempre que el dinero alcance.
#- Cada helado se selecciona según la siguiente Información:
#Tipo Descripción Valor
#1 vaso de Helado $2.500
#2 choco cono $2.000
#3 paleta Drácula $3.800
#4 polet $4.500
#5 platillo $1.800
#- Los valores deben almacenarse en un arreglo unidimensional,
#donde la posición 0 corresponde al primer tipo de helado, la
#posición 1 al segundo, y así sucesivamente:
#Posición 0 1 2 3 4
#$2.500 $2.000 $3.800 $4.500 $1.800
#- Después de cada compra, el programa debe mostrar el dinero
#restante para que el usuario tenga control del presupuesto.
#3. Condiciones para finalizar el ciclo de compra:
#- Cuando el dinero restante no alcance para comprar ningún tipo
#de helado (el programa debe mostrar un mensaje indicando esta
#situación).
#- O cuando el usuario decida no continuar comprando.
#Al terminar el proceso, el programa debe mostrar:
#• Cantidad total de helados comprados.
#• Cantidad de helados por cada tipo.
#• Valor total gastado.
#• Valor promedio por helado.
#• Dinero sobrante.

# Precios en arreglo (lista)
precios = [2500, 2000, 3800, 4500, 1800]

# Nombres (para mostrar)
nombres = ["Vaso de helado", "Choco cono", "Paleta Drácula", "Polet", "Platillo"]

# Contadores
cantidad_por_tipo = [0, 0, 0, 0, 0]
total_helados = 0
total_gastado = 0

# Dinero disponible
dinero = float(input("Ingrese el dinero disponible: "))

# Ciclo de compra
while True:
    print("\n=== MENÚ DE HELADOS ===")
    for i in range(5):
        print(f"{i+1}. {nombres[i]} - ${precios[i]}")

    # Verificar si alcanza para el más barato
    if dinero < min(precios):
        print("\nNo alcanza el dinero para comprar más helados ❌")
        break

    opcion = input("Seleccione un tipo (1-5) o '0' para salir: ")

    if opcion == "0":
        break

    if opcion.isdigit() and 1 <= int(opcion) <= 5:
        idx = int(opcion) - 1

        if dinero >= precios[idx]:
            dinero -= precios[idx]
            total_gastado += precios[idx]
            total_helados += 1
            cantidad_por_tipo[idx] += 1

            print(f"Compra exitosa ✅ - Dinero restante: ${dinero}")
        else:
            print("No tienes suficiente dinero para este helado ❌")
    else:
        print("Opción inválida ❌")

# Resultados
print("\n=== RESULTADOS ===")
print(f"Total de helados comprados: {total_helados}")

print("\nCantidad por tipo:")
for i in range(5):
    print(f"{nombres[i]}: {cantidad_por_tipo[i]}")

print(f"\nTotal gastado: ${total_gastado}")

# Promedio
if total_helados > 0:
    promedio = total_gastado / total_helados
else:
    promedio = 0

print(f"Valor promedio por helado: ${promedio:.2f}")
print(f"Dinero sobrante: ${dinero}")

#Realizado por Maria Fernanda Tolosa Angel
