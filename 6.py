compra = float(input("Ingresa el valor de la compra: "))

if compra > 200000:
    descuento = compra * 0.20
elif compra > 100000:
    descuento = compra * 0.10
else:
    descuento = 0

total = compra - descuento

print("Descuento:", descuento)
print("Total a pagar:", total)