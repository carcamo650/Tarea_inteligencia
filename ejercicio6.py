def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        print(a, end=", ")
        a, b = b, a + b
    print()

n = int(input("Ingrese el número de terminos : "))
fibonacci(n)