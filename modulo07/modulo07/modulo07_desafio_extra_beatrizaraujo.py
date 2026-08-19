contatos = {}

while True:
    print("\n1 - Adicionar contato")
    print("2 - Remover contato")
    print("3 - Buscar contato")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Digite o nome: ")
        telefone = input("Digite o telefone: ")

        contatos[nome] = telefone
        print("Contato adicionado!")

    elif opcao == "2":
        nome = input("Digite o nome do contato que deseja remover: ")

        if nome in contatos:
            del contatos[nome]
            print("Contato removido!")
        else:
            print("Contato não encontrado.")

    elif opcao == "3":
        nome = input("Digite o nome que deseja buscar: ")

        if nome in contatos:
            print("Telefone:", contatos[nome])
        else:
            print("Contato não encontrado.")

    elif opcao == "4":
        print("Programa encerrado.")
        break

    else:
        print("Opção inválida.")