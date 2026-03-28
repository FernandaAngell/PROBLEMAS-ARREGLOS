
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Se requiere desarrollar un programa que permita analizar la productividad de un equipo conformado por 4 empleados durante 3 días.
#Para ello, se deben representar los datos en dos matrices:
#- Matriz A: Contiene la cantidad de tareas completadas por cada empleado en cada día (números enteros mayores que 0).
#- Matriz B: Contiene el tiempo promedio en minutos que cada
#empleado tarda en completar una tarea en esos mismos días (números enteros mayores que 0).
#El objetivo es calcular una tercera matriz C, donde cada elemento
#represente el tiempo total trabajado por cada empleado en cada día.
#La operación para obtener cada elemento será el producto elemento a elemento (no multiplicación matricial tradicional), es decir: Cij=Aij×Bij
#El programa debe mostrar:
#- La matriz C completa, con el tiempo total trabajado (en minutos) por cada empleado en cada día.
#- Qué empleado acumuló más tiempo de trabajo sumando sus tres días.
#- Qué día registró el mayor tiempo total considerando a todos los empleados.

# Dimensiones
empleados = 4
dias = 3

# Matrices
A = []  # tareas
B = []  # tiempo por tarea
C = []  # tiempo total

print("=== INGRESO DE DATOS ===")

# Llenar matriz A
print("\nMatriz A (tareas completadas):")
for i in range(empleados):
    fila = []
    for j in range(dias):
        while True:
            val = int(input(f"Empleado {i+1}, Día {j+1}: "))
            if val > 0:
                fila.append(val)
                break
            else:
                print("Debe ser un número mayor que 0 ❌")
    A.append(fila)

# Llenar matriz B
print("\nMatriz B (tiempo por tarea en minutos):")
for i in range(empleados):
    fila = []
    for j in range(dias):
        while True:
            val = int(input(f"Empleado {i+1}, Día {j+1}: "))
            if val > 0:
                fila.append(val)
                break
            else:
                print("Debe ser un número mayor que 0 ❌")
    B.append(fila)

# Calcular matriz C (producto elemento a elemento)
for i in range(empleados):
    fila = []
    for j in range(dias):
        fila.append(A[i][j] * B[i][j])
    C.append(fila)

# Mostrar matriz C
print("\n=== MATRIZ C (Tiempo total en minutos) ===")
for fila in C:
    print(fila)

# Calcular total por empleado
total_empleado = []
for i in range(empleados):
    total = sum(C[i])
    total_empleado.append(total)

# Empleado con mayor tiempo
max_empleado = total_empleado.index(max(total_empleado)) + 1

# Calcular total por día
total_dia = []
for j in range(dias):
    suma = 0
    for i in range(empleados):
        suma += C[i][j]
    total_dia.append(suma)

# Día con mayor tiempo
max_dia = total_dia.index(max(total_dia)) + 1

# Resultados
print("\n=== RESULTADOS ===")
print(f"Empleado con más tiempo trabajado: Empleado {max_empleado}")
print(f"Día con mayor tiempo total: Día {max_dia}")

#Realizado por Maria Fernanda Tolosa Angel
