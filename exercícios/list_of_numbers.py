def list_of_numbers():
    numbers = []
    for i in range(1, 11):
        number = int(input(f"Digite o {i}º número: "))
        numbers.append(number)
    return numbers

numbers = list_of_numbers()

biggest_number = max(numbers)
print(f"O maior número digitado foi: {biggest_number}")

smallest_number = min(numbers)
print(f"O menor número digitado foi: {smallest_number}")

media = sum(numbers) / len(numbers)
print(f"A média dos números digitados é: {media}")

quantity_numbers = len(numbers)
print(f"A quantidade de números digitados é: {quantity_numbers}")