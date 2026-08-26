def calcular_media(notas):
    media = sum(notas) / len(notas)

    print("Média:", media)

    if media >= 7:
        print("Aluno aprovado!")
    else:
        print("Aluno reprovado!")


calcular_media([8, 7, 9])