
lista = []

lista.append(input("Digite um item: "))
lista.append(input("Digite outro item: "))

print(lista)

item = input("Qual item deseja remover? ")
lista.remove(item)

print(lista)