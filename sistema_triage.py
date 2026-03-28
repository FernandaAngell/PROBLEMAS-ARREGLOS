
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#En una entidad de salud, se requiere que se atiendan los n
#pacientes que llegan en el transcurso de la noche, de acuerdo al triage
#que reporte el médico asignado a la valoración, para ello se maneja la
#siguiente tabla de clasificación:
#Nivel de urgencia Tipo de urgencia Tiempo de atención
#1 resucitación Inmediatamente
#2 emergencia 15 min
#3 urgencia 60 min
#4 urgencia menor 2 horas
#5 sin urgencia 4 horas
#Para el ingreso a la entidad se debe solicitar los datos personales:
#nombre completo, edad, eps y nivel de urgencia (triage), el programa
#debe mostrar al finalizar:
#- ¿Cuántos pacientes fueron atendidos?
#- ¿Si hay un sólo médico de turno, cuánto tiempo le tardará atender
#a todos los pacientes?
#- ¿Cuál es el nivel de urgencia que se presenta con mayor frecuencia?
#- El promedio de las edades del triage 3.
#- Organizar en un arreglo los nombres de los pacientes de triage 1 e imprimir el arreglo.


# Cantidad de pacientes
n = int(input("Ingrese la cantidad de pacientes: "))

# Contadores
total_tiempo = 0
conteo_triage = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0}

# Para promedio de edades triage 3
suma_edades_t3 = 0
cont_t3 = 0

# Lista para triage 1
pacientes_t1 = []

# Tabla de tiempos (en minutos)
tiempos = {
    1: 0,      # inmediato
    2: 15,
    3: 60,
    4: 120,
    5: 240
}

# Proceso
for i in range(1, n + 1):
    print(f"\nPaciente {i}")
    
    nombre = input("Nombre completo: ")
    edad = int(input("Edad: "))
    eps = input("EPS: ")
    triage = int(input("Nivel de urgencia (1-5): "))

    if triage in tiempos:
        conteo_triage[triage] += 1
        total_tiempo += tiempos[triage]

        # Guardar nombres triage 1
        if triage == 1:
            pacientes_t1.append(nombre)

        # Promedio edades triage 3
        if triage == 3:
            suma_edades_t3 += edad
            cont_t3 += 1

    else:
        print("Triage inválido ❌")

# Resultados
print("\n=== RESULTADOS ===")

# 1. Total pacientes
print(f"Pacientes atendidos: {n}")

# 2. Tiempo total
print(f"Tiempo total de atención (min): {total_tiempo}")

# 3. Nivel más frecuente
nivel_mas_frecuente = max(conteo_triage, key=conteo_triage.get)
print(f"Triage más frecuente: {nivel_mas_frecuente}")

# 4. Promedio edades triage 3
if cont_t3 > 0:
    promedio_t3 = suma_edades_t3 / cont_t3
else:
    promedio_t3 = 0

print(f"Promedio de edades (triage 3): {promedio_t3:.2f}")

# 5. Lista triage 1
print("\nPacientes triage 1:")
print(pacientes_t1)

#Realizado por Maria Fernanda Tolosa Angel
