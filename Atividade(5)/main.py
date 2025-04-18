from cartoes import DiaDosNamorados, Natal, Aniversario
from pagamento import CartaoCredito, BoletoBancario, Pix, MetodoDePagamento

def escolher_cartao():
    print("Escolha o tipo de cartão:")
    print("1 - Dia dos Namorados")
    print("2 - Natal")
    print("3 - Aniversário")
    tipo = input("Opção: ")

    destinatario = input("Digite o nome do destinatário: ")

    if tipo == "1":
        return DiaDosNamorados(destinatario)
    elif tipo == "2":
        return Natal(destinatario)
    elif tipo == "3":
        return Aniversario(destinatario)
    else:
        print("Tipo de cartão inválido.")
        exit()

def escolher_pagamento():
    try:
        valor = float(input("Digite o valor da compra: R$ "))
    except ValueError:
        print("Valor inválido.")
        exit()

    print("Escolha o método de pagamento:")
    print("1 - Cartão de Crédito")
    print("2 - Boleto Bancário")
    print("3 - Pix")
    opcao = input("Opção: ")

    if opcao == "1":
        return CartaoCredito(valor)
    elif opcao == "2":
        return BoletoBancario(valor)
    elif opcao == "3":
        return Pix(valor)
    else:
        print("Opção de pagamento inválida.")
        exit()

def main():
    print("\n--- Sistema de Cartões Web ---")
    cartao = escolher_cartao()
    cartao.showMessage()

    print("\n--- Pagamento ---")
    pagamento = escolher_pagamento()
    pagamento.pagar()

if __name__ == "__main__":
    main()