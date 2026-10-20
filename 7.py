edad = int(input("Ingresa tu edad: "))

if edad < 0:
    print("Edad inválida")
elif edad < 12:
    print("Niño")
elif edad <= 17:
    print("Adolescente")
elif edad <= 59:
    print("Adulto")
else:
    print("Adulto mayor")