alunos = {
    "Ana": [8.5, 7.0, 9.2, 6.8],
    "Carlos": [5.5, 6.0, 7.5, 8.0],
    "Mariana": [9.0, 8.5, 10.0, 9.8],
    "Lucas": [6.5, 7.2, 5.8, 6.9],
    "Fernanda": [7.8, 8.2, 7.0, 8.5]
}

while True:
    escolha = input("\nEscolha uma opção: \n[1] Adicionar \n[2] Atualizar \n[3] Remover \n[4] Exibir \n[5] Sair: ")

    if escolha == "1":
        nome = input("Nome do aluno: ")
        if nome in alunos:
            print("Aluno já adicionado!")
        else:
            notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
            alunos[nome] = notas
            print("Aluno adicionado.")

    elif escolha == "2":
        nome = input("Nome do aluno para atualizar: ")
        if nome in alunos:
            notas = [float(input(f"Nota {i+1}: ")) for i in range(4)]
            alunos[nome] = notas
            print("Notas atualizadas.")
        else:
            print("Aluno não encontrado!")

    elif escolha == "3":
        nome = input("Nome do aluno para remover: ")
        if nome in alunos:
            del alunos[nome]
            print("Aluno removido.")
        else:
            print("Aluno não encontrado!")

    elif escolha == "4":
        print("\nLista de alunos:")
        for nome, notas in alunos.items():
            media = sum(notas) / len(notas)
            print(f"{nome}: \nNotas {notas} - Média {media:.2f}")

    elif escolha == "5":
        print("Saiu.")
        break

    else:
        print("Opção inválida.")
