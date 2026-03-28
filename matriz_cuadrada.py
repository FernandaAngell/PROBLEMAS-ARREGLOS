
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Desarrolle un programa que permita trabajar con una matriz cuadrada cuya dimensión será definida por el usuario.
#Recuerde que una matriz cuadrada tiene el mismo número de filas y columnas.
#Los elementos de la matriz deben cumplir las siguientes condiciones:
#• Ser números enteros.
#• Tener exactamente cuatro cifras (es decir, estar en el rango de 1000 a 9999).
#El programa debe realizar las siguientes operaciones:
#1)Identificar el número mayor y el número menor dentro de la matriz.
#- Calcular la suma de estos dos valores.
#- Determinar si el resultado obtenido es un número capicúa (es decir, se lee igual de izquierda a derecha que de derecha a izquierda).
#2)Calcular la sumatoria de todos los números pares presentes en la matriz.
#- Convertir el valor total de esta sumatoria a su representación binaria y mostrarla en pantalla.

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

#Realizado por Maria Fernanda Tolosa Angel
