import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Clientes (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        email TEXT NOT NULL
    )
""")

while True:
    print("\n--- MENU ---")
    print("1 - Inserir cliente")
    print("2 - Consultar clientes")
    print("3 - Atualizar cliente")
    print("4 - Deletar cliente")
    print("5 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        email = input("Email: ")

        cursor.execute(
            "INSERT INTO Clientes (nome, email) VALUES (?, ?)",
            (nome, email)
        )

        conexao.commit()
        print("Cliente inserido com sucesso!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM Clientes")
        clientes = cursor.fetchall()

        for cliente in clientes:
            print(cliente)

    elif opcao == "3":
        id_cliente = input("Digite o ID do cliente: ")
        nome = input("Novo nome: ")
        email = input("Novo email: ")

        cursor.execute(
            "UPDATE Clientes SET nome = ?, email = ? WHERE id = ?",
            (nome, email, id_cliente)
        )

        conexao.commit()
        print("Cliente atualizado com sucesso!")

    elif opcao == "4":
        id_cliente = input("Digite o ID do cliente: ")

        cursor.execute(
            "DELETE FROM Clientes WHERE id = ?",
            (id_cliente,)
        )

        conexao.commit()
        print("Cliente deletado com sucesso!")

    elif opcao == "5":
        break

    else:
        print("Opção inválida!")

conexao.close()