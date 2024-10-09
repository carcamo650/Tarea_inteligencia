class CuentaBancaria:
    def _init_(self, titular):
        self.titular = titular
        self.saldo = 0.0

    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depositado: {cantidad}. Saldo actual: {self.saldo}")

    def retirar(self, cantidad):
        if cantidad <= self.saldo:
            self.saldo -= cantidad
            print(f"Retirado: {cantidad}. Saldo actual: {self.saldo}")
        else:
            print("Fondos insuficientes.")

    def mostrar_saldo(self):
        print(f"Saldo actual: {self.saldo}")

cuenta = CuentaBancaria("Maynor Carcamo") 
cuenta.depositar(100)
cuenta.retirar(30)
cuenta.mostrar_saldo()