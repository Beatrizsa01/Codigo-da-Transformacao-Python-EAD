import sqlite3

conexao = sqlite3.connect("tarefas.db")
cursor = conexao.cursor()

cursor.execute("""
    CREATE TABLE IF NOT EXISTS Tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        tarefa TEXT NOT NULL
    )
""")

while True:
    print("\n--- GERENCIAMENTO DE TAREFAS ---")
    print("1 - Adicionar tarefa")
    print("2 - Visualizar tarefas")
    print("3 - Excluir tarefa")
    print("4 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")

        cursor.execute(
            "INSERT INTO Tarefas (tarefa) VALUES (?)",
            (tarefa,)
        )

        conexao.commit()
        print("Tarefa adicionada com sucesso!")

    elif opcao == "2":
        cursor.execute("SELECT * FROM Tarefas")
        tarefas = cursor.fetchall()

        print("\n--- LISTA DE TAREFAS ---")

        for tarefa in tarefas:
            print(tarefa)

    elif opcao == "3":
        id_tarefa = input("Digite o ID da tarefa que deseja excluir: ")

        cursor.execute(
            "DELETE FROM Tarefas WHERE id = ?",
            (id_tarefa,)
        )

        conexao.commit()
        print("Tarefa excluída com sucesso!")

    elif opcao == "4":
        break

    else:
        print("Opção inválida!")

conexao.close()