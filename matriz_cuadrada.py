
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

# Solicitar tamaño
n = int(input("Ingrese la dimensión de la matriz (n x n): "))

# Crear matriz
matriz = []

print("\nIngrese los valores (números de 4 cifras):")

for i in range(n):
    fila = []
    for j in range(n):
        while True:
            num = int(input(f"Elemento [{i}][{j}]: "))
            
            # Validar que tenga 4 cifras
            if 1000 <= num <= 9999:
                fila.append(num)
                break
            else:
                print("Error ❌: Debe ser un número de 4 cifras (1000-9999)")
    
    matriz.append(fila)

# Inicializar variables
mayor = matriz[0][0]
menor = matriz[0][0]
suma_pares = 0

# Recorrer matriz
for fila in matriz:
    for num in fila:
        # Mayor y menor
        if num > mayor:
            mayor = num
        if num < menor:
            menor = num
        
        # Suma de pares
        if num % 2 == 0:
            suma_pares += num

# Suma mayor + menor
suma_extremos = mayor + menor

# Función capicúa
def es_capicua(numero):
    return str(numero) == str(numero)[::-1]

# Convertir a binario
binario = bin(suma_pares)[2:]

# Resultados
print("\n=== RESULTADOS ===")
print(f"Número mayor: {mayor}")
print(f"Número menor: {menor}")
print(f"Suma (mayor + menor): {suma_extremos}")

if es_capicua(suma_extremos):
    print("La suma es capicúa ✅")
else:
    print("La suma NO es capicúa ❌")

print(f"\nSuma de números pares: {suma_pares}")
print(f"En binario: {binario}")