class Carro:

    def __init__(self, marca, modelo, ano, cor):

        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.cor = cor

    def ligar_carro(self):
        print("Ligando o carro!")

    def parar_carro(self):
        print("Parando o carro!")

carro1 = Carro("Fiat", "Uno Mille1.0", "2012", "Preto")
 
print(carro1.marca, carro1.modelo, carro1.ano, carro1.cor)

carro1.ligar_carro()

carro1.parar_carro()