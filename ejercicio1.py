class Rectangulo:
    def _init_(self, base, altura):
        self.base = base
        self.altura = altura

    def area(self):
        return self.base * self.altura

    def perimetro(self):
        return 2 * (self.base + self.altura)

rect = Rectangulo(5, 3)
print("El area es:", rect.area())
print("El perimetro es :", rect.perimetro())