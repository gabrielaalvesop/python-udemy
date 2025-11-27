hora = int(input("Digite a hora atual (0-23): "))

if 0 <= hora < 12:
    print("Bom dia!")
elif 12 <= hora < 18:
    print("Boa tarde!")
elif 18 <= hora <= 23:
    print("Boa noite!")
else:
    print("Hora inválida! Por favor, insira um valor entre 0 e 23.")