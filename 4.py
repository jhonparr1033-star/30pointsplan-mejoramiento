Noa = int(input("Ingresa el primer número: "))
b = int(input("Ingresa el segundo número: "))
c = int(input("Ingresa el tercer número: "))

if a > b and a > c:
    print("El mayor es:", a)
elif b > a and b > c:
    print("El mayor es:", b)
elif c > a and c > b:
    print("El mayor es:", c)
else:
    print("Hay números iguales en el valor máximo")