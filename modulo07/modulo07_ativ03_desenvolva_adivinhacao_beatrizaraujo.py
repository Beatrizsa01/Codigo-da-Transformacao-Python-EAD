import random
import math

print("___________________________")
print(" 🎯 JOGO DE ADIVINHAÇÃO  🎯")
print("____________________________")
print("Estou pensando em um número de 1 a 24.")
print("Você tem 6 chances para acertar!\n")

numero_secreto = random.randint(1, 24)

for tentativa in range(1, 7):

    palpite = int(input(f"Tentativa {tentativa}/6: Digite seu palpite: "))

    diferenca = math.fabs(numero_secreto - palpite)

    if palpite == numero_secreto:
        print("Você acertou! ✔")
        print(f"Você acertou em {tentativa} tentativa(s)!")
        break

    elif diferenca <= 3:
        print("🔍 Muito perto!")

    elif palpite < numero_secreto:
        print("💡 Dica: O número secreto é MAIOR!")

    else:
        print("💡 Dica: O número secreto é MENOR!")

else:
    print("\n Você perdeu! ❌")
    print(f"O número secreto era {numero_secreto}.")