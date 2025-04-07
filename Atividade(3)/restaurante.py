class Restaurante:
    def __init__(self, nomeRestaurante, tipoCozinha):
        self.nomeRestaurante = nomeRestaurante
        self.tipoCozinha = tipoCozinha

    def abrirRestaurante(self):
        print(f"O restaurante {self.nomeRestaurante} está aberto!")

    def __str__(self):
        return f"Restaurante: {self.nomeRestaurante} | Tipo de Cozinha: {self.tipoCozinha}"


restaurante1 = Restaurante("Temperos da Vó", "Comida Caseira")
restaurante2 = Restaurante("Na Brasa", "Churrascaria")
restaurante3 = Restaurante("Le Bistrô", "Comida Francesa")

print(restaurante1)
print(restaurante2)
print(restaurante3)

restaurante1.abrirRestaurante()