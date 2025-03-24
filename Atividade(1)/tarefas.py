tarefas = []

while True:
    escolha = input("\nEscolha uma opção: \n[1] Adicionar \n[2] Concluir \n[3] Listar \n[4] Sair: ")

    if escolha == "1":
        titulo = input("Título da tarefa: ")
        descricao = input("Descrição: ")
        tarefas.append({"titulo": titulo, "descricao": descricao, "status": "Pendente"})
        print("Tarefa adicionada.")

    elif escolha == "2":
        titulo = input("Título da tarefa a concluir: ")
        for tarefa in tarefas:
            if tarefa["titulo"] == titulo and tarefa["status"] == "Pendente":
                tarefa["status"] = "Concluído"
                print("Tarefa marcada como concluída.")
                break
        else:
            print("Tarefa não encontrada ou já foi concluída.")

    elif escolha == "3":
        print("\nTarefas Pendentes:")
        for tarefa in tarefas:
            if tarefa["status"] == "Pendente":
                print(f"- {tarefa['titulo']}: {tarefa['descricao']}")

        print("\nTarefas Concluídas:")
        for tarefa in tarefas:
            if tarefa["status"] == "Concluído":
                print(f"- {tarefa['titulo']}")

    elif escolha == "4":
        print("Saiu.")
        break

    else:
        print("Opção inválida.")
