anio = int(input("Ingresa un año: "))

if anio % 400 == 0:
    print("Es un año bisiesto")
elif anio % 4 == 0 and anio % 100 != 0:
    print("Es un año bisiesto")
else:
    print("No es un año bisiesto")