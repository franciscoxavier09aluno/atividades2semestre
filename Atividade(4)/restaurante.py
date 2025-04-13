class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha
        self.numeroServidos = 0

    def descreverRestaurante(self):
        print(f"Restaurante: {self.nomeRestaurante}")
        print(f"Tipo de Cozinha: {self.tipoCozinha}")

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está aberto!")

    def getNumeroServidos(self):
        return self.numeroServidos

    def setNumeroServidos(self, valor):
        if valor >= 0:
            self.numeroServidos = valor

    def incrementeNumeroServidos(self, quantidade):
        total = self.getNumeroServidos() + quantidade
        self.setNumeroServidos(total)

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo de Cozinha: {self.tipoCozinha}"