from abc import ABC, abstractmethod

class MetodoDePagamento(ABC):
    def __init__(self, valor: float):
        self.valor = valor

    @abstractmethod
    def pagar(self):
        pass

class CartaoCredito(MetodoDePagamento):
    def pagar(self):
        taxa = self.valor * 0.05
        valor_final = self.valor + taxa
        print(f"Pagamento com Cartão de Crédito:")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Taxa de 5%: R${taxa:.2f}")
        print(f"Valor final: R${valor_final:.2f}")

class BoletoBancario(MetodoDePagamento):
    def pagar(self):
        desconto = self.valor * 0.02
        valor_final = self.valor - desconto
        print(f"Pagamento com Boleto Bancário:")
        print(f"Valor original: R${self.valor:.2f}")
        print(f"Desconto de 2%: R${desconto:.2f}")
        print(f"Valor final: R${valor_final:.2f}")

class Pix(MetodoDePagamento):
    def pagar(self):
        print(f"Pagamento com Pix:")
        print(f"Valor original e final: R${self.valor:.2f} (sem descontos ou acréscimos)")

'''Questão: Como o uso de polimorfismo 
facilitou a implementação do sistema de 
pagamento?
Resposta:
Polimorfismo permite usar uma única variável 
(pagamento), do tipo MetodoPagamento,
para armazenar qualquer tipo de método de 
pagamento concreto (Pix, Boleto, Cartão),
isso facilita a extensão do sistema e a 
manutenção do código'''