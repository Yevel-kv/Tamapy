#!/usr/bin/env python3

class CuentaBancaria:
    def __init__(self, titular, saldo):
        movimientos = []
        self.titular = titular
        self.saldo = saldo
        self.movimientos = movimientos
    def depositar(self, monto):
        self.saldo = self.saldo + monto
        self.movimientos.append(f"Deposito de {monto}")
             
    def retirar(self, monto):
        if monto <= self.saldo:
            self.saldo = self.saldo - monto
            self.movimientos.append(f"Retiro de {monto}")
        else:
            print(f"\n [!] Error: Saldo insuficiente")
            self.movimientos.append(f"\n [!] Error: Intento de retiro sin fondos")

    def mostrar_saldo(self):
        print(f"\n {self.titular} tiene un saldo de {self.saldo}")
    def mostrar_movimientos(self):
        print(f"\n {self.titular} ha realizado los siguientes movimientos:")
        for movimiento in self.movimientos:
            print(f"\n [+] {movimiento}")

Rocio = CuentaBancaria("Rocio", 5000)
Rocio.depositar(1000)
Rocio.retirar(1500)
Rocio.mostrar_saldo()
Rocio.mostrar_movimientos()