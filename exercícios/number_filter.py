print("Lista de Números:")
list_of_numbers=[10, 23, 45, 67, 89, 12, 34, 56, 78, 90]
print(list_of_numbers)

print("Números Pares:")
even_numbers = [num for num in list_of_numbers if num % 2 == 0]
print(even_numbers)

print("Números Ímpares:")
odd_numbers = [num for num in list_of_numbers if num % 2 != 0]
print(odd_numbers)

print("Soma dos Números Pares:")
sum_even = sum(even_numbers)
print(sum_even)

print("Média dos Números Ímpares:")
median_odd = sum(odd_numbers) / len(odd_numbers)
print(median_odd)