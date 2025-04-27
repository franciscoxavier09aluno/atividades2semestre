class Veiculo:
    total_veiculos = 0

    def __init__(self, placa="ind", modelo="ind", diaria=0.0, __alugado=False):
        self.__placa = placa
        self.modelo = modelo
        self.diaria = diaria
        self.__alugado = False
        Veiculo.total_veiculos += 1

    def alugar(self):
        if not self.__alugado:
            self.__alugado = True
            print(f"Veículo {self.__placa} foi alugado.")
        else:
            print(f"Veículo {self.__placa} já está alugado.")

    def devolver(self):
        if self.__alugado:
            self.__alugado = False
            print(f"Veículo {self.__placa} foi devolvido.")
        else:
            print(f"Veículo {self.__placa} já está disponível.")

    def status(self):
        estado = "alugado" if self.__alugado else "disponível"
        print(f"Veículo {self.__placa} está {estado}.")

    @property
    def placa(self):
        return self.__placa
    @placa.setter
    def placa(self, value):
        print("A placa não pode ser modificada.")
    
    @classmethod
    def mostrar_total_veiculos(cls):
        print(f"Total de veículos: {cls.total_veiculos}")

    @staticmethod
    def calcular_preco_aluguel(dias, diaria):
        return dias * diaria