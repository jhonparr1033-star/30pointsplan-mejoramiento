correos = [
    "diego@sena.edu.co",
    "usuario.com",
    "jhonparr@gmail.com",
    "correo@",
    "jhon@hotmail.com"
]

for correo in correos:
    if "@" in correo and "." in correo:
        print(correo, "- Formato válido")
    else:
        print(correo, "- Formato inválido")