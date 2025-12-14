password = input("Digite a senha com no mínimo 8 caracteres, com pelo menos 1 número e 1 letra maiúscula: ")

if len(password) < 8:
    print("A senha deve ter no mínimo 8 caracteres.")
elif not any(c.isupper() for c in password):
    print("A senha deve conter pelo menos uma letra maiúscula.")
elif not any(c.isdigit() for c in password):
    print("A senha deve conter pelo menos um número.")
else:
    print("Senha válida.")