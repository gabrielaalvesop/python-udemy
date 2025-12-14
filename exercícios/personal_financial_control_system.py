print("=== Sistema de Controle Financeiro Pessoal ===")

historico_financeiro = []

def exibir_menu():
    print("\nMenu:")
    print("1. Adicionar receita")
    print("2. Adicionar despesa")
    print("3. Listar histórico financeiro")
    print("4. Calcular saldo")
    print("5. Mostrar total de despesas por categoria")
    print("6. Sair")
    escolha = input("Escolha uma opção: ").strip()
    return escolha

def adicionar_receita():
    while True:
        try:
            valor = float(input("Digite o valor da receita: "))
            if valor <= 0:
                print("O valor deve ser positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    descricao = input("Digite a descrição da receita: ").strip()
    historico_financeiro.append({"tipo": "receita", "valor": valor, "descricao": descricao})
    print("Receita adicionada com sucesso!")

def adicionar_despesa():
    while True:
        try:
            valor = float(input("Digite o valor da despesa: "))
            if valor <= 0:
                print("O valor deve ser positivo.")
            else:
                break
        except ValueError:
            print("Entrada inválida. Digite um número válido.")
    descricao = input("Digite a descrição da despesa: ").strip()
    categoria = input("Digite a categoria da despesa (ex: alimentação, transporte, lazer): ").strip().title()
    historico_financeiro.append({"tipo": "despesa", "valor": valor, "descricao": descricao, "categoria": categoria})
    print("Despesa adicionada com sucesso!")

def listar_historico():
    if not historico_financeiro:
        print("Nenhum registro financeiro encontrado.")
        return
    print("\n--- Histórico Financeiro ---")
    for registro in historico_financeiro:
        if registro["tipo"] == "receita":
            print(f"Receita: R$ {registro['valor']:.2f} - {registro['descricao']}")
        else:
            print(f"Despesa: R$ {registro['valor']:.2f} - {registro['descricao']} (Categoria: {registro['categoria']})")

def calcular_saldo():
    saldo = sum(registro["valor"] if registro["tipo"] == "receita" else -registro["valor"] for registro in historico_financeiro)
    print(f"Saldo atual: R$ {saldo:.2f}")

def total_despesas_por_categoria():
    categorias = {}
    for registro in historico_financeiro:
        if registro["tipo"] == "despesa":
            categoria = registro["categoria"]
            categorias[categoria] = categorias.get(categoria, 0) + registro["valor"]
    if not categorias:
        print("Nenhuma despesa registrada.")
        return
    print("\n--- Total de Despesas por Categoria ---")
    for categoria, total in categorias.items():
        print(f"Categoria: {categoria} - Total de despesas: R$ {total:.2f}")


while True:
    escolha_usuario = exibir_menu()
    if escolha_usuario == "1":
        adicionar_receita()
    elif escolha_usuario == "2":
        adicionar_despesa()
    elif escolha_usuario == "3":
        listar_historico()
    elif escolha_usuario == "4":
        calcular_saldo()
    elif escolha_usuario == "5":
        total_despesas_por_categoria()
    elif escolha_usuario == "6":
        print("Saindo do sistema. Até mais!")
        break
    else:
        print("Opção inválida. Tente novamente.")
