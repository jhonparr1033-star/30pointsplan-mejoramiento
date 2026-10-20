numeros = [12, 7, 4, 9, 15, 20, 3, 8, 11, 6]

pares = []
impares = []

for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
    else:
        impares.append(numero)

print("Números pares:", pares)
print("Números impares:", impares)