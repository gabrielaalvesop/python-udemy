initial_counter=int(input("Digite um número para iniciar a contagem: "))

end_counter=int(input("Digite um número para finalizar a contagem: "))

step=int(input("Digite o valor do passo da contagem: "))

for counter in range(initial_counter, end_counter + 1, step):
    print(counter)
