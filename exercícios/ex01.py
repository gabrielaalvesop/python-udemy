primeiro_valor = input("Digite o primeiro valor: ")
segundo_valor = input("Digite o segundo valor: ")

if primeiro_valor > segundo_valor:
    print(f"O primeiro valor {primeiro_valor} é maior.")
elif segundo_valor > primeiro_valor:
    print(f"O segundo valor {segundo_valor} é maior.")
else:
    print("Os dois valores são iguais.")