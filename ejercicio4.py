class Calculadora:
    def sumar(self, a, b):
        return a + b

    def restar(self, a, b):
        return a - b

    def multiplicar(self, a, b):
        return a * b

    def dividir(self, a, b):
        if b == 0:
            return "Error: la división entre cero no está permitida."
        return a / b
    
calc = Calculadora()
print("Suma:", calc.sumar(5, 3))
print("Resta:", calc.restar(5, 3))
print("Multiplicación:", calc.multiplicar(5, 3))
print("División:", calc.dividir(5, 0))