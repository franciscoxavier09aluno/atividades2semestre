from datetime import datetime

class Conta:
    def __init__(self, numero, agencia, usuario, dataAbertura, saldo=0):
        self.numero = numero
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def consultarSaldo(self):
        print(f"Saldo atual da conta {self.numero}: R${self.saldo:.2f}")

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            print(f"Depósito de R${valor:.2f} realizado.")
        else:
            print("Valor de depósito inválido.")

    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Saldo insuficiente para saque.")

    def transferir(self, valor, destino):
        if valor <= self.saldo:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada para {destino.usuario}.")
        else:
            print("Saldo insuficiente para transferência.")

    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_data_abertura(self):
        return self.dataAbertura

    def get_saldo(self):
        return self.saldo


class ContaPoupanca(Conta):
    def aplicarRendimento(self, taxa):
        rendimento = self.saldo * taxa
        self.saldo += rendimento
        print(f"Rendimento de R${rendimento:.2f} aplicado. Novo saldo: R${self.saldo:.2f}")


class ContaCorrente(Conta):
    def cobrarTarifaMensal(self):
        tarifa = 10.0
        self.saldo -= tarifa
        print(f"Tarifa mensal de R${tarifa:.2f} cobrada. Novo saldo: R${self.saldo:.2f}")


class ContaEspecial(ContaCorrente):
    def __init__(self, numero, agencia, usuario, dataAbertura, saldo=0, limite=500):
        super().__init__(numero, agencia, usuario, dataAbertura, saldo)
        self.limite = limite

    def consultarSaldo(self):
        print(f"Saldo: R${self.saldo:.2f} | Limite disponível: R${self.limite:.2f}")

    def sacar(self, valor):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            print(f"Saque de R${valor:.2f} realizado.")
        else:
            print("Limite insuficiente para saque.")

    def transferir(self, valor, destino):
        if valor <= self.saldo + self.limite:
            self.saldo -= valor
            destino.saldo += valor
            print(f"Transferência de R${valor:.2f} realizada para {destino.usuario}.")
        else:
            print("Limite insuficiente para transferência.")