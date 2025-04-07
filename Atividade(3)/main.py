from usuario import Usuario
from conta import Conta
from datetime import datetime
import random

def main():
    usuario = Usuario()

    rg = int(input("Digite o RG: "))
    cpf = int(input("Digite o CPF: "))
    nome = input("Digite o nome: ")
    data_nasc_str = input("Digite a data de nascimento (DD/MM/AAAA): ")
    data_nasc = datetime.strptime(data_nasc_str, "%d/%m/%Y")

    usuario.set_rg(rg)
    usuario.set_cpf(cpf)
    usuario.set_nome(nome)
    usuario.set_data_nascimento(data_nasc)

    agencia = random.randint(0, 999)
    data_abertura_str = input("Digite a data de abertura da conta (DD/MM/AAAA): ")
    data_abertura = datetime.strptime(data_abertura_str, "%d/%m/%Y")
    saldo = float(input("Digite o saldo inicial: "))

    conta = Conta(agencia, usuario, data_abertura, saldo)

    print("\n--- Dados da Conta ---")
    print(f"Agência: {conta.get_agencia()}")
    print(f"Data de Abertura: {conta.get_data_abertura().strftime('%d/%m/%Y')}")
    print(f"Saldo: R$ {conta.get_saldo():.2f}")

    print("\n--- Dados do Usuário ---")
    print(f"Nome: {usuario.get_nome()}")
    print(f"RG: {usuario.get_rg()}")
    print(f"CPF: {usuario.get_cpf()}")
    print(f"Data de Nascimento: {usuario.get_data_nascimento().strftime('%d/%m/%Y')}")

if __name__ == "__main__":
    main()