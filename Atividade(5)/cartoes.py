from abc import ABC, abstractmethod
from pagamento import MetodoDePagamento

class CartaoWeb(ABC):
    def __init__(self, destinatario: str):
        self.destinatario = destinatario

    @abstractmethod
    def showMessage(self):
        pass

class DiaDosNamorados(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)
    
    def showMessage(self):
        print(f"Feliz dia dos Namorados, {self.destinatario}!")

class Natal(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Natal, {self.destinatario}!")

class Aniversario(CartaoWeb):
    def __init__(self, destinatario: str):
        super().__init__(destinatario)

    def showMessage(self):
        print(f"Feliz Aniversário, {self.destinatario}!")

'''Questão: Como ocorre o polimorfismo neste
código?
Resposta:
O polimorfismo permite usar uma única
variável de referência (cartao), do tipo 
CartaoWeb, para se referir a qualquer uma das
subclasses (DiaDosNamorados, Natal e 
Aniversario). 
O método showMessage chamado é sempre o da 
subclasse correspondente.'''