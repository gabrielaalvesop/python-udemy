nome_usuario = input("Digite o nome do usuário: ")
tamanho_nome = len(nome_usuario)

if tamanho_nome <= 4:
    print("Nome curto.")
elif 5 <= tamanho_nome <=6:
    print("Seu nome é normal.")
else:
    print("Nome muito grande.")