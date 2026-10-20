inventario = [
    ("Mouse", 15),
    ("Teclado", 3),
    ("Monitor", 8),
    ("Cable HDMI", 2)
]

for producto, cantidad in inventario:
    print("Producto:", producto)
    print("Cantidad:", cantidad)

    if cantidad < 5:
        print("Advertencia: Stock crítico")

    print("--------------------")