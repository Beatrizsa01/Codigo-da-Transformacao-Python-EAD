def maior_menor(numeros):
    maior = max(numeros)
    menor = min(numeros)

    return maior, menor


numeros = [5, 8, 2, 10, 4]

maior, menor = maior_menor(numeros)

print("Maior:", maior)
print("Menor:", menor)