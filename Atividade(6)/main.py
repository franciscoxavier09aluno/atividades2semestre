from veiculo import Veiculo

def menu():
    print("\n=== Menu ===")
    print("1. Alugar Veículo")
    print("2. Devolver Veículo")
    print("3. Status do Veículo")
    print("4. Mostrar Total de Veículos")
    print("5. Sair")
    return input("Opção: ")

veiculo1 = Veiculo("ABC-1234", "Sedan", 100.0)
veiculo2 = Veiculo("ABC-5678", "SUV", 150.0)

veiculos = [veiculo1, veiculo2]

while True:
        opcao = menu()

        if opcao == "1":
            placa = input("Digite a placa do veículo a ser alugado: ")
            for veiculo in veiculos:
                if veiculo.placa == placa:
                    veiculo.alugar()
                    print(f"Veículo {placa} alugado com sucesso!")
                    break
            else:
                print("Veículo não encontrado.")

        elif opcao == "2":
            placa = input("Digite a placa do veículo a ser devolvido: ")
            for veiculo in veiculos:
                if veiculo.placa == placa:
                    veiculo.devolver()
                    print(f"Veículo {placa} devolvido com sucesso!")
                    break
            else:
                print("Veículo não encontrado.")

        elif opcao == "3":
            for veiculo in veiculos:
                status = "Alugado" if veiculo.status else "Disponível"
                print(f"Veículo {veiculo.placa}: {status}")

        elif opcao == "4":
            total = Veiculo.mostrar_total_veiculos()
        
        elif opcao == "5":
            print("Saindo...")

        else:
            print("Opção inválida. Tente novamente.")