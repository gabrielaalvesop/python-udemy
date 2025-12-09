def par(numero):
    if numero % 2 == 0:
        return True
    else:
        return False
    
number = int(input("Digite um número: "))

if par(number):
    print(f"O número {number} é par.")
else:
    print(f"O número {number} é ímpar.")
    

