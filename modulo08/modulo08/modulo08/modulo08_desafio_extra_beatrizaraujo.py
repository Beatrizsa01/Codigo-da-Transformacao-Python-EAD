usuarios = {
    "Beatriz": "5762"
}


def validar_login(usuario, senha):
    if usuario in usuarios and usuarios[usuario] == senha:
        print("Login realizado com sucesso!")
    else:
        print("Usuário ou senha incorretos.")


usuario = input("Digite o usuário: ")
senha = input("Digite a senha: ")

validar_login(usuario, senha)