agenda = {}

nome = input("Nome: ")
telefone = input("Telefone: ")
agenda[nome] = telefone

print(agenda)

buscar = input("Buscar contato: ")
print(agenda[buscar])

remover = input("Remover contato: ")
del agenda[remover]

print(agenda)