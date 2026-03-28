
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

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