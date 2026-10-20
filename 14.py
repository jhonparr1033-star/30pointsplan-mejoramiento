n = int(input("Ingresa un número entero positivo: "))
suma = 0

if n < 1:
    print("Debes ingresar un número positivo")
else:
    for i in range(1, n + 1):
        suma += i

    print("La suma total es:", suma)