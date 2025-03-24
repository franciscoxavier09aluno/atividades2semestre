estoque = {
  "Caju": 5,
  "Banana": 6,
  "Melancia": 4
}

while True:
  print("\nOpções:")
  print("1 - Adicionar produto")
  print("2 - Remover produto")
  print("3 - Atualizar produto")
  print("4 - Exibir estoque")
  print("5 - Sair")
  
  escolha = input("Escolha uma opção: ")
  if escolha == "1":
        produto = input("Forneça o nome do produto: ")
        if produto in estoque:
            print("Produto já existente.")
        else:
            quantidade = int(input("Forneça a quantidade do produto: "))
            estoque[produto] = quantidade
            print(f"Produto '{produto}' adicionado com sucesso.")
            
  elif escolha == "2":
        produto = input("Forneça o nome do produto a ser removido: ")
        if produto in estoque:
            del estoque[produto]
            print(f"Produto '{produto}' removido com sucesso.")
        else:
            print("Produto não encontrado.")

  elif escolha == "3":
        produto = input("Nome do produto para atualizar: ")
        if produto in estoque:
            quantidade = int(input("Quantidade a adicionar ou remover: "))
            estoque[produto] += quantidade
            print("Estoque atualizado.")
        else:
            print("Produto não encontrado.")

  elif escolha == "4":
        if estoque:
            print("\nEstoque atual:")
            for produto, quantidade in estoque.items():
                print(f"{produto}: {quantidade}")
        else:
            print("Estoque vazio.")

  elif escolha == "5":
        print("Saiu.")
        break

  else:
        print("Opção inválida, tente novamente.")