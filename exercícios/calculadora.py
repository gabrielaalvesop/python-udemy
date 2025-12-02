while True:
    numero_1 = float(input("Digite o primeiro número: "))
    numero_2 = float(input("Digite o segundo número: "))
    operacao = input("Digite a operação (+, -, *, /): ").strip()
    
    if operacao == '+':
        resultado = numero_1 + numero_2
    elif operacao == '-':
        resultado = numero_1 - numero_2
    elif operacao == '*':
        resultado = numero_1 * numero_2
    elif operacao == '/':
        resultado = numero_1 / numero_2
    else:
        print("Operação inválida. Tente novamente.")
        continue
        
    print(f"O resultado de {numero_1} {operacao} {numero_2} é: {resultado}")
    
    sair = input("Deseja sair da calculadora? (s/n): ").strip().lower()
    
    if sair == 's':
        print("Encerrando a calculadora. Até mais!")
        break
    