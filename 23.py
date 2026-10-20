notas = [3.0, 4.2, 2.8, 3.9, 4.8, 1.5]

aprobados = 0
reprobados = 0

for nota in notas:
    if nota >= 3.5:
        aprobados += 1
    else:
        reprobados += 1

print("Aprendices aprobados:", aprobados)
print("Aprendices reprobados:", reprobados)