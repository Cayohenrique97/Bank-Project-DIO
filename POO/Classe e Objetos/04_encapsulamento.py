class Conta:
    def __init__(self, saldo=0):
        self._saldo = saldo

    def depositar(self, valor):
        self._saldo += 100

    def sacar(self, valor):
        pass
