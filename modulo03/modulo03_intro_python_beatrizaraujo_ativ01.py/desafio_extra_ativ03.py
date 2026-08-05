opcao = ""

while opcao != "3":
    print("\n1 - Soma")
    print("2 - Subtração")
    print("3 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado:", numero1 + numero2)

    elif opcao == "2":
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        print("Resultado:", numero1 - numero2)

    elif opcao == "3":
        print("Programa encerrado.")

    else:
        print("Opção inválida.")