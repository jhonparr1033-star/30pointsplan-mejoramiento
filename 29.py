asistencia = [True, False, True, True, False]

presentes = 0

for estado in asistencia:
    if estado == True:
        presentes += 1

porcentaje = (presentes / len(asistencia)) * 100

print("Asistencias:", presentes)
print("Porcentaje de asistencia:", porcentaje, "%")