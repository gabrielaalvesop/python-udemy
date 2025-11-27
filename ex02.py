numero_inteiro = int(input("Digite um número inteiro: "))

if numero_inteiro % 2 == 0:
    print(f"O número {numero_inteiro} é par.")
elif numero_inteiro % 2 != 0:
    print(f"O número {numero_inteiro} é ímpar.")
else:
    print("Esse não é um número inteiro válido.")  
    