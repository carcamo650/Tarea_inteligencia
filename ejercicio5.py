def es_primo(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

numero = int(input("Ingrese un número entero: "))
if es_primo(numero):
    print(f"{numero} es primo.")
else:
    print(f"{numero} no es primo.")