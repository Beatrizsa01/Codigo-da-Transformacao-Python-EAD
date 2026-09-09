import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("""
    SELECT * FROM Clientes
    WHERE nome LIKE 'A%'
""")

clientes = cursor.fetchall()

print("Clientes com o nome começando com A:")

for cliente in clientes:
    print(cliente)

conexao.close()