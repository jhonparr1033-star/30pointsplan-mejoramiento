a = float(input("Ingresa el primer número: "))
operador = input("Ingresa el operador (+, -, *, /): ")
b = float(input("Ingresa el segundo número: "))

if operador == "+":
    print("Resultado:", a + b)
elif operador == "-":
    print("Resultado:", a - b)
elif operador == "*":
    print("Resultado:", a * b)
elif operador == "/":
    if b != 0:
        print("Resultado:", a / b)
    else:
        print("Error: no se puede dividir entre cero")
else:
    print("Operador inválido")