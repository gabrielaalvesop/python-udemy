print("=== Cadastro de pessoas ===")

def register_person():
    name = input("Digite o nome: ").strip().title()
    while True:
        age = input("Digite a idade: ").strip()
        if age.isdigit() and int(age) >= 0:
            age = int(age)
            break
        else:
            print("Por favor, digite uma idade válida.")
    profession = input("Digite a profissão: ").strip().title()
    
    return {"nome": name, "idade": age, "profissão": profession}

def show_people(people_list, title):
    if not people_list:
        print(f"\n=== {title} ===\nNenhuma pessoa encontrada.")
        return
    print(f"\n=== {title} ===")
    for index, person in enumerate(people_list, start=1):
        print(f"{index}. Nome: {person['nome']}, Idade: {person['idade']}, Profissão: {person['profissão']}")

people = []

while True:
    people.append(register_person())
    continue_registration = input("Deseja cadastrar outra pessoa? (s/n): ").strip().lower()
    if continue_registration != 's':
        break

show_people(people, "Pessoas cadastradas")

adults = [person for person in people if person['idade'] >= 18]
show_people(adults, "Pessoas maiores de 18 anos")

search_profession = input("\nDigite uma profissão para buscar: ").strip().title()
found_people = [person for person in people if person['profissão'] == search_profession]
show_people(found_people, f"Pessoas com a profissão '{search_profession}'")
    