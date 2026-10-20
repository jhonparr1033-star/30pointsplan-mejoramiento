clave_correcta = "1234"
intentos = 0
acceso = False

while intentos < 3 and acceso == False:
    clave = input("Ingresa la clave: ")
    intentos += 1

    if clave == clave_correcta:
        acceso = True
        print("Acceso concedido")
    else:
        print("Clave incorrecta")

if acceso == False:
    print("Cuenta bloqueada")