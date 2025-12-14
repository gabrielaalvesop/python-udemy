NOTES_AVALIABLE = [100, 50, 20, 10, 5, 2]

def withdrawal_amount():
    while True:
        try:
            value = float(input("Digite o valor que deseja sacar: R$ "))
            if value <= 0:
                print("Por favor, insira um valor positivo.")
            elif value % 2 != 0:
                print("Não é possível sacar valores ímpares com as notas disponíveis.")
            else:
                return value
        except ValueError:
            print("Entrada inválida. Por favor, insira um número válido.")

def calculate_grades(value, notes=NOTES_AVALIABLE):
    result = {}
    for note in notes:
        amount = value // note
        result[note] = int(amount)
        value -= amount * note
    return result, value


value = withdrawal_amount()
necessary_notes, rest = calculate_grades(value)

print("\nNotas necessárias para o saque:")
for note, amount in necessary_notes.items():
    if amount > 0:
        print(f"{amount} nota(s) de R$ {note}")

if rest > 0:
    print("Não foi possível sacar o valor exato com as notas disponíveis.")
