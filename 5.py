nota = float(input("Ingresa la calificación (0.0 a 5.0): "))

if nota < 0 or nota > 5:
    print("Calificación inválida")
elif nota >= 3.5:
    print("Aprobado")
else:
    print("No aprobado")