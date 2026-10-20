numero = int(input("Ingresa un número entero positivo: "))
factorial = 1

if numero < 0:
    print("No se acepta un número negativo")
else:
    for i in range(1, numero + 1):
        factorial *= i

    print("El factorial es:", factorial)