def contar_vocales(frase):
    return sum(1 for char in frase.lower() if char in 'aeiou')

frase = input("Ingrese una frase: ")
vocales = contar_vocales(frase)
print(f"Número total de vocales: {vocales}")