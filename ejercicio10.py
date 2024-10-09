import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(caracteres) for _ in range(longitud))

longitud = int(input("Ingrese la longitud de la contraseña (mínimo 8): "))
if longitud >= 8:
    contrasena = generar_contrasena(longitud)
    print(f"Contraseña generada: {contrasena}")
else:
    print("La longitud debe ser al menos 8.")