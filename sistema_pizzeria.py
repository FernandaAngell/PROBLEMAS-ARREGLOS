#Nombre: Maria Fernanda Tolosa Angel
#Grupo: 277
#Porgrama: Fundamentos de programación
#Código Fuente: Autoría propia

def mostrar_menu():
    print("\n=== MENÚ DE PIZZAS ===")
    print("1. Pequeña  (2 porciones)  - $10.000")
    print("2. Mediana  (4 porciones)  - $15.000")
    print("3. Larga    (6 porciones)  - $20.000")
    print("4. Familiar (8 porciones)  - $25.000")
    print("5. Extra Familiar (12 porciones) - $35.000")


def main():
    # Arreglos
    precios = [10000, 15000, 20000, 25000, 35000]
    porciones = [2, 4, 6, 8, 12]

    # Contadores
    cantidad_por_tipo = [0, 0, 0, 0, 0]

    total_ventas = 0
    total_porciones = 0

    num_clientes = int(input("Ingrese el número de clientes: "))

    for cliente in range(1, num_clientes + 1):
        print(f"\n--- Cliente {cliente} ---")

        continuar = True
        while continuar:
            mostrar_menu()

            try:
                tipo = int(input("Seleccione el tipo de pizza (1-5): "))
                
                if tipo < 1 or tipo > 5:
                    print("⚠️ Tipo inválido.")
                    continue

                cantidad = int(input("Cantidad de pizzas: "))

                if cantidad <= 0:
                    print("⚠️ La cantidad debe ser mayor a 0.")
                    continue

                indice = tipo - 1

                # Acumuladores
                cantidad_por_tipo[indice] += cantidad
                total_ventas += precios[indice] * cantidad
                total_porciones += porciones[indice] * cantidad

                # Preguntar si desea agregar más pizzas a la misma orden
                opcion = input("¿Desea agregar otro tipo de pizza? (1: sí, 0: no): ")
                if opcion == "0":
                    continuar = False

            except ValueError:
                print("⚠️ Ingrese valores válidos.")

    # Resultados finales
    print("\n=== RESULTADOS FINALES ===")

    tipos = ["Pequeña", "Mediana", "Larga", "Familiar", "Extra Familiar"]

    for i in range(5):
        print(f"{tipos[i]}: {cantidad_por_tipo[i]} pizzas vendidas")

    print(f"\n💰 Total de ventas: ${total_ventas}")
    print(f"🍽️ Total de porciones: {total_porciones}")


if __name__ == "__main__":
    main()