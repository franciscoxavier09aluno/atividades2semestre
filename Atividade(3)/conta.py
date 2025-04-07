from datetime import datetime

class Conta:
    def __init__(self, agencia, usuario, dataAbertura, saldo):
        self.agencia = agencia
        self.usuario = usuario
        self.dataAbertura = dataAbertura
        self.saldo = saldo

    def get_agencia(self):
        return self.agencia

    def get_usuario(self):
        return self.usuario

    def get_data_abertura(self):
        return self.dataAbertura

    def get_saldo(self):
        return self.saldo